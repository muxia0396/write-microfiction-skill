<p align="right">
  <b>中文</b> ·
  <a href="./README_EN.md">English</a>
</p>

<h1 align="center">write-microfiction-skill</h1>

<p align="center">
  <strong>面向智能体（以 Codex 为例）的中文微型小说创作、诊断与精修 Skill</strong>
  <br>
  <em>把灵感变成可执行的叙事工作流，同时保留文学判断的开放性。</em>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-5c6ac4" alt="Apache-2.0 License"></a>
  <a href="./write-microfiction/SKILL.md"><img src="https://img.shields.io/badge/Agent-Skill-111827" alt="Agent Skill"></a>
  <a href="https://github.com/muxia0396/write-microfiction-skill/issues"><img src="https://img.shields.io/github/issues/muxia0396/write-microfiction-skill" alt="GitHub issues"></a>
</p>

---

## 一句话说明

`write-microfiction` 是一个可供支持 Skills 的智能体使用的中文微型小说 Skill（以 Codex 为例）。它不是固定模板或故事生成器，而是一套覆盖构思、成稿、诊断、改写和技法教学的写作工作流。

安装后，你可以直接向智能体提出：

```text
使用 $write-microfiction，把“凌晨四点的首班公交”写成一篇 700 字左右、
不使用反转的中文微型小说，只给标题和正文。
```

## 主要能力

- 从一句话、生活细节、新闻灵感或人物片段发展故事。
- 设计反转、留白、伏笔、象征、讽刺和心理转折。
- 创作约 600—1200 字的中文微型小说，也支持更严格的篇幅约束。
- 诊断平铺直叙、强行反转、结尾说教、人物失焦和因果失真。
- 在保留原稿有效意图的前提下进行轻改、结构重写或风格重写。
- 解释微型小说主题与技法，并使用原创微型示例教学。
- 使用本地脚本检查字符数、段落、对话比例、禁用词和说教提示词。

## 快速导航

- 第一次使用：阅读[安装](#安装)与[在智能体中调用](#在智能体中调用)。
- 想了解 Skill 如何工作：阅读[项目结构](#项目结构)。
- 想核对测试方法：阅读[能力验证](#能力验证)。
- 准备发布到 GitHub：阅读[GitHub 发布资料清单](./docs/GITHUB_PUBLISHING.md)。
- 想参与改进：阅读[贡献指南](./CONTRIBUTING.md)。
- 发现问题：提交 [GitHub Issue](https://github.com/muxia0396/write-microfiction-skill/issues)。

## 安装

### 方式一：使用智能体安装 Skill（以 Codex 为例）

以 Codex 为例，在任务中打开本仓库后提出：

```text
请把 https://github.com/muxia0396/write-microfiction-skill 的skill安装到我当前使用的智能体。
```

智能体会读取 `SKILL.md` 并按自身的 Skill 机制完成安装；Codex 还会校验目录结构并安装到个人 Skills 目录。

### 方式二：手动安装（以 Codex 为例）

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\write-microfiction" "$env:USERPROFILE\.codex\skills\"
```

macOS 或 Linux：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./write-microfiction "${CODEX_HOME:-$HOME/.codex}/skills/"
```

以 Codex 为例，安装后新建一个任务，使 Skill 列表重新载入。

> 仓库发布版的 `write-microfiction/` 只包含运行所需文件。研究原始资料不会随仓库分发。

## 在智能体中调用

你可以显式调用，也可以让支持该格式的智能体根据任务自动触发。以下以 Codex 为例。

显式调用：

```text
使用 $write-microfiction，诊断下面这篇草稿。先给整体判断，
再列出最多三个最重要的问题和对应修改动作，不要重写全文：
……
```

直接描述任务：

```text
把这段真实经历虚构化为微型小说提纲。先处理隐私和可识别信息，
不要把未经证实的指控写成事实。
```

更多可尝试的请求：

- “给同一素材设计三个有实质差异的故事方向。”
- “把这篇草稿改成 700 字左右，保留旧车票这个细节，删除说教结尾。”
- “解释篇末逆转与悬念的区别，并分别给原创微型示例。”
- “写一篇不超过 120 个中文字符、具有人物认知变化的超短篇。”

## 项目结构

```text
.
├── write-microfiction/          # 可直接安装的 Skill
│   ├── SKILL.md                 # 触发描述与核心工作流
│   ├── agents/
│   │   └── openai.yaml          # 智能体界面元数据（以 Codex 为例）
│   ├── references/
│   │   ├── foundations.md       # 文体边界、主题与创作基础
│   │   ├── techniques.md        # 技法机制与成立条件
│   │   ├── workflows.md         # 构思、成稿、诊断、改稿流程
│   │   └── quality-rubric.md    # 交付前质量检查
│   └── scripts/
│       └── story_metrics.py     # 确定性表层指标与硬约束检查
├── comparison-test/             # 固定题集、量表与可复核测试数据
├── docs/
│   ├── EVALUATION.md            # 精简版能力验证说明
│   └── GITHUB_PUBLISHING.md     # GitHub 网页端发布资料清单
├── tests/                       # 脚本自动化测试
├── CONTRIBUTING.md
├── SECURITY.md
├── NOTICE
└── LICENSE
```

Skill 采用渐进式加载：智能体先看到名称和触发描述，任务触发后读取 `SKILL.md`，再按任务需要读取具体参考文件。这样可以减少无关上下文，同时保留完整的专业工作流。

## 可选的稿件指标检查

`story_metrics.py` 只使用 Python 标准库。运行它需要 Python 3.10 或更高版本。

```bash
python write-microfiction/scripts/story_metrics.py draft.md --pretty
```

需要严格检查篇幅和禁用词时：

```bash
python write-microfiction/scripts/story_metrics.py draft.md \
  --min-chars 600 \
  --max-chars 800 \
  --forbid "这个故事告诉我们" \
  --strict \
  --pretty
```

指标脚本只能发现确定性的表层信号，不能替代文学判断。

## 能力验证

项目使用 18 个固定问题覆盖直接成稿、无反转写作、多方案构思、公平反转、开放结尾、草稿诊断、结构改稿、技法教学、真实经历虚构化、超短篇和极窄约束等任务。

仓库公开保留了同一组 18 道题在“未使用 Skill”和“使用 v2”两种条件下的完整回答，按题目纵向排列，不使用对比表格，也不在 README 中预设评分结论。请直接阅读[未使用 Skill 与 v2 完整回答对比](./comparison-test/unused-skill-vs-v2.md)，自行判断两组回答的差异。

## 贡献

欢迎提交问题、测试题、参考规则和代码改进。涉及 Skill 行为的修改，请同时说明目标失败模式，并尽量补充可复现测试。

提交 Pull Request 前请先阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 许可证与资料边界

本项目原创的 Skill 指令、脚本和项目文档采用 [Apache License 2.0](./LICENSE)。

扫描书籍、OCR 中间结果、来源例文及其他第三方资料不属于本项目的 Apache-2.0 授权范围，也不会包含在默认开源发布内容中。项目运行时参考文件经过重新组织和原创表述，不复制来源书籍中的受版权保护例文。具体说明见 [NOTICE](./NOTICE)。

## 致谢

感谢所有参与测试、提出问题和改进写作工作流的人。
