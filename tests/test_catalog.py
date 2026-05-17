from __future__ import annotations

import json
from pathlib import Path
import unittest

from human_data_lib import CatalogError, load_catalog


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()

    def test_catalog_is_non_empty_and_unique(self) -> None:
        ids = [entry.id for entry in self.catalog]
        self.assertGreaterEqual(len(ids), 100)
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_entry_has_public_repository_url(self) -> None:
        for entry in self.catalog:
            self.assertTrue(entry.repo_url, entry.id)
            self.assertTrue(entry.repo_url.startswith(("https://", "http://")), entry.id)

    def test_every_entry_has_scale(self) -> None:
        for entry in self.catalog:
            self.assertGreaterEqual(len(entry.scales), 1, entry.id)

    def test_search_by_keyword_and_filter(self) -> None:
        entries = self.catalog.search("single-cell", ecosystem="Python")
        names = {entry.name for entry in entries}
        self.assertIn("Scanpy", names)

    def test_search_by_scale(self) -> None:
        entries = self.catalog.search(scale="population")
        self.assertTrue(any("clinical-data" in entry.domains for entry in entries))

    def test_facet_counts_include_major_domains(self) -> None:
        counts = self.catalog.facet_counts("domains")
        self.assertIn("genomics", counts)
        self.assertIn("neurophysiology", counts)
        self.assertIn("clinical-data", counts)

    def test_facet_counts_include_scales(self) -> None:
        counts = self.catalog.facet_counts("scales")
        self.assertIn("molecular", counts)
        self.assertIn("cellular", counts)
        self.assertIn("population", counts)

    def test_json_export_round_trips(self) -> None:
        exported = json.loads(self.catalog.to_json(self.catalog.search(task="workflow")))
        self.assertEqual(exported["schema_version"], self.catalog.schema_version)
        self.assertGreaterEqual(len(exported["entries"]), 1)

    def test_unknown_facet_raises(self) -> None:
        with self.assertRaises(CatalogError):
            self.catalog.facet_counts("unknown")

    def test_public_catalog_page_lists_every_entry(self) -> None:
        page = (ROOT / "catalog.md").read_text(encoding="utf-8")
        self.assertIn("# 全件カタログ", page)
        for entry in self.catalog:
            self.assertIn(f"`{entry.id}`", page)


if __name__ == "__main__":
    unittest.main()
