import tests.configtests as _config
from sharedlibs.tools_dynamo import ToolsDynamo
from unittest import TestCase


class TestDynamoIntegration(TestCase):
    def test_integration(self):
        #initialization, delete the test table if it exists
        ToolsDynamo.delete_table(_config.DynamoTestTablename)

        #make sure the table is not there
        ret = ToolsDynamo.read_table(_config.DynamoTestTablename)
        self.assertFalse(ret, msg=ret)

        # create the table
        ret = ToolsDynamo.create_table(_config.DynamoTestTablename, _config.DynamoTestKeySchema,
                                       _config.DynamoTestAttributeDefinitions, _config.DynamoTestProvisionedThroughput)
        self.assertTrue(ret, msg=ret)

        # insert a record into the table
        ret = ToolsDynamo.insert_record(_config.DynamoTestTablename, _config.DynamoTestRecord)
        self.assertTrue(ret, msg=ret)

        # verify the record
        ret = ToolsDynamo.get_record(_config.DynamoTestTablename, _config.DynamoTestQuery)
        self.assertEqual(ret, _config.DynamoTestRecord, msg=ret)

        # insert a second record into the table
        ret = ToolsDynamo.insert_record(_config.DynamoTestTablename, _config.DynamoTestRecord2)
        self.assertTrue(ret, msg=ret)

        # verify the second record
        ret = ToolsDynamo.get_record(_config.DynamoTestTablename, _config.DynamoTestQuery2)
        self.assertEqual(ret, _config.DynamoTestRecord2, msg=ret)

        # verify the recordset
        ret = ToolsDynamo.get_recordset(_config.DynamoTestTablename, _config.DynamoTestKey, _config.DynamoTestKeyval)
        self.assertEqual(ret, _config.DynamoTestRecordset, msg=ret)

        # update a record
        ret = ToolsDynamo.update_record(_config.DynamoTestTablename, _config.DynamoTestQuery,
                                        _config.DynamoTestUpdateExpression,
                                        _config.DynamoTestUpdateExpressionAttributeValues)
        self.assertTrue(ret, "failed on update")

        # verify the updated record
        ret = ToolsDynamo.get_record(_config.DynamoTestTablename, _config.DynamoTestQuery)
        self.assertEqual(ret, _config.DynamoTestRecordUpdated, msg=ret)

        #cleanup, delete the test table
        ToolsDynamo.delete_table(_config.DynamoTestTablename)