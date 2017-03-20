import tests.configtests as _config
from sharedlibs.tools_dynamo import ToolsDynamo
from unittest import TestCase

@staticmethod
def fake_create_table(tablename, keyschema, attributedefinitions, provisionedthroughput):
    return True

@staticmethod
def fake_delete_record(tablename, key):
    return True

@staticmethod
def fake_delete_table(tablename):
    return True

@staticmethod
def fake_get_record(tablename, key):
    return _config.DynamoTestRecord

@staticmethod
def fake_get_recordset(tablename, key, keyval):
    return _config.DynamoTestRecordset

@staticmethod
def fake_insert_record(tablename, item):
    return True

@staticmethod
def fake_insert_record_batch(tablename, itemlist):
    return True

@staticmethod
def fake_read_table(table):
    return '2010-11-01 15:31:10.123456-07:00'

@staticmethod
def fake_update_record(tablename, key, updateexpression, expressionattributevalues):
    return True


class TestDynamo(TestCase):
    def create_patch(self, name, fakemethod):
        self.patcher = patch(name, fakemethod)
        thing = self.patcher.start()
        self.client = ToolsDynamo()
        self.addCleanup(self.patcher.stop)
        return thing

    def test_create_table_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.create_table', fake_create_table)
        response = self.client.create_table(_config.DynamoTestTablename, _config.DynamoTestKeySchema,
                                            _config.DynamoTestAttributeDefinitions, _config.DynamoTestProvisionedThroughput)
        self.assertTrue(response)

    def test_delete_record_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.delete_record', fake_delete_record)
        response = self.client.delete_record(_config.DynamoTestTablename, _config.DynamoTestRecord)
        self.assertTrue(response)

    def test_delete_table_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.delete_table', fake_delete_table)
        response = self.client.delete_table(_config.DynamoTestTablename)
        self.assertTrue(response)

    def test_get_record_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.get_record', fake_get_record)
        response = self.client.get_record(_config.DynamoTestTablename, _config.DynamoTestRecord)
        self.assertIn('field_a', response)
        self.assertEqual(response['field_a'], _config.DynamoTestRecord['field_a'])
        self.assertEqual(response['field_b'], _config.DynamoTestRecord['field_b'])

    def test_get_recordset_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.get_recordset', fake_get_recordset)
        key = "username"
        keyval = "janedoe"
        response = self.client.get_recordset(_config.DynamoTestTablename, key, keyval)
        self.assertIn(_config.DynamoTestRecord, response)
        self.assertEqual(response[0]['field_a'], _config.DynamoTestRecordset[0]['field_a'])
        self.assertEqual(response[1]['field_a'], _config.DynamoTestRecordset[1]['field_a'])
        self.assertEqual(response[1]['field_b'], _config.DynamoTestRecordset[1]['field_b'])

    def test_insert_record_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.insert_record', fake_insert_record)
        response = self.client.insert_record(_config.DynamoTestTablename, _config.DynamoTestRecord)
        self.assertTrue(response)

    def test_insert_record_batch_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.insert_record_batch', fake_insert_record_batch)
        response = self.client.insert_record_batch(_config.DynamoTestTablename, _config.DynamoTestRecordset)
        self.assertTrue(response)

    def test_read_table_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.read_table', fake_read_table)
        response = self.client.read_table(_config.DynamoTestTablename)
        self.assertEqual(response, '2010-11-01 15:31:10.123456-07:00')

    def test_update_record_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.update_record', fake_update_record)
        updateexpression = 'SET field_b = :val1'
        expressionattributevalues = {
            ':val1': 'Doh'
        }
        response = self.client.update_record(_config.DynamoTestTablename, _config.DynamoTestRecord, updateexpression, expressionattributevalues)
        self.assertTrue(response)












