from sharedlibs.tools_dynamo import ToolsDynamo

# run this to initialize a new dynamo instance.
########### WARNING!  Any existing of the tables herein will be wiped ##########################

keyschema = [
                {
                    'AttributeName': 'oid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'studyid',
                    'KeyType': 'RANGE'
                }
        ]

attributedefinitions = [
                {
                    'AttributeName': 'oid',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'studyid',
                    'AttributeType': 'N'
                },

        ]

provisionedthroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
        }

ToolsDynamo.delete_table("studies")
ToolsDynamo.create_table("studies", keyschema, attributedefinitions, provisionedthroughput)
