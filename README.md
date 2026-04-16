# GEO Monitor Toolkit

**GEO Monitor Toolkit** 是一套面向 **开发者工具与开源项目** 的 GEO（Generative Engine Optimization）监控与内容优化闭环框架。它把 `关键词研究 → Query Pool → 多模型监控 → 内容铺设 → 发布前质检 → 负向修复 → 回归监控` 串成一条可复用工作流，并以 **MinerU** 作为完整参考案例。

与通用 SEO/GEO 工具不同，这个项目更强调 **技术产品的实体认知、开源信源建设、模型差异化内容铺设，以及负向内容的系统修复**。其结构设计参考了 backlog-first GEO 工作流与可安装 Skill 仓库的实践模式，兼顾文档、示例、技能与发布兼容性。[1] [2] [3]

## Why This Repository

| 维度 | 通用 SEO/GEO 技能库 | 本项目的聚焦点 |
|---|---|---|
| 主要对象 | 品牌、内容站、营销团队 | 开发者工具、API、SDK、开源项目 |
| 工作流重心 | 写作与优化 | 监控、铺设、质检、修复闭环 |
| 典型信源 | 通用内容站、媒体、SERP | GitHub、PyPI、pkg.go.dev、HuggingFace、知乎、头条、阿里云社区 |
| 输出形态 | 单篇内容或通用技能 | Query Pool、周报模板、渠道地图、负向修复 SOP、技能包 |
| 参考案例 | 泛行业 | MinerU |

## Quick Start

如果你希望整库安装并直接复用工作流，可以使用：

```bash
npx skills add veeicwgy/geo-monitor-toolkit
```

如果你只希望安装某一个技能，可以使用：

```bash
npx skills add veeicwgy/geo-monitor-toolkit -s geo-monitor
npx skills add veeicwgy/geo-monitor-toolkit -s geo-content-check
npx skills add veeicwgy/geo-monitor-toolkit -s geo-fix-negative
npx skills add veeicwgy/geo-monitor-toolkit -s geo-keyword-matrix
```

如果你更偏向阅读方法论文档而不是直接调用技能，则可以直接浏览 `playbooks/` 与 `examples/` 目录。

## Workflow Architecture

整个方法遵循一个闭环：先找到真实用户会问什么，再监控模型如何回答，然后把内容铺到每个模型最可能学习和检索的位置，在发布前做 GEO 质检，最后对负向或错误回答做归因与修复，并把修复结果重新带回监控。

| 阶段 | 核心问题 | 主要产物 | 对应文件 |
|---|---|---|---|
| 关键词研究 | 用户会用什么任务语言提问？ | 场景矩阵、三级关键词、初始 Query Pool | `playbooks/keyword-strategy.md` |
| GEO 监控 | 模型是否提及、是否推荐、是否说对？ | 四维指标周报、模型盘点、异常清单 | `playbooks/monitoring-system.md` |
| 内容铺设 | 应该去哪里铺内容才能影响不同模型？ | 数据源地图、渠道优先级、模型分发策略 | `playbooks/model-datasources.md` `playbooks/content-platform-map.md` |
| 发布前质检 | 这篇内容是否足够可引用、可抽取、可验证？ | 质检记录、结构优化建议、实体清晰度结论 | `skills/geo-content-check/` |
| 负向修复 | 错误、负面、过时、竞品植入如何分类处理？ | 事件归因、修复 SOP、回归监控建议 | `playbooks/negative-fix-sop.md` `skills/geo-fix-negative/` |

## Core Modules

### 1. Keyword Research

关键词研究不是从功能清单倒推，而是从 **用户任务场景** 正推。对于开发者工具，这意味着优先围绕 “怎么把 PDF 变成 RAG 数据”“怎么提取公式和表格”“怎么接到 LangChain / LlamaIndex / MCP / Agent 工作流中” 等问题建立场景矩阵，再拆成核心词、场景词与长尾词。

### 2. GEO Monitoring

监控层至少追踪四类指标：**提及率、正面提及率、能力准确率、生态准确率**。如果只看“有没有被提到”，就无法知道模型是不是在错误地引用你、把你和别的实体混淆，或在关键集成问题上完全缺失。[2]

