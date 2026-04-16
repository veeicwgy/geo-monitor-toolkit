---
name: geo-monitor-toolkit
description: >
  Use when the user wants to build or operate a GEO monitoring and content optimization loop for a developer tool, API product, SDK, or open-source project. Covers keyword matrix design, Query Pool planning, multi-model monitoring, model-specific content placement, pre-publish GEO quality checks, and negative content repair. Especially suitable for technical products that need stronger citation and recommendation performance in LLMs.
compatibility: "skills.sh, OpenClaw, ClawHub, Claude-style skill ecosystems"
metadata:
  author: Manus AI
  version: "0.1.0"
  homepage: https://github.com/veeicwgy/geo-monitor-toolkit
  tags:
    - geo
    - ai-search
    - llm-monitoring
    - open-source
    - developer-tools
    - mineru
    - query-pool
  requires:
    bins: []
---

# GEO Monitor Toolkit

Use this skill as the **workflow router** for GEO programs built around developer tools and open-source products.

## Trigger

Use this skill when the next task is any of the following:

1. design a GEO monitoring system for a technical product;
2. generate a keyword scenario matrix and Query Pool from a product description;
3. diagnose why a product is not being cited or recommended by LLMs;
4. decide where to publish content for different models;
5. classify and repair negative or incorrect model responses.

## Quick Start

If the user starts with a product description, go to `skills/geo-keyword-matrix/` first.

If the user already has a Query Pool and model outputs, go to `skills/geo-monitor/` first.

If the user has a draft article and wants pre-publish validation, go to `skills/geo-content-check/` first.

If the user has a bad answer, wrong answer, outdated answer, or competitor-only answer, go to `skills/geo-fix-negative/` first.

## Operating Contract

Read the repository in this order:

1. `playbooks/geo-workflow-architecture.md`
2. `playbooks/keyword-strategy.md`
3. `playbooks/monitoring-system.md`
4. `playbooks/model-datasources.md`
5. `playbooks/content-platform-map.md`
6. `playbooks/negative-fix-sop.md`
7. `playbooks/seo-geo-claude-skills-integration.md`

Then choose one of the four packaged skills.

## Inputs

Typical inputs include:

| Input Type | Examples |
|---|---|
| Product context | product description, positioning, target users, pricing, open-source status |
| Evidence | model responses, screenshots, answer logs, cited links |
| Entity truth | official README, docs, package pages, version notes |
| Publishing targets | target models, languages, regions, channels |

## Outputs

Typical outputs include:

| Output | Description |
|---|---|
| Keyword matrix | scenario-led keyword foundation for GEO monitoring and content planning |
| Query Pool | reusable monitoring prompts for brand, capability, ecosystem, and competitor scenes |
| Monitoring report | mention rate, sentiment, capability accuracy, ecosystem accuracy, and anomaly list |
| Placement plan | channel-by-model distribution map and publication priorities |
| Repair plan | negative-type classification, source correction actions, authority coverage plan, regression checks |

## Handoff Rules

Always preserve the following handoff summary after execution:

1. what product is being optimized;
2. which models are in scope;
3. which queries are used repeatedly;
4. what the top three weaknesses are;
5. which content or repair actions are already completed.

## Next Best Skill

| Situation | Next Skill |
|---|---|
| Need a Query Pool | `geo-keyword-matrix` |
| Need weekly metrics | `geo-monitor` |
| Need pre-publish QA | `geo-content-check` |
| Need to fix bad answers | `geo-fix-negative` |
