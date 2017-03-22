import tests.configtests as _config
from mock import patch
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


class TestDynamoUnit(TestCase):
    def create_patch(self, name, fakemethod):
        self.patcher = patch(name, fakemethod)
        thing = self.patcher.start()
        self.client = ToolsDynamo()
        self.addCleanup(self.patcher.stop)
        return thing

    def test_convert_oracle_record_to_dynamo(self):
        response = ToolsDynamo.convert_oracle_record_to_dynamo(_config.OracleTestRecord)
        self.assertEqual(_config.DynamoTestRecord, response)

    def test_create_table_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.create_table', fake_create_table)
        response = self.client.create_table(_config.DynamoTestTablename, _config.DynamoTestKeySchema,
                                            _config.DynamoTestAttributeDefinitions,
                                            _config.DynamoTestProvisionedThroughput)
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
        self.assertIn('oid', response)
        self.assertEqual(response['oid'], _config.DynamoTestRecord['oid'])
        self.assertEqual(response['oid'], _config.DynamoTestRecord['oid'])

    def test_get_recordset_mock(self):
        self.create_patch('sharedlibs.tools_dynamo.ToolsDynamo.get_recordset', fake_get_recordset)
        response = self.client.get_recordset(_config.DynamoTestTablename, _config.DynamoTestKey,
                                             _config.DynamoTestKeyval)
        self.assertIn(_config.DynamoTestRecord, response)
        self.assertEqual(response[0]['oid'], _config.DynamoTestRecordset[0]['oid'])
        self.assertEqual(response[1]['oid'], _config.DynamoTestRecordset[1]['oid'])
        self.assertEqual(response[1]['oid'], _config.DynamoTestRecordset[1]['oid'])

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
        updateexpression = _config.DynamoTestUpdateExpression
        expressionattributevalues = _config.DynamoTestUpdateExpressionAttributeValues
        response = self.client.update_record(_config.DynamoTestTablename, _config.DynamoTestRecord,
                                             updateexpression, expressionattributevalues)
        self.assertTrue(response)












