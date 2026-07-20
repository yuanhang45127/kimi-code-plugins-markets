# Kimi Plugin Template & Marketplace

A **Kimi Code plugin marketplace** repository — hosts community-contributed plugins and provides a reusable template for building new ones.

Browse the [official Kimi Code docs](https://www.kimi.com/code/docs/en/) for more about the platform.

---

## Quick Start: Using the Marketplace

This repository doubles as a plugin marketplace. Point Kimi Code at it to browse and install available plugins:

```bash
# From the Kimi Code TUI
/plugins marketplace https://raw.githubusercontent.com/yuanhang45127/kimi-plugin-template/main/marketplace.json
```

Or set the environment variable to make it the default:

```bash
export KIMI_CODE_PLUGIN_MARKETPLACE_URL=https://raw.githubusercontent.com/yuanhang45127/kimi-plugin-template/main/marketplace.json
```

> Once published to GitHub, replace the URL with the raw GitHub link to `marketplace.json`.

### Available Plugins

| Plugin | Description |
|--------|-------------|
| **Hello World** | Minimal demo plugin — great starting point for learning |
| **Code Reviewer** | Lightweight code review assistant with session-start guidelines |
| **Commit Writer** | Generates conventional commit messages from staged changes |

---

## Repository Structure

```
kimi-plugin-template/
├── marketplace.json              # Marketplace catalog (version 2)
├── kimi.plugin.json              # Root plugin manifest (optional — for this repo itself)
├── skills/
│   └── hello/
│       └── SKILL.md              # Example skill for the root plugin
├── plugins/                      # All marketplace plugins live here
│   ├── hello-world/
│   │   ├── kimi.plugin.json      # Plugin manifest
│   │   └── skills/
│   │       └── greet/
│   │           └── SKILL.md      # Skill definition
│   ├── code-reviewer/
│   │   ├── kimi.plugin.json
│   │   └── skills/
│   │       └── review-guidelines/
│   │           └── SKILL.md
│   └── commit-writer/
│       ├── kimi.plugin.json
│       ├── skills/
│       │   └── write-commit/
│       │       └── SKILL.md
│       └── commands/
│           └── write.md          # Slash command (/commit-writer:write)
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
- **GitHub URL**: `"https://github.com/owner/repo"` — installs from a release or default branch
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
