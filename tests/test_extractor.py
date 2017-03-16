from __future__ import absolute_import
from extractor import Extractor
import sharedlibs.config as _config
from unittest import TestCase


class TestExtractor(TestCase):
    def test_extractor_database_connection(self):
        e = Extractor()
        self.assertTrue(e.extract_tester(_config.OracleTestQuery))











