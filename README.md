# Kimi Plugin Template

A minimal template for building [Kimi Code](https://www.kimi.com/) plugins.

## Structure

```
kimi-plugin-template/
├── kimi.plugin.json      # Plugin manifest (name, version, skills path, hooks)
├── skills/
│   └── hello/
│       └── SKILL.md      # Example skill
└── README.md
```

## Installation

From the Kimi Code TUI:

```
/plugins install <path-or-git-url>
/reload
```

Or from the command line:

```bash
kimi plugins install <path-or-git-url>
```

Then start a new session or run `/reload`.

## Developing your plugin

1. Edit `kimi.plugin.json` — set your plugin's `name`, `version`, and `description`.
2. Add skills under `skills/<skill-name>/SKILL.md`. Each skill is a Markdown file
   with YAML frontmatter (`name`, `description`) plus instructions in the body.
3. Optionally register lifecycle `hooks` in `kimi.plugin.json`, e.g.:

```json
"hooks": [
  {
    "event": "Stop",
    "command": "node ./hooks/my-hook.mjs",
    "timeout": 5
  }
]
```

4. Install locally and iterate.
