"""Offline checks for the dependency-free GitHub Pages search interface."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.labels = []
        self.local_assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "label" and "for" in attrs:
            self.labels.append(attrs["for"])
        if tag == "script" and attrs.get("src"):
            self.local_assets.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.local_assets.append(attrs["href"])


class SiteInterfaceTests(unittest.TestCase):
    def test_home_has_valid_labels_unique_ids_and_local_assets(self):
        parser = PageParser()
        parser.feed((ROOT / "index.html").read_text())
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        for label in parser.labels:
            self.assertIn(label, parser.ids)
        for asset in parser.local_assets:
            self.assertTrue((ROOT / asset.split("?", 1)[0]).is_file(), asset)

    def test_fallback_and_single_source_of_truth(self):
        html = (ROOT / "index.html").read_text()
        script = (ROOT / "assets/catalog.mjs").read_text()
        self.assertIn("<noscript>", html)
        self.assertIn('href="catalog.html"', html)
        self.assertIn("src/human_data_lib/data/libraries.json", script)
        self.assertNotIn("innerHTML", script)
        self.assertIn('aria-live="polite"', html)
        self.assertIn('class="skip-link"', html)

    @unittest.skipUnless(shutil.which("node"), "Node.js is unavailable; run UI logic checks with node --test tests/catalog-ui.test.mjs")
    def test_catalog_search_logic(self):
        result = subprocess.run(["node", "--test", "tests/catalog-ui.test.mjs"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
