"""Source-verified eeglabio catalog record tests."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class EeglabioCatalogTests(unittest.TestCase):
    def test_eeglabio_metadata_and_uniqueness(self):
        data = json.loads((ROOT / "src/human_data_lib/data/libraries.json").read_text(encoding="utf-8"))
        hits = [e for e in data["entries"] if e["id"] == "eeglabio"]
        self.assertEqual(len(hits), 1)
        item = hits[0]
        self.assertEqual(item["repo_url"], "https://github.com/jackz314/eeglabio")
        self.assertEqual(item["license"], "BSD-3-Clause")
        self.assertIn("h5py", item["notes"])
        self.assertEqual(sum(e["repo_url"].lower().rstrip("/") == item["repo_url"].lower() for e in data["entries"]), 1)

    def test_public_pages_include_entry(self):
        self.assertIn('<a id="eeglabio"></a>', (ROOT / "catalog.md").read_text(encoding="utf-8"))
        self.assertIn("[eeglabio](../catalog.md#eeglabio)", (ROOT / "docs/catalog-index.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
