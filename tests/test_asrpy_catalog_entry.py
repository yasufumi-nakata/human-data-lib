"""Regression test for the independently reviewed ASRpy catalog entry."""

import json
import unittest
from pathlib import Path


class AsrpyCatalogTests(unittest.TestCase):
    def test_asrpy_primary_source_and_caveat(self):
        root = Path(__file__).resolve().parents[1]
        catalog = json.loads((root / "src/human_data_lib/data/libraries.json").read_text(encoding="utf-8"))
        matches = [entry for entry in catalog["entries"] if entry["id"] == "asrpy"]
        self.assertEqual(len(matches), 1)
        entry = matches[0]
        self.assertEqual(entry["repo_url"], "https://github.com/DiGyt/asrpy")
        self.assertEqual(entry["license"], "BSD-3-Clause")
        self.assertIn("保守", entry["notes"])
        self.assertEqual(
            sum(item["repo_url"].lower().rstrip("/").removesuffix(".git") == "https://github.com/digyt/asrpy" for item in catalog["entries"]),
            1,
        )


if __name__ == "__main__":
    unittest.main()
