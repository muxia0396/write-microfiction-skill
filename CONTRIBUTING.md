# 贡献指南

感谢你愿意改进 `write-microfiction`。本项目欢迎问题报告、测试题、工作流规则、文档修正和脚本改进。

## 提交 Issue

提交问题前，请先搜索现有 Issue，避免重复。行为问题尽量包含：

- 完整提示词和期望交付物；
- 实际输出或最小可复现片段；
- 使用的智能体环境（如 Codex）及是否显式调用 `$write-microfiction`；
- 你认为违反的硬约束或暴露的失败模式；
- 输出包含个人信息时，请先匿名化。

不要上传无权公开的书籍、文章、扫描件、用户草稿或其他受保护材料。

## 提交 Pull Request

1. 从目标分支创建范围单一的分支。
2. 只修改解决当前问题所需的文件。
3. 在 PR 中说明问题、改动机制和验证方法。
4. 修改 Skill 行为时，尽量在 `comparison-test/prompts.md` 增加或指出可复现题目。
5. 修改 `story_metrics.py` 时，补充或更新自动化测试。
6. 确认没有提交扫描资料、OCR 中间文件、个人路径、凭据或大体积生成文件。

## Skill 内容原则

- `SKILL.md` 只保留核心工作流和资源导航，避免重复参考文件的详细内容。
- 触发场景应写在 YAML frontmatter 的 `description` 中。
- 详细知识按需放入 `references/`，并从 `SKILL.md` 直接链接。
- 确定性、重复性的检查优先实现为 `scripts/` 下的脚本。
- 不把审美偏好写成无条件规则；规则应对应可说明的失败模式。
- 不复制第三方教材中的例文、专名或受版权保护表达。

## 本地验证

运行测试：

```bash
python -m unittest discover -s tests -v
```

检查脚本语法：

```bash
python -m py_compile write-microfiction/scripts/story_metrics.py
```

如果你的环境中可用 Codex 官方 `skill-creator`，还应使用它的 `quick_validate.py` 校验 `write-microfiction/`。

## 贡献许可

除非你明确另行声明，主动提交并被项目接收的贡献将按照本仓库的 Apache License 2.0 授权。请只提交你有权以该许可证发布的内容。
