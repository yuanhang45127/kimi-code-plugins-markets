# Contributing Guide

Thanks for your interest in contributing to the Kimi Plugin Template & Marketplace!

---

## Adding a Plugin

1. Fork the repository
2. Create a directory under `plugins/<your-plugin>/`
3. Add your plugin following the format described in the [README](./README.md)
4. Register it in `marketplace.json`
5. Submit a Pull Request

## Plugin Submission Requirements

Every plugin submission must:

- [ ] Have a valid `kimi.plugin.json` manifest
- [ ] Have all file paths within the plugin's own directory
- [ ] Not contain obfuscated, minified, or encoded code
- [ ] Declare any external network calls or MCP servers in the PR description
- [ ] Not attempt to read sensitive files (`.env`, SSH keys, credentials, etc.)
- [ ] Be written in readable, auditable Markdown / JSON — no binary blobs
- [ ] Include a clear description of what the plugin does

## Code of Conduct

- Be respectful and constructive
- Focus on technical merit and safety
- Do not submit plugins with hidden or undocumented behavior

## Security

If you find a security issue, **do not open a public issue**. Follow the process in [SECURITY.md](./SECURITY.md).
