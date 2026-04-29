# Sec_search

每日自动更新的**网络安全项目库雷达**，涵盖最近 7 天内有推送的 GitHub 仓库，按四大类分组展示。

## 📋 最新报告

👉 [LATEST_SECURITY_REPOS.md](./LATEST_SECURITY_REPOS.md)

## 🗂️ 覆盖类别

| 分类 | 关键词示例 |
|------|-----------|
| 🔴 网络安全渗透 / 红队 | penetration, pentest, 渗透测试, red team, 红队 |
| 🛠️ 网络安全工具 | security tool, scanner, recon, 信息收集, exploit |
| 🤖 大模型安全 | LLM security, 大模型安全, prompt injection, guardrails |
| 🔓 大模型越狱 | jailbreak, 越狱, prompt hacking, 提示越狱 |

## ⚙️ 自动化说明

- **定时运行**：每天 UTC 00:00（北京时间 08:00）由 GitHub Actions 自动运行
- **手动触发**：在 [Actions 页面](../../actions/workflows/security-radar.yml) 点击 **Run workflow**
- **结果更新**：若报告有变化，workflow 会自动 commit 并 push 到默认分支

## 🚀 本地手动运行

```bash
# 安装依赖
pip install requests

# 设置 GitHub Token（可选，但推荐，可提高 API 速率限制）
export GITHUB_TOKEN=your_personal_access_token

# 设置每类展示数量（可选，默认 30）
export TOP_N=30

# 运行脚本
python scripts/security_radar.py
```

运行后报告输出到仓库根目录的 `LATEST_SECURITY_REPOS.md`。

## 📁 文件结构

```
.
├── .github/
│   └── workflows/
│       └── security-radar.yml   # GitHub Actions workflow
├── scripts/
│   └── security_radar.py        # 数据采集与报告生成脚本
├── LATEST_SECURITY_REPOS.md     # 每日自动更新的报告
└── README.md
```
