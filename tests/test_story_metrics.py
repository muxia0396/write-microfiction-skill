from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "write-microfiction" / "scripts" / "story_metrics.py"
SPEC = importlib.util.spec_from_file_location("story_metrics", SCRIPT)
assert SPEC and SPEC.loader
story_metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(story_metrics)


class AnalyzeTests(unittest.TestCase):
    def test_counts_and_didactic_marker(self) -> None:
        result = story_metrics.analyze("甲说：“走吧。”\n\n这个故事告诉我们要守时。")

        self.assertEqual(result["paragraphs"], 2)
        self.assertEqual(result["dialogue_segments"], 1)
        self.assertTrue(result["didactic_marker_hits"])

    def test_constraints_and_forbidden_terms(self) -> None:
        result = story_metrics.analyze(
            "短稿里出现禁词。",
            min_chars=20,
            forbidden=("禁词",),
        )

        self.assertFalse(result["constraints_passed"])
        self.assertEqual(len(result["constraint_violations"]), 2)

    def test_strict_cli_returns_two_for_violation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            draft = Path(temp_dir) / "draft.md"
            draft.write_text("太短。", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(draft),
                    "--min-chars",
                    "10",
                    "--strict",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(completed.returncode, 2)
        self.assertIn('"constraints_passed": false', completed.stdout)


if __name__ == "__main__":
    unittest.main()

