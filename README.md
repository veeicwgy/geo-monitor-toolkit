![GEO Monitor Toolkit](assets/logo.png)

# GEO Monitor Toolkit

**GEO Monitor Toolkit** 是一个面向 **developer tools、API、SDK 与 open-source 项目** 的 **GEO Monitoring OS**。它不是通用内容生成器，而是一套把 **Query Pool、answer monitoring、四指标打分、repair loop 与 T+7/T+14 回归验证** 串起来的可复现工作流。

## Why this repository exists

如果你的团队已经开始关注“LLM 会不会提到我、会不会说错我、修完后会不会变好”，这个仓库的目标就是把这条链路变成可执行、可复盘、可对比的流程。

| 你要解决的问题 | 这个仓库给你的东西 |
|---|---|
| 想知道模型有没有提到你的产品 | Query Pool + raw responses |
| 想判断提到得对不对、正不正向 | 四指标打分框架 |
| 想知道应该去哪里修复信息源 | placement / repair 视角 |
| 想验证修复动作是否真的有效 | T+7 / T+14 回归验证 |

## 30-second path

第一次使用，按这个顺序即可。

```bash
git clone https://github.com/veeicwgy/geo-monitor-toolkit.git
cd geo-monitor-toolkit
bash install.sh
make doctor
bash quickstart.sh
```

## What you will get first

第一次跑完后，优先看下面 4 个输出。

| Output | Path | Why it matters |
|---|---|---|
| Raw responses | `data/runs/quickstart-run/raw_responses.jsonl` | 查看多模型原始回答证据 |
| Score draft | `data/runs/quickstart-run/score_draft.jsonl` | 后续人工复核与补标入口 |
| Weekly report snapshot | `data/runs/sample-run/weekly_report.md` | 查看团队可消费的周报样式 |
| Leaderboard snapshot | `assets/leaderboard-sample.png` | 快速理解默认多模型对比 |

> `quickstart.sh` 会生成一份新的 `quickstart-run` 原始证据，同时重放仓库内置的样例摘要来生成周报与图表快照。因此首轮体验既能看到“新 run 长什么样”，也能直接看到“成熟输出长什么样”。

## Beginner-first docs

如果你是第一次接触 GEO 监控，请先读这两个入口。

| 文档 | 用途 |
|---|---|
| `docs/for-beginners.md` | 5 分钟上手版，先跑通、先看结果 |
| `docs/getting-started.md` | 长版入门，解释输出、模式和团队使用方式 |

## Which mode should you choose

| 你的状态 | 推荐模式 | 入口 |
|---|---|---|
| 没有 API key，只想先看整个流程 | Quickstart replay | `bash quickstart.sh` |
| 已经从外部聊天产品拿到回答，想导入评估 | Manual paste mode | `python -m geo_monitor run --manual-responses ...` |
| 想做真实、持续、多模型 GEO 监控 | API collection mode | `python -m geo_monitor run --query-pool ... --model-config ...` |

## Core commands

| Command | What it does |
|---|---|
| `bash install.sh` | 创建 `.venv` 并安装依赖 |
| `make doctor` | 检查 Python、依赖、样例文件与输出目录是否可用 |
| `bash quickstart.sh` | 运行零 API 成本的新手演示 |
| `make sample-report` | 重建样例报告与图表 |
| `python -m geo_monitor run ...` | 运行自定义 Query Pool 监控 |

## Default sample inputs

| File | Purpose |
|---|---|
| `data/query-pools/mineru-example.json` | 默认 Query Pool 示例 |
| `data/models.sample.json` | 最小单模型配置 |
| `data/models.multi.sample.json` | 默认多模型配置 |
| `data/manual.sample.json` | 最小手工回答样例 |
| `data/manual.multi.sample.json` | 多模型手工回答样例 |

## Repository positioning

请把它理解为：

> **GEO Monitoring OS for Developer Tools**
>
> 它关注的是 **monitoring、scoring、repair 与 regression**，而不是泛化营销文案生成。

## Read next

| Topic | Path |
|---|---|
| 5-minute path | `docs/for-beginners.md` |
| Long-form onboarding | `docs/getting-started.md` |
| Skill package | `SKILL.md` or `skills/geo-monitor-toolkit/SKILL.md` |
