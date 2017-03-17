from mock import patch
from sharedlibs.tools_dynamo import ToolsDynamo
from unittest import TestCase


@staticmethod
def fake_get_record(url):
    return {"a": "b"}

@staticmethod
def fake_read_table(table):
    return '2010-11-01 15:31:10.386000-07:00'


class TestDynamo(TestCase):
    def create_patch(self, name, fakemethod):
        self.patcher = patch(name, fakemethod)
        thing = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        return thing

    def test_get_record_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.get_record', fake_get_record)
        table = 'test'
        self.client = ToolsDynamo()
        response = self.client.get_record(table)
        self.assertIn('a', response)
        self.assertEqual(response['a'], 'b')

    def test_read_table_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.read_table', fake_read_table)
        table = 'test'
        self.client = ToolsDynamo()
        response = self.client.read_table(table)
        self.assertEqual(response, '2010-11-01 15:31:10.386000-07:00')












