<!-- Language Switch / 语言切换 -->
[中文](./README.md) | [**English**](./README.en.md)

---

# Kimi Plugin Template & Marketplace

A **Kimi Code plugin marketplace** repository — hosts community-contributed plugins and provides a reusable template for building new ones.

Browse the [official Kimi Code docs](https://www.kimi.com/code/docs/en/) for more about the platform.

---

## Quick Start: Using the Marketplace

This repository doubles as a plugin marketplace. Point Kimi Code at it to browse and install available plugins:

```bash
# From the Kimi Code TUI
/plugins marketplace https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

Or set the environment variable to make it the default:

```bash
export KIMI_CODE_PLUGIN_MARKETPLACE_URL=https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

> If published to GitHub, replace the URL with the raw link to `marketplace.json`.

### Available Plugins

| Plugin | Description |
|--------|-------------|
| **Hello World** | Minimal demo plugin — great starting point for learning |
| **Code Reviewer** | Lightweight code review assistant with session-start guidelines |
| **Commit Writer** | Generates conventional commit messages from staged changes |

---

## Repository Structure

```
kimi-plugin-market/
├── marketplace.json              # Marketplace catalog (version 2)
├── kimi.plugin.json              # Root plugin manifest (optional)
├── skills/
│   └── hello/
│       └── SKILL.md              # Example skill for the root plugin
├── plugins/                      # All marketplace plugins live here
│   ├── hello-world/
│   │   ├── kimi.plugin.json      # Plugin manifest
│   │   └── skills/greet/SKILL.md
│   ├── code-reviewer/
│   │   ├── kimi.plugin.json
│   │   └── skills/review-guidelines/SKILL.md
│   └── commit-writer/
│       ├── kimi.plugin.json
│       ├── skills/write-commit/SKILL.md
│       └── commands/write.md     # Slash command (/commit-writer:write)
├── SECURITY.md                   # Security policy
├── CONTRIBUTING.md               # Contributing guide
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md  # PR template
└── README.md
```

---

## Marketplace Format

The `marketplace.json` follows the official Kimi Code schema:

```json
{
  "version": "2",
  "plugins": [
    {
      "id": "my-plugin",
      "displayName": "My Plugin",
      "shortDescription": "What this plugin does",
      "source": "./plugins/my-plugin"
    }
  ]
}
```

| Field | Description |
|-------|-------------|
| `version` | Must be `"2"` |
| `plugins` | Array of plugin entries |
| `id` | Unique plugin identifier (matches `name` in `kimi.plugin.json`) |
| `displayName` | Human-readable name shown in the plugin manager |
| `shortDescription` | Brief description shown in listings |
| `source` | Path (relative to `marketplace.json`) or URL to the plugin directory |

### Source Options

The `source` field supports:

- **Relative path**: `"./plugins/my-plugin"` — for local development
- **GitHub URL**: `"https://github.com/owner/repo"`
- **Branch/tag URL**: `"https://github.com/owner/repo/tree/branch-name"`
- **Zip URL**: `"https://example.com/plugin.zip"`

---

## Plugin Manifest (`kimi.plugin.json`)

Each plugin is a directory with a `kimi.plugin.json` manifest:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "What this plugin does",
  "keywords": ["keyword1", "keyword2"],
  "author": "Your Name",
  "homepage": "https://github.com/yourname/my-plugin",
  "skills": "./skills",
  "commands": "./commands",
  "sessionStart": {
    "skill": "my-skill-name"
  },
  "skillInstructions": "Additional instructions appended whenever a skill from this plugin is loaded.",
  "interface": {
    "displayName": "My Plugin",
    "shortDescription": "Brief description",
    "longDescription": "Full description shown in plugin details",
    "developerName": "Your Name",
    "websiteURL": "https://github.com/yourname/my-plugin"
  }
}
```

Key restrictions:
- `name` must match `[a-z0-9][a-z0-9_-]{0,63}`
- `skills` and `commands` paths must be inside the plugin root
- The manifest can also be placed at `.kimi-plugin/plugin.json`

---

## Adding Your Own Plugin

1. Create a directory under `plugins/<your-plugin>/`
2. Add a `kimi.plugin.json` manifest
3. Add skills under `skills/<skill-name>/SKILL.md`
4. Optionally add commands under `commands/<name>.md`
5. Register it in `marketplace.json`:

   ```json
   {
     "id": "your-plugin",
     "displayName": "Your Plugin",
     "shortDescription": "What it does",
     "source": "./plugins/your-plugin"
   }
   ```

6. Submit a PR (or push directly if you're the maintainer).

---

## Security

> **⚠️ Community plugins are third-party software.** They are not reviewed or endorsed by Moonshot AI / Kimi Code.

This repository implements basic safety measures to reduce risk:

- **PR review checklist** — Every new plugin is reviewed for obfuscated code, unsafe paths, suspicious network calls, and prompt injection
- **Kimi Code's built-in sandbox** — Plugin paths are confined to the plugin root directory; hooks only run when the plugin is enabled
- **Trust badges** — Kimi Code labels plugins from this repo as `third-party`, which requires explicit user confirmation to install

For the full security policy, reporting process, and review checklist, see **[SECURITY.md](./SECURITY.md)**.

Before installing any community plugin, consider:
- Review the plugin's source files in this repo
- Check what MCP servers or hooks it declares
- Disable MCP servers you don't trust via `/plugins mcp disable <id> <server>`

---

## Local Development

```bash
# Install a plugin from a local path
/plugins install ./plugins/hello-world
/reload

# Or browse the marketplace locally
/plugins marketplace ./marketplace.json
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
