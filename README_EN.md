<p align="right">
  <a href="./README.md">中文</a> ·
  <b>English</b>
</p>

<h1 align="center">write-microfiction-skill</h1>

<p align="center">
  <strong>An agent Skill for writing, critiquing, and revising Chinese microfiction (using Codex as an example)</strong>
  <br>
  <em>Turn a fragment of inspiration into a disciplined narrative workflow without flattening literary judgment.</em>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-5c6ac4" alt="Apache-2.0 License"></a>
  <a href="./write-microfiction/SKILL.md"><img src="https://img.shields.io/badge/Agent-Skill-111827" alt="Agent Skill"></a>
</p>

---

## What it is

`write-microfiction` is a Chinese microfiction Skill for agents that support Skills, with Codex used as the installation and invocation example. It supports ideation, drafting, critique, revision, and technique-focused instruction. It is a writing workflow rather than a fixed story template.

Example:

```text
Use $write-microfiction to write a Chinese microfiction story of about
700 Chinese characters set on the first bus at 4 a.m. Do not use a twist.
Return only the title and story.
```

## Capabilities

- Develop a sentence, observation, news-inspired idea, or character fragment into a story.
- Design twists, omissions, foreshadowing, symbols, satire, and psychological turns.
- Diagnose forced twists, didactic endings, weak causality, and unfocused characters.
- Revise while preserving the draft's effective intent and distinctive details.
- Teach microfiction techniques with original miniature examples.
- Check length, forbidden terms, paragraphing, dialogue ratio, and didactic markers with a deterministic local script.

## Installation

Ask a compatible agent from the repository. For example, in Codex:

```text
Install the write-microfiction Skill from this repository into my agent environment.
```

Or copy the directory manually. The following paths use Codex as the example:

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\write-microfiction" "$env:USERPROFILE\.codex\skills\"
```

macOS or Linux:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./write-microfiction "${CODEX_HOME:-$HOME/.codex}/skills/"
```

For Codex, start a new task after installation so the Skill list is reloaded.

## Repository layout

```text
write-microfiction/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── foundations.md
│   ├── techniques.md
│   ├── workflows.md
│   └── quality-rubric.md
└── scripts/story_metrics.py
```

The repository also contains a reproducible evaluation set under `comparison-test/`, a concise [evaluation note](./docs/EVALUATION.md), tests, and community files.

## Evaluation

The fixed evaluation set contains 18 tasks spanning drafting, no-twist writing, ideation, fair twists, open endings, critique, structural revision, technique instruction, anonymization, ultra-short fiction, and narrow constraints.

The repository publishes the same 18 prompts and both complete answers under two conditions: no Skill and v2. The README does not prescribe a score or conclusion. Inspect [No Skill vs v2: full output comparison](./comparison-test/unused-skill-vs-v2.md) and judge the differences directly.

## Contributing

Issues, evaluation cases, writing rules, and code improvements are welcome. Read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

## License and source-material boundary

Original Skill instructions, scripts, and project documentation are licensed under the [Apache License 2.0](./LICENSE).

Scanned books, OCR intermediates, source examples, and other third-party materials are not covered by that license and are excluded from the default open-source distribution. See [NOTICE](./NOTICE).
