# Security Policy

This repository is a community plugin marketplace for **Kimi Code CLI**.
We take security seriously — please report any concerns responsibly.

---

## 🔐 Trust Model

Kimi Code CLI has a built-in trust badge system that applies to every plugin at install time:

| Badge | Meaning |
|-------|---------|
| `kimi-official` | Plugin from an official Kimi Code address |
| `curated` | Plugin from a curated/trusted address |
| `third-party` | Everything else — install requires explicit user confirmation |

Plugins from **this repository** are **not** official Kimi Code plugins. They are community-contributed and treated as **third-party** by Kimi Code. Installing a third-party plugin always shows a confirmation prompt that defaults to cancelling — you must actively choose to trust the source.

---

## 🛡️ Our Commitments

1. **Review before merge** — Every pull request that adds or modifies a plugin undergoes a basic safety review (see [Review Checklist](#review-checklist) below).
2. **No obfuscated code** — All plugin code in this repository must be readable and auditable. Minified, obfuscated, or encoded payloads are not permitted.
3. **No network calls without disclosure** — Plugins that make external network requests must declare this in their `kimi.plugin.json` metadata and in the PR description.
4. **Transparency** — Plugin source is always visible in the repo. If a plugin requires external binaries, the source or a verifiable build process must be provided.

---

## ✅ Plugin Review Checklist

When a new plugin or update is submitted, we check for:

- [ ] Manifest (`kimi.plugin.json`) is valid JSON and all fields are correctly formatted
- [ ] All file paths in the manifest point within the plugin's own directory
- [ ] No obfuscated, minified, or otherwise unreadable code
- [ ] No shell scripts or commands that fetch and execute remote content
- [ ] MCP server URLs point to reputable/known services, or are clearly documented
- [ ] Hooks do not execute dangerous commands without clear justification
- [ ] Plugin does not attempt to read or exfiltrate sensitive files (`.env`, SSH keys, credentials, etc.)
- [ ] `skillInstructions` and `SKILL.md` content does not contain prompt injection or social engineering

---

## 📋 Reporting a Security Issue

If you find a **malicious plugin** in this repository, or a security vulnerability in the marketplace infrastructure itself:

**Do not open a public issue.** Instead:

1. **Email the maintainer** — [your-email@example.com](mailto:your-email@example.com)
2. Include:
   - The affected plugin name and path
   - A clear description of the issue
   - Steps to reproduce
   - Any evidence (screenshots, logs)

We will acknowledge within **48 hours** and work on a fix. Once resolved, we'll publish a security advisory and credit the reporter (if desired).

---

## ⚠️ Disclaimer

**This is a community marketplace.** Plugins are contributed by third-party developers and are **not audited or endorsed** by Moonshot AI / Kimi Code. You install them at your own risk.

Always review a plugin's source before installing. When in doubt, install plugins from the **Official** tab in Kimi Code's plugin manager instead.

---

## 🔒 Plugin Sandboxing

Kimi Code CLI provides these built-in security boundaries:

- All plugin file paths must resolve **within the plugin root directory** — symbolic links are followed and enforced
- Plugin MCP servers can be **disabled individually** from `/plugins mcp disable <id> <server>`
- Hooks only run while the plugin is **enabled** — disabling the plugin stops all its hooks
- Broken manifests or unsafe paths are shown as **diagnostics** and do not affect other sessions
- Installing a plugin **never runs its hooks automatically** — they only fire on matching events after `/reload`

For full details, see the [official security model documentation](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html#security-model).
