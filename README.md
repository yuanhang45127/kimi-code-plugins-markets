**[中文](./README.md)** · [English](./README.en.md)

---

# Kimi Plugin Market

Kimi Code 社区插件市场 — 托管 & 分享 Kimi Code 插件

`3 个插件` · `MIT 协议` · `欢迎 PR` · `Kimi Code 兼容`

---

## 快速开始

在 Kimi Code 中加载本市场，浏览和安装插件：

```bash
/plugins marketplace https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

设为默认市场：

```bash
export KIMI_CODE_PLUGIN_MARKETPLACE_URL=https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

### 可用插件

| 插件 | 说明 |
|------|------|
| **Hello World** | 最简示例插件，学习插件开发的起点 |
| **Code Reviewer** | 轻量代码审查助手，含 session-start 指南 |
| **Commit Writer** | 根据暂存变更自动生成 conventional commit 消息 |

---

## 仓库结构

```
kimi-plugin-market/
├── marketplace.json           # 市场目录（version 2）
├── kimi.plugin.json           # 根插件 manifest
├── skills/hello/SKILL.md      # 示例 skill
├── plugins/
│   ├── hello-world/           # 最简示例插件
│   ├── code-reviewer/         # 代码审查助手
│   └── commit-writer/         # commit 消息生成器
├── SECURITY.md                # 安全策略
├── CONTRIBUTING.md            # 贡献指南
└── README.md                  # 本文件
```

---

## 添加你的插件

1. 在 `plugins/<name>/` 下创建目录，添加 `kimi.plugin.json`
2. 在 `marketplace.json` 中注册 `id`、`displayName`、`source`
3. 提交 PR

详细格式规范见 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 安全

社区插件属于第三方软件，未经 Moonshot AI / Kimi Code 审核。安装前请：

- 审查插件源码
- 检查声明的 MCP 服务和 hook
- 通过 `/plugins mcp disable <id> <server>` 禁用不信任的 MCP 服务

详见 **[SECURITY.md](./SECURITY.md)**

---

## 开源协议

[MIT](./LICENSE)
