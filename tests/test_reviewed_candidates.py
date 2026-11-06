"""Regression coverage for the canonical entries reviewed in issue #3."""

import json
import unittest
from pathlib import Path


class ReviewedCandidatesTests(unittest.TestCase):
    def test_distinct_official_candidates_and_licenses(self):
        root = Path(__file__).resolve().parents[1]
        entries = json.loads(
            (root / "src/human_data_lib/data/libraries.json").read_text(encoding="utf-8")
        )["entries"]
        expected = {
            "pylsl": ("https://github.com/labstreaminglayer/pylsl", "MIT"),
            "tensorpac": ("https://github.com/EtienneCmb/tensorpac", "BSD-3-Clause"),
        }
        for identity, (url, license_name) in expected.items():
            with self.subTest(identity=identity):
                matches = [entry for entry in entries if entry["id"] == identity]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["repo_url"], url)
                self.assertEqual(matches[0]["license"], license_name)
                self.assertEqual(
                    sum(
                        entry.get("repo_url", "").lower().rstrip("/").removesuffix(".git")
                        == url.lower()
                        for entry in entries
                    ),
                    1,
                )


if __name__ == "__main__":
    unittest.main()
