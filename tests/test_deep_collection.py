"""Offline regression checks for the 2026-11-09 source-backed collection."""

from __future__ import annotations

from copy import deepcopy
from datetime import date
import json
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

from human_data_lib import Catalog, CatalogError, load_catalog
from human_data_lib.catalog import canonical_repo_url


ROOT = Path(__file__).resolve().parents[1]


class DeepCollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.raw = json.loads((ROOT / "src/human_data_lib/data/libraries.json").read_text())
        cls.review = json.loads((ROOT / "docs/reviews/2026-11-09-source-review.json").read_text())

    def fixture(self):
        raw = deepcopy(self.raw)
        raw["entries"] = raw["entries"][:1]
        return raw

    def test_source_review_counts_and_evidence(self):
        accepted = [entry for entry in self.review["candidates"] if entry["decision"] == "included"]
        self.assertEqual(len(accepted), 142)
        self.assertEqual(self.review["baseline_entries"] + len(accepted), self.review["total_entries"])
        for reviewed in accepted:
            with self.subTest(identity=reviewed["id"]):
                entry = self.catalog.get(reviewed["id"])
                self.assertEqual(entry.repo_url, reviewed["repo_url"])
                self.assertEqual(entry.license, reviewed["license"])
                self.assertFalse(reviewed["archived"])
                date.fromisoformat(reviewed["checked_at"])
                self.assertTrue(reviewed["sources"])
                self.assertIn(reviewed["license_source"], reviewed["sources"])
                for source in reviewed["sources"]:
                    self.assertRegex(source["sha"], r"^[0-9a-f]{40}$")
                    self.assertTrue(source["url"].startswith(entry.repo_url + "/blob/"))

    def test_complete_registry_screening(self):
        screening = self.review["registry_screening"]
        self.assertEqual(len(screening), 133)
        self.assertEqual(sum(e["decision"] == "catalogued" for e in screening), 119)
        self.assertEqual(len({e["registry_path"] for e in screening}), len(screening))
        for entry in screening:
            if entry["entry_id"]:
                self.catalog.get(entry["entry_id"])
            else:
                self.assertTrue(entry["reason"])

    def test_existing_audit_does_not_claim_unchecked_sources(self):
        audit = json.loads((ROOT / "docs/reviews/2026-11-09-existing-repository-audit.json").read_text())["entries"]
        self.assertEqual(len(audit), 1226)
        self.assertEqual(sum(e["status"] == "ok" for e in audit), 1105)
        self.assertEqual(sum(e["status"] == "not_checked" for e in audit), 121)
        self.assertEqual(sum(e.get("archived") is True for e in audit), 6)
        for item in audit:
            if item.get("archived"):
                self.assertEqual(self.catalog.get(item["id"]).maturity, "archived")

    def test_all_entries_have_navigable_anchors_and_index_links(self):
        page = (ROOT / "catalog.md").read_text()
        index = (ROOT / "docs/catalog-index.md").read_text()
        anchors = re.findall(r'<a id="([^"]+)"', page)
        self.assertEqual(len(anchors), len(self.catalog))
        self.assertEqual(len(set(anchors)), len(self.catalog))
        for entry in self.catalog:
            self.assertIn(f"../catalog.md#{entry.id}", index, entry.id)
        index_anchors = re.findall(r'<a id="([^"]+)"', index)
        self.assertEqual(len(index_anchors), len(set(index_anchors)))
        for target in re.findall(r"\]\(#([^)]+)\)", index):
            self.assertIn(target, index_anchors)

    def test_generated_catalog_and_index_match_source(self):
        spec = importlib.util.spec_from_file_location("render_catalog", ROOT / "tools/render_catalog_page.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            module.OUTPUT = Path(directory) / "catalog.md"
            module.INDEX_OUTPUT = Path(directory) / "index.md"
            module.main()
            self.assertEqual(module.OUTPUT.read_bytes(), (ROOT / "catalog.md").read_bytes())
            self.assertEqual(module.INDEX_OUTPUT.read_bytes(), (ROOT / "docs/catalog-index.md").read_bytes())

    def test_invalid_identity_and_calendar_date_are_rejected(self):
        raw = self.fixture()
        for identity in ("Bad_ID", "a b", "../repo", ""):
            raw["entries"][0]["id"] = identity
            with self.assertRaises(CatalogError):
                Catalog.from_dict(raw)
        raw = self.fixture()
        for invalid in ("2026-02-30", "20261109", "tomorrow"):
            raw["generated_at"] = invalid
            with self.assertRaises(CatalogError):
                Catalog.from_dict(raw)

    def test_duplicate_repo_spelling_is_rejected(self):
        raw = self.fixture()
        duplicate = deepcopy(raw["entries"][0])
        duplicate["id"] = "different-id"
        duplicate["repo_url"] = duplicate["repo_url"].upper().replace("HTTPS", "https") + ".GIT/"
        raw["entries"].append(duplicate)
        with self.assertRaises(CatalogError):
            Catalog.from_dict(raw)
        self.assertEqual(canonical_repo_url("https://GitHub.com/OpenMS/OpenMS.git/"), "https://github.com/openms/openms")

    def test_duplicate_tags_and_missing_url_host_are_rejected(self):
        raw = self.fixture()
        raw["entries"][0]["domains"] *= 2
        with self.assertRaises(CatalogError):
            Catalog.from_dict(raw)
        raw = self.fixture()
        raw["entries"][0]["official_url"] = "https:///broken"
        with self.assertRaises(CatalogError):
            Catalog.from_dict(raw)

    def test_known_shared_repository_is_documented(self):
        for identity in ("openms", "pyopenms"):
            self.assertIn("同一ソース", self.catalog.get(identity).notes)
        self.assertEqual(self.catalog.get("openms").repo_url, self.catalog.get("pyopenms").repo_url)

    def test_explicit_noncommercial_candidate_is_not_added(self):
        with self.assertRaises(KeyError):
            self.catalog.get("celloracle")
        candidate = next(c for c in self.review["candidates"] if c["name"] == "CellOracle")
        self.assertEqual(candidate["decision"], "deferred")
        self.assertIn("非商用", candidate["reason"])


if __name__ == "__main__":
    unittest.main()
