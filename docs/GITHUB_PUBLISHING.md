# GitHub 发布资料清单

这份清单用于把本地仓库发布到 GitHub。以下文案可以直接复制，再按实际仓库名称调整。

## 1. 新建或整理仓库

### Repository name

```text
write-microfiction-skill
```

仓库名称中的 `-skill` 用于明确项目类型；可安装的 Skill 名称仍为 `write-microfiction`。

### Description

```text
中文微型小说创作、诊断与精修 Skill
```

### Visibility

选择：

```text
Public
```

### 初始化选项

如果从当前本地仓库推送到一个新的空 GitHub 仓库，不要在 GitHub 创建页面勾选以下选项：

- Add a README file
- Add .gitignore
- Choose a license

这些文件本地已经存在，远程再次生成会增加首次推送时的合并冲突。

## 2. 仓库主页 About

进入仓库主页，点击右侧 About 区域的齿轮。

### Description

填写前面给出的项目简介。

### Website

当前没有独立文档站或项目主页时保持为空。不要为了填满字段而重复填写仓库地址。

### Topics

推荐添加：

```text
agent-skill
ai-agents
codex-skill
openai-codex
microfiction
flash-fiction
chinese-writing
creative-writing
writing-assistant
prompt-engineering
chinese-language
```

Topic 使用小写字母和连字符。以后可以根据实际访问来源删减，不必一次填满 20 个。

## 3. Social preview

路径：

```text
Settings → General → Social preview
```

建议准备一张 1280 × 640 的 PNG 或 JPG，内容只保留：

```text
write-microfiction-skill
中文微型小说智能体 Skill（以 Codex 为例）
构思 · 创作 · 诊断 · 精修
```

图片应小于 1 MB，使用纯色背景或确保透明背景在深浅色界面都清晰。

## 4. Features

路径：

```text
Settings → General → Features
```

首发建议：

- Issues：开启。仓库已经准备好问题与功能建议模板。
- Discussions：可以暂不开启；出现稳定用户和交流需求后再开启。
- Projects：暂不开启，除非准备在 GitHub 看板公开维护路线图。
- Wiki：关闭。当前文档已集中在 README 与 `docs/`，避免两处内容不同步。
- Sponsorships：有明确赞助渠道后再开启。

## 5. Security

路径：

```text
Settings → Security → Advanced Security
```

建议开启：

- Private vulnerability reporting；
- Dependabot alerts；
- Secret scanning；
- Push protection（账户和仓库类型支持时）。

仓库已经包含 `SECURITY.md`。开启私密漏洞报告后，安全研究者可以通过非公开表单提交问题。

## 6. 默认分支与合并保护

默认分支使用：

```text
main
```

第一次推送并成功运行 GitHub Actions 后，再为 `main` 添加 Ruleset 或 Branch protection：

- 合并前要求状态检查通过；
- 要求分支在合并前与目标分支保持最新；
- 禁止 force push；
- 禁止删除默认分支；
- 如果只有一名维护者，可以暂不强制每次都走 Pull Request。

不要在第一次 Actions 尚未产生检查名称前设置“必需状态检查”，否则容易选错检查或阻塞首发。

## 7. Issue Labels

GitHub 默认标签可以保留，并建议补充：

- `evaluation`：评测题、评分方法和对比结果；
- `skill-behavior`：Skill 触发与工作流行为；
- `writing-rule`：写作规则或失败模式；
- `documentation`：README 与说明文档；
- `good first issue`：适合首次贡献；
- `question`：使用问题。

## 8. 首个 Release

如果希望把当前版本作为稳定 v2 发布：

```text
Tag: v2.0.0
Release title: write-microfiction-skill v2.0.0 — 首个公开版本
```

如果仍准备频繁调整 Skill 规则，可以改为：

```text
Tag: v0.2.0
Release title: write-microfiction-skill v2 — Public Preview
勾选：Set as a pre-release
```

推荐 Release 说明：

```markdown
## 首个公开版本

`write-microfiction` 是一个面向智能体（以 Codex 为例）的中文微型小说创作、诊断、
改写与技法教学 Skill。

### 主要能力

- 从生活细节、新闻灵感、人物片段或一句话题材发展故事
- 支持成稿、构思、诊断、结构改写和技法教学
- 检查篇幅、禁用词和说教提示词等确定性约束
- 使用渐进式参考文件降低无关上下文占用

### 公开评测

仓库包含 18 道固定题目、评分量表，以及“未使用 Skill 与 v2”
两组完整回答，欢迎读者自行判断。

### 安装

将 `write-microfiction/` 复制到目标智能体的 Skills 目录。以 Codex 为例，
复制到个人 Skills 目录后新建一个任务，使 Skill 列表重新载入。

### 资料边界

扫描书籍、OCR 中间结果和第三方来源例文不包含在发布内容中，
也不属于 Apache-2.0 授权范围。
```

GitHub Release 会自动提供该标签对应源码的 ZIP 和 tar.gz 下载，不需要另行上传整个仓库压缩包。

## 9. 发布前最后检查

- README 中的仓库地址、Issues 地址和徽章均指向最终仓库名；
- GitHub 正确识别根目录 `LICENSE` 为 Apache-2.0；
- Actions 的 `Validate` 工作流通过；
- PDF、OCR 文件、盲评映射和个人路径没有出现在提交列表；
- 完整对比文档可以从 README 点击打开；
- `main` 是默认分支；
- About 简介和 Topics 已填写；
- Social preview 已上传或明确暂缓；
- 首个 Release 的版本号与 README 中的 v2 表述一致。

## GitHub 官方参考

- [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [Customizing your repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [Managing releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [Configuring private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository)