### 3. Content Placement

不同模型的训练语料和检索入口并不一致，因此内容铺设必须按模型拆开。对于技术产品，GitHub README、官方文档、PyPI、HuggingFace、技术博客和问答社区往往比泛营销站更重要。参考实践中，GitHub、文档、参考资料与 Skill 元数据往往需要在同一个仓库里协同维护，才能形成稳定的知识出口。[1] [3]

### 4. Negative Fix SOP

当模型给出错误事实、负面判断、过时描述或竞品单边植入时，修复策略不能统一处理。你需要先判断负向类型，再区分“纠正信源”“发布权威覆盖”“承认限制并重塑场景边界”“提升竞品对比词覆盖”这几类动作。

## Skill Map

| Skill | 用途 | 典型输入 | 典型输出 |
|---|---|---|---|
| `geo-keyword-matrix` | 从产品描述生成场景矩阵与 Query Pool | 产品描述、目标用户、核心能力、竞品 | 核心词/场景词/长尾词、场景矩阵、验证闭环 |
| `geo-monitor` | 跑 Query Pool 并生成四维指标周报 | Query Pool、模型列表、回答样本 | 提及率/正面率/能力准确率/生态准确率周报 |
| `geo-content-check` | 发布前进行 GEO 质检 | 草稿、实体定义、目标模型 | 质检分、结构缺口、引用友好性建议 |
| `geo-fix-negative` | 识别负向类型并生成修复方案 | 负向回答、引用来源、标准事实 | 类型判断、修复动作表、回归验证计划 |

## MinerU Example

本仓库附带一个基于 MinerU 的完整示例，包括 Query Pool、模型与渠道映射、案例化工作流说明，以及针对 PDF 解析、RAG 预处理、学术文档处理、开源替代方案等高价值场景的关键词组织方式。你可以把它视为一个可复制模板，再替换成自己的项目。

## Integration with seo-geo-claude-skills

本项目并不试图重复造一个通用 SEO/GEO 技能库，而是把自己定位成 **垂直于开发者工具与开源项目的 GEO 闭环层**。在执行上，它适合与 `keyword-research`、`serp-analysis`、`competitor-analysis`、`geo-content-optimizer`、`content-quality-auditor`、`entity-optimizer`、`schema-markup-generator` 等现有技能配合使用。[2]

具体映射关系见 `playbooks/seo-geo-claude-skills-integration.md`。

## Repository Map

```text
geo-monitor-toolkit/
├── README.md
├── LICENSE
├── SKILL.md
├── manifest.json
├── query-pools/
│   └── mineru-example.json
├── playbooks/
│   ├── geo-workflow-architecture.md
│   ├── keyword-strategy.md
│   ├── monitoring-system.md
│   ├── model-datasources.md
│   ├── content-platform-map.md
│   ├── negative-fix-sop.md
│   └── seo-geo-claude-skills-integration.md
├── examples/
│   └── mineru-case-study.md
└── skills/
    ├── geo-monitor/
    ├── geo-content-check/
    ├── geo-fix-negative/
    └── geo-keyword-matrix/
```

## Recommended Adoption Order

| 周期 | 重点动作 | 目标 |
|---|---|---|
| 第 1 周 | 建关键词矩阵、整理 Query Pool、设定监控口径 | 建好监控地基 |
| 第 2-3 周 | 跑首轮监控、确认模型短板、输出渠道优先级 | 找到优先修复面 |
| 第 3-6 周 | 按模型做内容铺设并执行发布前质检 | 提升被引用概率 |
| 第 4-8 周 | 跟踪负向内容、执行类型化修复、做回归监控 | 缩短修复周期并提升正面提及率 |

## References

[1]: https://github.com/dageno-agents/geo-content-writer "dageno-agents/geo-content-writer"
[2]: https://github.com/aaron-he-zhu/seo-geo-claude-skills "aaron-he-zhu/seo-geo-claude-skills"
[3]: https://github.com/yaojingang/yao-geo-skills/tree/main/skills/geoflow-cli-ops "yaojingang/yao-geo-skills geoflow-cli-ops"
