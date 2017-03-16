import config
import debug
import boto3

__author__ = 'scottbowers'


class ToolsDynamo(object):
    @staticmethod
    def create_table(_json):
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')

        # Create the DynamoDB table.
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='users')

        # Print out some data about the table.
        print(table.item_count)

        return True

    @staticmethod
    def delete_record(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        table.delete_item(
            Key={
                'username': 'janedoe',
                'last_name': 'Doe'
            }
        )
        return True

    @staticmethod
    def delete_table(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        table.delete()

    @staticmethod
    def get_record(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        response = table.get_item(
            Key={
                'username': 'janedoe',
                'last_name': 'Doe'
            }
        )
        item = response['Item']
        return item

    @staticmethod
    def get_recordset(_json):
        from boto3.dynamodb.conditions import Key, Attr
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        response = table.query(
            KeyConditionExpression=Key('username').eq('johndoe')
        )
        items = response['Items']
        return items

    @staticmethod
    def insert_record(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        table.put_item(
            Item={
                'username': 'janedoe',
                'first_name': 'Jane',
                'last_name': 'Doe',
                'age': 25,
                'account_type': 'standard_user',
            }
        )
        return True

    @staticmethod
    def insert_record_batch(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        with table.batch_writer() as batch:
            for i in range(50):
                batch.put_item(
                    Item={
                        'account_type': 'anonymous',
                        'username': 'user' + str(i),
                        'first_name': 'unknown',
                        'last_name': 'unknown'
                    }
                )
        return True

    @staticmethod
    def read_table():
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')

        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        table = dynamodb.Table('users')

        # Print out some data about the table.
        # This will cause a request to be made to DynamoDB and its attribute
        # values will be set based on the response.
        return table.creation_date_time

    @staticmethod
    def update_record(_json):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        table.update_item(
            Key={
                'username': 'janedoe',
                'last_name': 'Doe'
            },
            UpdateExpression='SET age = :val1',
            ExpressionAttributeValues={
                ':val1': 26
            }
        )
