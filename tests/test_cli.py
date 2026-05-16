from __future__ import annotations

import contextlib
from io import StringIO
import unittest

from human_data_lib.cli import main


class CliTests(unittest.TestCase):
    def test_validate(self) -> None:
        out = StringIO()
        with contextlib.redirect_stdout(out):
            code = main(["validate"])
        self.assertEqual(code, 0)
        self.assertIn("OK:", out.getvalue())

    def test_search_outputs_scanpy(self) -> None:
        out = StringIO()
        with contextlib.redirect_stdout(out):
            code = main(["search", "single-cell", "--ecosystem", "Python"])
        self.assertEqual(code, 0)
        self.assertIn("scanpy", out.getvalue())

    def test_scale_filter_outputs_population_entries(self) -> None:
        out = StringIO()
        with contextlib.redirect_stdout(out):
            code = main(["list", "--scale", "population"])
        self.assertEqual(code, 0)
        self.assertIn("population", out.getvalue())

    def test_show_missing_returns_error(self) -> None:
        err = StringIO()
        with contextlib.redirect_stderr(err):
            code = main(["show", "not-a-real-entry"])
        self.assertEqual(code, 1)
        self.assertIn("見つかりませんでした", err.getvalue())


if __name__ == "__main__":
    unittest.main()
