#!/usr/bin/env python3
"""
Kimi Quota MCP Server

Implements the Model Context Protocol (stdio transport) to expose the
Kimi Code usage/quota API as a tool callable by the agent.

Protocol: JSON-RPC 2.0 over stdin/stdout
          (https://spec.modelcontextprotocol.io)
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error

# ── Config ────────────────────────────────────────────────────────────

DEFAULT_BASE_URL = "https://api.kimi.com/coding/v1"
USAGE_ENDPOINT = "/usages"

# ── Helpers ───────────────────────────────────────────────────────────


def kimi_code_home():
    return os.environ.get("KIMI_CODE_HOME") or os.path.join(
        os.path.expanduser("~"), ".kimi-code"
    )


def credential_path():
    return os.path.join(kimi_code_home(), "credentials", "kimi-code.json")


def load_token():
    path = credential_path()
    if not os.path.isfile(path):
        return None, "Credential file not found. Run `/login` first."
    try:
        with open(path) as f:
            cred = json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        return None, f"Failed to read credentials: {exc}"

    token = cred.get("access_token")
    if not token:
        return None, "No access_token in credentials."

    expires_at = cred.get("expires_at", 0)
    if time.time() >= expires_at:
        return token, "Token may be expired. Try `/login` to refresh."

    return token, None


def base_url():
    return (os.environ.get("KIMI_CODE_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")


def fetch_usage(token):
    url = base_url() + USAGE_ENDPOINT
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read()), None
    except urllib.error.HTTPError as exc:
        msg = exc.read().decode(errors="replace")
        return None, f"API error {exc.code}: {msg[:300]}"
    except urllib.error.URLError as exc:
        return None, f"Network error: {exc.reason}"
    except Exception as exc:
        return None, f"Unexpected error: {exc}"


def format_limits(limits):
    """Pretty-print the limits array (includes 5h rolling rate limit)."""
    lines = []
    for i, lim in enumerate(limits or []):
        w = lim.get("window", {})
        d = lim.get("detail", {})
        duration = w.get("duration")
        unit = w.get("timeUnit", "")
        used = d.get("used")
        limit = d.get("limit")
        remaining = d.get("remaining")

        if duration and "MINUTE" in unit:
            label = f"{duration // 60}h rolling limit" if duration >= 60 else f"{duration}m limit"
        elif duration and "HOUR" in unit:
            label = f"{duration}h limit"
        elif duration and "DAY" in unit:
            label = f"{duration}d limit"
        else:
            label = f"Limit #{i + 1}"

        if limit is not None and used is not None and remaining is not None:
            pct = (int(used) / int(limit)) * 100 if int(limit) > 0 else 0
            bar = _bar(pct)
            lines.append(
                f"  {label}: {used}/{limit} used ({remaining} remaining) {pct:.0f}%\n"
                f"    {bar}"
            )
        else:
            lines.append(f"  {label}: {json.dumps(d or lim)}")
    return "\n".join(lines)


def _bar(pct, width=20):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


# ── MCP protocol (stdio transport) ────────────────────────────────────


def send(obj):
    line = json.dumps(obj, ensure_ascii=False)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def read_request():
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            # non-JSON lines are ignored per MCP spec
            pass
    return None


def handle_initialize(msg):
    send({
        "jsonrpc": "2.0",
        "id": msg.get("id"),
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "kimi-quota",
                "version": "1.0.0"
            }
        }
    })
    log("initialize → done")


def handle_tools_list(msg):
    send({
        "jsonrpc": "2.0",
        "id": msg.get("id"),
        "result": {
            "tools": [
                {
                    "name": "get_quota",
                    "description": (
                        "Query the current Kimi Code weekly quota, 5-hour rolling "
                        "rate limit, and Extra Usage (booster wallet) balance. "
                        "Returns used/limit/remaining percentages with visual bars."
                    ),
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                }
            ]
        }
    })
    log("tools/list → sent")


def handle_tools_call(msg):
    params = msg.get("params", {})
    name = params.get("name", "")

    if name != "get_quota":
        send({
            "jsonrpc": "2.0",
            "id": msg.get("id"),
            "error": {"code": -32601, "message": f"Unknown tool: {name}"}
        })
        return

    token, err = load_token()
    if err:
        text = f"⚠️  {err}\n\nRun `/login` or `/reload`, then try again."
        send({
            "jsonrpc": "2.0",
            "id": msg.get("id"),
            "result": {"content": [{"type": "text", "text": text}]}
        })
        return

    data, err = fetch_usage(token)
    if err:
        text = f"⚠️  Failed to fetch quota: {err}"
        send({
            "jsonrpc": "2.0",
            "id": msg.get("id"),
            "result": {"content": [{"type": "text", "text": text}]}
        })
        return

    lines = []
    usage = data.get("usage", {})
    limits = data.get("limits", [])
    wallet = data.get("boosterWallet", {})
    membership = data.get("user", {}).get("membership", {})
    parallel = data.get("parallel", {})

    # ── Membership level
    level = membership.get("level", "").replace("LEVEL_", "")
    lines.append(f"📋  Membership: {level}")
    lines.append("")

    # ── Weekly quota
    wk_limit = usage.get("limit")
    wk_used = usage.get("used")
    wk_remain = usage.get("remaining")
    wk_reset = usage.get("resetTime", "")
    if wk_limit is not None and wk_used is not None:
        pct = (int(wk_used) / int(wk_limit)) * 100 if int(wk_limit) > 0 else 0
        lines.append(f"📊  Weekly Quota:  {wk_used}/{wk_limit} used ({wk_remain} remaining)")
        lines.append(f"     {_bar(pct)}  {pct:.0f}%")
        if wk_reset:
            lines.append(f"     Resets at: {wk_reset[:19].replace('T', ' ')}")
        lines.append("")
    else:
        lines.append("📊  Weekly Quota:  (not available)")
        lines.append("")

    # ── 5-hour rolling rate limit
    lines.append("⏱  5-Hour Rolling Rate Limit:")
    if limits:
        lines.append(format_limits(limits))
        lines.append("")

    # ── Extra Usage (booster wallet)
    balance = wallet.get("balance", {})
    wallet_status = wallet.get("status", "")
    monthly_used = wallet.get("monthlyUsed", {})
    monthly_limit = wallet.get("monthlyChargeLimit", {})
    if wallet_status:
        status_label = wallet_status.replace("STATUS_", "").title()
        lines.append(f"💳  Extra Usage:  {status_label}")
        bal_cents = int(balance.get("priceInCents") or 0)
        if bal_cents > 0:
            lines.append(f"     Balance: ¥{bal_cents / 100:.2f}")
        mu_cents = int(monthly_used.get("priceInCents") or 0)
        ml_cents = int(monthly_limit.get("priceInCents") or 0)
        if ml_cents > 0:
            lines.append(
                f"     Monthly spending: ¥{mu_cents / 100:.2f} / ¥{ml_cents / 100:.2f}"
            )
        lines.append("")

    # ── Parallel requests
    pl = parallel.get("limit")
    if pl is not None:
        lines.append(f"⚡  Parallel requests:  {pl}")
        lines.append("")

    text = "\n".join(lines) or "No quota data available."
    send({
        "jsonrpc": "2.0",
        "id": msg.get("id"),
        "result": {"content": [{"type": "text", "text": text}]}
    })
    log("tools/call get_quota → sent")


def log(msg):
    """Write diagnostics to stderr so they don't pollute the MCP stream."""
    print(f"[quota_server] {msg}", file=sys.stderr, flush=True)


def main():
    log("Starting Kimi Quota MCP server")
    try:
        while True:
            msg = read_request()
            if msg is None:
                break

            method = msg.get("method", "")

            # ── Notifications (no response expected) ──
            if method.startswith("notifications/"):
                if method == "notifications/initialized":
                    log("client initialized")
                continue

            # ── Requests (require a response) ──
            if method == "initialize":
                handle_initialize(msg)
            elif method == "tools/list":
                handle_tools_list(msg)
            elif method == "tools/call":
                handle_tools_call(msg)
            elif method == "ping":
                send({"jsonrpc": "2.0", "id": msg.get("id"), "result": {}})
            else:
                log(f"Unknown method: {method}")
                send({
                    "jsonrpc": "2.0",
                    "id": msg.get("id"),
                    "error": {"code": -32601, "message": f"Method not found: {method}"}
                })
    except KeyboardInterrupt:
        pass
    finally:
        log("Shutdown")


if __name__ == "__main__":
    main()
