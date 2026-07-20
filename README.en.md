[中文](./README.md) · **[English](./README.en.md)**

---

# 🧩 Kimi Plugin Market

**Kimi Code Community Plugin Marketplace** — Host & share Kimi Code plugins

![License](https://img.shields.io/badge/license-MIT-yellow)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Plugins](https://img.shields.io/badge/plugins-4-brightgreen)
![Kimi Code](https://img.shields.io/badge/Kimi%20Code-compatible-8A2BE2)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange)](./CONTRIBUTING.md)

---

## 🚀 Quick Start

Load this marketplace in Kimi Code:

```bash
/plugins marketplace https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market/-/raw/main/marketplace.json
```

Set as default:

```bash
export KIMI_CODE_PLUGIN_MARKETPLACE_URL=https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market/-/raw/main/marketplace.json
```

### 📦 Available Plugins

| Plugin | Description |
|--------|-------------|
| 🆕 **Hello World** | Minimal demo plugin — starting point for learning |
| 🔍 **Code Reviewer** | Lightweight code review assistant with session-start guidelines |
| ✍️ **Commit Writer** | Generates conventional commit messages from staged changes |
| 🔊 **Completion Sound** | Plays a configurable sound when the assistant finishes a response |

---

## 📁 Repository Structure

```
kimi-plugin-market/
├── marketplace.json               # Marketplace catalog (version 2)
├── kimi.plugin.json               # Root plugin manifest
├── skills/hello/SKILL.md          # Example skill
├── plugins/
│   ├── hello-world/               # Demo plugin
│   ├── code-reviewer/             # Code review assistant
│   ├── commit-writer/             # Commit message generator
│   └── completion-sound/          # Completion sound
├── SECURITY.md                    # Security policy
├── CONTRIBUTING.md                # Contributing guide
└── README.md                      # This file
```

---

## ➕ Adding Your Plugin

1. Create `plugins/<name>/` with a `kimi.plugin.json`
2. Register `id`, `displayName`, `source` in `marketplace.json`
3. Submit a PR

See [CONTRIBUTING.md](./CONTRIBUTING.md) for format specs.

---

## 🔒 Security

Community plugins are third-party software, not reviewed by Moonshot AI / Kimi Code. Before installing:

- Review the plugin source
- Check declared MCP servers and hooks
- Disable untrusted MCP servers via `/plugins mcp disable <id> <server>`

See **[SECURITY.md](./SECURITY.md)**

---

## 📄 License

[MIT](./LICENSE)
