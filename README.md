![GEO Monitor Toolkit](assets/logo.png)

# GEO Monitor Toolkit

> Monitor how ChatGPT, Claude, Gemini, and other LLMs describe your developer tool, API, SDK, or open-source project.

[![CI](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml)

**GEO Monitor Toolkit** is a **GEO Monitoring OS for developer tools, APIs, SDKs, and open-source projects**.
It is not a generic content generator. It is a reproducible workflow that connects **Query Pool design, answer monitoring, four-metric scoring, repair loops, and T+7/T+14 regression checks**.

For 中文说明, see [`README.zh-CN.md`](README.zh-CN.md).

## Why this repository exists

If your team is already asking whether LLMs mention your product, describe it correctly, or improve after documentation fixes, this repository turns that concern into an executable and reviewable workflow.

| What you need to answer | What this repository gives you |
|---|---|
| Do models mention our product at all? | Query Pool + raw responses |
| When they mention us, is it accurate and positive? | Four-metric scoring framework |
| Where should we repair the source of truth? | Placement and repair lens |
| Did our fixes actually improve model answers? | T+7 / T+14 regression checks |

## 30-second path

For a first run, follow this exact order.

```bash
git clone https://github.com/veeicwgy/geo-monitor-toolkit.git
cd geo-monitor-toolkit
bash install.sh
make doctor
bash quickstart.sh
```

## What you will get first

After the first run, start with these four outputs.

| Output | Path | Why it matters |
|---|---|---|
| Raw responses | `data/runs/quickstart-run/raw_responses.jsonl` | Review multi-model answer evidence |
| Score draft | `data/runs/quickstart-run/score_draft.jsonl` | Start manual review and annotation |
| Weekly report snapshot | `data/runs/sample-run/weekly_report.md` | See the report format a team can consume |
| Leaderboard snapshot | `assets/leaderboard-sample.png` | Understand the default multi-model comparison |

> `quickstart.sh` creates a fresh `quickstart-run` with raw evidence, then replays built-in sample summaries to generate report and chart snapshots. Your first run therefore shows both what a new run looks like and what a mature output package looks like.

## Beginner-first docs

If you are new to GEO monitoring, start with these two entry points.

| Document | Purpose |
|---|---|
| `docs/for-beginners.md` | 5-minute path: run it once and read the outputs |
| `docs/getting-started.md` | Long-form onboarding with modes, outputs, and team usage |

## Which mode should you choose

| Your situation | Recommended mode | Entry point |
|---|---|---|
| No API key yet and you only want to see the full workflow | Quickstart replay | `bash quickstart.sh` |
| You already copied answers from external chat products and want to score them | Manual paste mode | `python -m geo_monitor run --manual-responses ...` |
| You want real, repeatable, multi-model GEO monitoring | API collection mode | `python -m geo_monitor run --query-pool ... --model-config ...` |

## Core commands

| Command | What it does |
|---|---|
| `bash install.sh` | Creates `.venv` and installs dependencies |
| `make doctor` | Checks Python, dependencies, sample files, and output directories |
| `bash quickstart.sh` | Runs the zero-API-cost beginner demo |
| `make sample-report` | Rebuilds sample reports and chart assets |
| `python -m geo_monitor run ...` | Runs custom Query Pool monitoring |

## Default sample inputs

| File | Purpose |
|---|---|
| `data/query-pools/mineru-example.json` | Default Query Pool sample |
| `data/models.sample.json` | Minimal single-model config |
| `data/models.multi.sample.json` | Default multi-model config |
| `data/manual.sample.json` | Minimal manual-response sample |
| `data/manual.multi.sample.json` | Multi-model manual-response sample |

## Repository positioning

Think of this repository as:

> **GEO Monitoring OS for Developer Tools**
>
> It focuses on **monitoring, scoring, repair, and regression**, not on generic marketing copy generation.

## Read next

| Topic | Path |
|---|---|
| 5-minute path | `docs/for-beginners.md` |
| Long-form onboarding | `docs/getting-started.md` |
| Chinese README | `README.zh-CN.md` |
| Skill package | `SKILL.md` or `skills/geo-monitor-toolkit/SKILL.md` |
