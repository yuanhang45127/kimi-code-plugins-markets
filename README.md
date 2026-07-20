<!-- 语言切换 / Language Switch -->
[**中文**](./README.md) | [English](./README.en.md)

---

# Kimi Plugin Template & Marketplace

**Kimi Code 插件市场仓库** — 托管社区贡献的插件，并提供开发模板供参考。

浏览 [Kimi Code 官方文档](https://www.kimi.com/code/docs/en/) 了解平台详情。

---

## 快速开始：使用市场

本仓库同时也是一个插件市场，让 Kimi Code 可以浏览和安装插件：

```bash
# 在 Kimi Code TUI 中
/plugins marketplace https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

或设置环境变量使其成为默认市场：

```bash
export KIMI_CODE_PLUGIN_MARKETPLACE_URL=https://codeup.aliyun.com/64e63304dba61e96ebf62138/kimi-plugin-market.git/raw/main/marketplace.json
```

> 如果发布到 GitHub，将 URL 替换为 `marketplace.json` 的 raw 地址。

### 可用插件

| 插件 | 说明 |
|------|------|
| **Hello World** | 最简示例插件 — 学习插件开发的起点 |
| **Code Reviewer** | 轻量代码审查助手，含 session-start 指南 |
| **Commit Writer** | 根据暂存变更自动生成 conventional commit 消息 |

---

## 仓库结构

```
kimi-plugin-market/
├── marketplace.json              # 市场目录（version 2）
├── kimi.plugin.json              # 根插件 manifest（可选）
├── skills/
│   └── hello/
│       └── SKILL.md              # 根插件的示例 skill
├── plugins/                      # 所有市场插件
│   ├── hello-world/
│   │   ├── kimi.plugin.json      # 插件清单
│   │   └── skills/greet/SKILL.md
│   ├── code-reviewer/
│   │   ├── kimi.plugin.json
│   │   └── skills/review-guidelines/SKILL.md
│   └── commit-writer/
│       ├── kimi.plugin.json
│       ├── skills/write-commit/SKILL.md
│       └── commands/write.md     # 斜杠命令 (/commit-writer:write)
├── SECURITY.md                   # 安全策略
├── CONTRIBUTING.md               # 贡献指南
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md  # PR 模板
└── README.md
```

---

## Marketplace 格式

`marketplace.json` 遵循官方 Kimi Code 规范：

```json
{
  "version": "2",
  "plugins": [
    {
      "id": "my-plugin",
      "displayName": "我的插件",
      "shortDescription": "插件的作用",
      "source": "./plugins/my-plugin"
    }
  ]
}
```

| 字段 | 说明 |
|------|------|
| `version` | 必须为 `"2"` |
| `plugins` | 插件条目数组 |
| `id` | 唯一标识（需匹配 `kimi.plugin.json` 中的 `name`）|
| `displayName` | 插件管理器中显示的名称 |
| `shortDescription` | 列表中的简短描述 |
| `source` | 插件目录的相对路径或 URL |

### Source 支持的类型

- **相对路径**：`"./plugins/my-plugin"` — 本地开发用
- **GitHub URL**：`"https://github.com/owner/repo"`
- **分支/标签 URL**：`"https://github.com/owner/repo/tree/branch-name"`
- **Zip URL**：`"https://example.com/plugin.zip"`

---

## 插件清单 (`kimi.plugin.json`)

每个插件目录下都需要一个 `kimi.plugin.json`：

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "插件功能描述",
  "keywords": ["keyword1", "keyword2"],
  "author": "作者名",
  "homepage": "https://github.com/yourname/my-plugin",
  "skills": "./skills",
  "commands": "./commands",
  "sessionStart": {
    "skill": "my-skill-name"
  },
  "skillInstructions": "每次加载此插件的 skill 时附加的额外指令。",
  "interface": {
    "displayName": "我的插件",
    "shortDescription": "简短描述",
    "longDescription": "插件详情中显示的完整描述",
    "developerName": "作者名",
    "websiteURL": "https://github.com/yourname/my-plugin"
  }
}
```

关键限制：
- `name` 必须匹配 `[a-z0-9][a-z0-9_-]{0,63}`
- `skills` 和 `commands` 路径必须在插件根目录内
- 清单也可放在 `.kimi-plugin/plugin.json`

---

## 添加你自己的插件

1. 在 `plugins/<你的插件>/` 下创建目录
2. 添加 `kimi.plugin.json` 清单
3. 在 `skills/<skill-name>/SKILL.md` 添加技能
4. 可选：在 `commands/<name>.md` 添加斜杠命令
5. 在 `marketplace.json` 中注册：

   ```json
   {
     "id": "your-plugin",
     "displayName": "你的插件",
     "shortDescription": "它做什么",
     "source": "./plugins/your-plugin"
   }
   ```

6. 提交 PR（如果你是维护者，可直接 push）。

---

## 安全

> **⚠️ 社区插件是第三方软件，未经 Moonshot AI / Kimi Code 审核或认可。**

本仓库实施以下基本安全措施：

- **PR 审查清单** — 每个新插件会检查混淆代码、不安全路径、可疑网络调用和 prompt 注入
- **Kimi Code 内置沙箱** — 插件路径被限制在插件根目录内；hook 仅在插件启用时运行
- **信任徽章** — Kimi Code 将此仓库的插件标记为 `third-party`，安装需要用户明确确认

完整的安全策略和报告流程请参见 **[SECURITY.md](./SECURITY.md)**。

安装前建议：
- 审查插件源码
- 检查它声明了哪些 MCP 服务或 hook
- 通过 `/plugins mcp disable <id> <server>` 禁用不信任的 MCP 服务

---

## 本地开发

```bash
# 从本地路径安装插件
/plugins install ./plugins/hello-world
/reload

# 浏览本地市场
/plugins marketplace ./marketplace.json
```

---

## 开源协议

本项目基于 MIT 协议开源 — 详见 [LICENSE](LICENSE) 文件。
