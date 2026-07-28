#!/usr/bin/env python3
"""Report deterministic surface metrics for a Chinese microfiction draft."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DIDACTIC_MARKERS = (
    "这个故事告诉我们",
    "这件事告诉我们",
    "说明了一个道理",
    "由此可见",
    "这说明",
    "人生就是",
    "人性就是",
)


def analyze(
    text: str,
    *,
    min_chars: int | None = None,
    max_chars: int | None = None,
    count_mode: str = "non-whitespace",
    forbidden: tuple[str, ...] = (),
) -> dict[str, object]:
    non_whitespace = re.sub(r"\s+", "", text)
    chinese_chars = re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff]", text)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n|\r?\n", text) if part.strip()]
    sentences = [
        part.strip()
        for part in re.split(r"(?<=[。！？!?…])", text)
        if part.strip()
    ]
    dialogue_segments = re.findall(r"[“「『](.*?)[”」』]", text, flags=re.DOTALL)
    dialogue_chars = sum(len(re.sub(r"\s+", "", segment)) for segment in dialogue_segments)
    marker_hits = [
        {"marker": marker, "count": text.count(marker)}
        for marker in DIDACTIC_MARKERS
        if marker in text
    ]

    counts = {
        "non-whitespace": len(non_whitespace),
        "chinese": len(chinese_chars),
    }
    constraint_violations: list[str] = []
    selected_count = counts[count_mode]
    if min_chars is not None and selected_count < min_chars:
        constraint_violations.append(
            f"{count_mode} 字符数 {selected_count}，低于下限 {min_chars}。"
        )
    if max_chars is not None and selected_count > max_chars:
        constraint_violations.append(
            f"{count_mode} 字符数 {selected_count}，高于上限 {max_chars}。"
        )
    forbidden_hits = [
        {"term": term, "count": text.count(term)}
        for term in forbidden
        if term and term in text
    ]
    for hit in forbidden_hits:
        constraint_violations.append(
            f"出现禁用词“{hit['term']}” {hit['count']} 次。"
        )

    return {
        "non_whitespace_characters": len(non_whitespace),
        "chinese_characters": len(chinese_chars),
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "dialogue_segments": len(dialogue_segments),
        "dialogue_character_ratio": round(
            dialogue_chars / len(non_whitespace), 3
        ) if non_whitespace else 0.0,
        "didactic_marker_hits": marker_hits,
        "constraint_count_mode": count_mode,
        "constraint_character_count": selected_count,
        "forbidden_term_hits": forbidden_hits,
        "constraint_violations": constraint_violations,
        "constraints_passed": not constraint_violations,
        "length_band": length_band(len(chinese_chars)),
        "notes": build_notes(len(chinese_chars), len(paragraphs), marker_hits),
    }


def length_band(chinese_count: int) -> str:
    if chinese_count < 300:
        return "very-short"
    if chinese_count < 600:
        return "short"
    if chinese_count <= 1200:
        return "default"
    if chinese_count <= 2500:
        return "long"
    return "over-common-upper-bound"


def build_notes(
    chinese_count: int,
    paragraph_count: int,
    marker_hits: list[dict[str, object]],
) -> list[str]:
    notes: list[str] = []
    if chinese_count < 300:
        notes.append("篇幅很短；检查是否仍有人物、事件和认知变化。")
    elif chinese_count > 2500:
        notes.append("超出常见微型小说上限；优先压缩背景、支线和重复解释。")
    if paragraph_count <= 1 and chinese_count >= 600:
        notes.append("正文较长但没有明显分段；检查阅读节奏。")
    if marker_hits:
        notes.append("发现可能的说教提示词；结合上下文判断是否改成动作或细节。")
    if not notes:
        notes.append("未发现确定性的表层红旗；仍需按文学质量量表人工判断。")
    return notes


def read_text(path: str | None) -> str:
    if path and path != "-":
        return Path(path).read_text(encoding="utf-8")
    if sys.stdin.isatty():
        raise SystemExit("请提供 UTF-8 稿件路径，或通过标准输入传入文本。")
    return sys.stdin.read()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="输出中文微型小说稿件的确定性表层指标。"
    )
    parser.add_argument("path", nargs="?", help="UTF-8 文本或 Markdown 稿件路径")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="以缩进 JSON 输出",
    )
    parser.add_argument("--min-chars", type=int, help="允许的最少字符数")
    parser.add_argument("--max-chars", type=int, help="允许的最多字符数")
    parser.add_argument(
        "--count-mode",
        choices=("non-whitespace", "chinese"),
        default="non-whitespace",
        help="约束计数口径：非空白字符或仅中文字符",
    )
    parser.add_argument(
        "--forbid",
        action="append",
        default=[],
        metavar="TERM",
        help="禁用词，可重复传入",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="存在约束违规时以状态码 2 退出",
    )
    args = parser.parse_args()

    if (
        args.min_chars is not None
        and args.max_chars is not None
        and args.min_chars > args.max_chars
    ):
        parser.error("--min-chars 不能大于 --max-chars")

    result = analyze(
        read_text(args.path),
        min_chars=args.min_chars,
        max_chars=args.max_chars,
        count_mode=args.count_mode,
        forbidden=tuple(args.forbid),
    )
    json.dump(
        result,
        sys.stdout,
        ensure_ascii=False,
        indent=2 if args.pretty else None,
    )
    sys.stdout.write("\n")
    if args.strict and not result["constraints_passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
