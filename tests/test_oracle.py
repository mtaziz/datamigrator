from mock import patch
from sharedlibs.tools_oracle import ToolsOracle
from unittest import TestCase


@staticmethod
def fake_get_record(url):
    # fake a data return, not sure of the format that will be used
    return {"a": "b"}


class TestOracle(TestCase):
    def setUp(self):
        self.patcher = patch('sharedlibs.tools_oracle.ToolsOracle.get_record', fake_get_record)
        self.patcher.start()
        self.client = ToolsOracle()

    def tearDown(self):
        self.patcher.stop()

    def test_loader_mock(self):
        table = 'test_table'
        response = self.client.get_record(table)
        self.assertIn('a', response)
        self.assertEqual(response['a'], 'b')










