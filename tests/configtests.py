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

DynamoTestRecord = {
                'field_a': 'janedoe',
                'field_b': 'Doe'
            }
DynamoTestRecordset = [
{
                'field_a': 'janedoe',
                'field_b': 'Doe'
            },
{
                'field_a': 'johndoe',
                'field_b': 'Doe'
            }
]
DynamoTestTablename = "test"

OracleTestQueryOneRecord = "SELECT ENROLLMENTTARGET, UPDATE_DATE FROM RODS.STUDIES WHERE rownum=1 "
OracleTestQueryRecordset = "SELECT ENROLLMENTTARGET, UPDATE_DATE FROM RODS.STUDIES WHERE rownum < 25 "
OracleTestRecord = {"ENROLLMENTTARGET": "eta", "UPDATE_DATE": "123"}
OracleTestRecordset = [{"ENROLLMENTTARGET": "eta", "UPDATE_DATE": "123"}, {"ENROLLMENTTARGET": "etb", "UPDATE_DATE": "123"}]