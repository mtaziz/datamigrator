DynamoTestAttributeDefinitions = [
                {
                    'AttributeName': 'field_a',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'field_b',
                    'AttributeType': 'S'
                },

        ]

DynamoTestKey = 'field_a'
DynamoTestKeyval = 'Doe'

DynamoTestKeySchema = [
                {
                    'AttributeName': 'field_a',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'field_b',
                    'KeyType': 'RANGE'
                }
        ]

DynamoTestProvisionedThroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
        }

DynamoTestQuery = {
                'field_a': 'Doe',
                'field_b': 'jane',
            }

DynamoTestQuery2 = {
                'field_a': 'Doe',
                'field_b': 'john',
            }

DynamoTestRecord = {
                'field_a': 'Doe',
                'field_b': 'jane',
                'info': [1, 2, 3]
            }

DynamoTestRecord2 = {
                'field_a': 'Doe',
                'field_b': 'john',
                'info': [4, 5, 6]
            }

DynamoTestRecordUpdated = {
                'field_a': 'Doe',
                'field_b': 'jane',
                'info': [7, 8, 9]
            }

DynamoTestRecordset = [
{
                'field_a': 'Doe',
                'field_b': 'jane',
                'info': [1, 2, 3]
            },
{
                'field_a': 'Doe',
                'field_b': 'john',
                'info': [4, 5, 6]
            }
]

DynamoTestTablename = "test"
DynamoTestUpdateExpression = "set info = :a"
DynamoTestUpdateExpressionAttributeValues = {
        ':a': [7, 8, 9]
    }

ODMTestFilename = "testfile"
ODMTestString = "<test>ing</test>"

OracleTestQueryOneRecord = "SELECT ENROLLMENTTARGET, UPDATE_DATE FROM RODS.STUDIES WHERE rownum=1 "
OracleTestQueryRecordset = "SELECT ENROLLMENTTARGET, UPDATE_DATE FROM RODS.STUDIES WHERE rownum < 25 "
OracleTestRecord = {"ENROLLMENTTARGET": "eta", "UPDATE_DATE": "123"}
OracleTestRecordset = [{"ENROLLMENTTARGET": "eta", "UPDATE_DATE": "123"}, {"ENROLLMENTTARGET": "etb", "UPDATE_DATE": "123"}]