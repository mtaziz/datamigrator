from __future__ import absolute_import
from mock import patch
from sharedlibs.tools_dynamo import ToolsDynamo
from unittest import TestCase


@staticmethod
def fake_get_record(url):
    return {"a": "b"}
    # return from a file...
    # parsed_url = urlparse(url)
    # resource_file = os.path.normpath('tests/resources%s' % parsed_url.path)
    # Must return a file-like object
    # return open(resource_file, mode='rb')

class TestDynamo(TestCase):
    def setUp(self):
        self.patcher = patch('sharedlibs.tools_dynamo.ToolsDynamo.get_record', fake_get_record)
        self.patcher.start()
        self.client = ToolsDynamo()

    def tearDown(self):
        self.patcher.stop()

    def test_loader_mock(self):
        table = 'test_table'
        response = self.client.get_record(table)
        self.assertIn('a', response)
        self.assertEqual(response['a'], 'b')










