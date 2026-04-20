![GEO Monitor Toolkit](assets/logo.png)

# GEO Monitor Toolkit

> 监控 ChatGPT、Claude、Gemini 等大模型如何描述你的 developer tool、API、SDK 或 open-source 项目。

[![CI](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml)

**GEO Monitor Toolkit** 是一个面向 **developer tools、API、SDK 与 open-source 项目** 的 **GEO Monitoring OS**。
它不是通用内容生成器，而是一套把 **Query Pool 设计、答案监控、四指标打分、repair loop 与 T+7/T+14 回归验证** 串起来的可复现工作流。

For English, see [`README.md`](README.md).

## 为什么需要这个仓库

如果你的团队已经开始关注“LLM 会不会提到我、会不会说错我、修完后会不会变好”，这个仓库的目标就是把这条链路变成可执行、可复盘、可对比的流程。

| 你要回答的问题 | 这个仓库提供的能力 |
|---|---|
| 模型有没有提到你的产品 | Query Pool + raw responses |
| 提到时是否准确、是否正向 | 四指标打分框架 |
| 应该去哪里修复信息源 | placement / repair 视角 |
| 修复动作是否真的改善了模型回答 | T+7 / T+14 回归验证 |

## 30 秒开始路径

第一次使用，按这个顺序即可。

```bash
git clone https://github.com/veeicwgy/geo-monitor-toolkit.git
cd geo-monitor-toolkit
bash install.sh
make doctor
bash quickstart.sh
```

## 第一次会先看到什么

第一次跑完后，优先看下面四个输出。

| 输出 | 路径 | 为什么重要 |
|---|---|---|
| 原始回答 | `data/runs/quickstart-run/raw_responses.jsonl` | 查看多模型原始回答证据 |
| 打分草稿 | `data/runs/quickstart-run/score_draft.jsonl` | 进入人工复核与补标流程 |
| 周报快照 | `data/runs/sample-run/weekly_report.md` | 直接理解团队可消费的周报形态 |
| 排行榜快照 | `assets/leaderboard-sample.png` | 快速理解默认多模型对比 |

> `quickstart.sh` 会生成一份新的 `quickstart-run` 原始证据，同时重放仓库内置的样例摘要来生成周报与图表快照。因此首轮体验既能看到“新 run 长什么样”，也能直接看到“成熟输出长什么样”。

## 新手优先文档

如果你是第一次接触 GEO 监控，请先读这两个入口。

| 文档 | 用途 |
|---|---|
| `docs/for-beginners.md` | 5 分钟上手版，先跑通、先看结果 |
| `docs/getting-started.md` | 长版入门，解释输出、模式和团队使用方式 |

## 应该选哪种模式

| 你的状态 | 推荐模式 | 入口 |
|---|---|---|
| 没有 API key，只想先看整个流程 | Quickstart replay | `bash quickstart.sh` |
| 已经从外部聊天产品拿到回答，想导入评估 | Manual paste mode | `python -m geo_monitor run --manual-responses ...` |
| 想做真实、持续、多模型 GEO 监控 | API collection mode | `python -m geo_monitor run --query-pool ... --model-config ...` |

## 核心命令

| 命令 | 作用 |
|---|---|
| `bash install.sh` | 创建 `.venv` 并安装依赖 |
| `make doctor` | 检查 Python、依赖、样例文件与输出目录是否可用 |
| `bash quickstart.sh` | 运行零 API 成本的新手演示 |
| `make sample-report` | 重建样例报告与图表 |
| `python -m geo_monitor run ...` | 运行自定义 Query Pool 监控 |

## 默认样例输入

| 文件 | 作用 |
|---|---|
| `data/query-pools/mineru-example.json` | 默认 Query Pool 示例 |
| `data/models.sample.json` | 最小单模型配置 |
| `data/models.multi.sample.json` | 默认多模型配置 |
| `data/manual.sample.json` | 最小手工回答样例 |
| `data/manual.multi.sample.json` | 多模型手工回答样例 |

## 仓库定位

请把它理解为：

> **GEO Monitoring OS for Developer Tools**
>
> 它关注的是 **monitoring、scoring、repair 与 regression**，而不是泛化营销文案生成。

## 继续阅读

| 主题 | 路径 |
|---|---|
| 5 分钟上手 | `docs/for-beginners.md` |
| 长版入门 | `docs/getting-started.md` |
| English README | `README.md` |
| Skill 包 | `SKILL.md` 或 `skills/geo-monitor-toolkit/SKILL.md` |
