import boto3

__author__ = 'scottbowers'


class ToolsDynamo(object):
    @staticmethod
    def convert_oracle_record_to_dynamo(record):
        ret = {}
        ret['oid'] = str(record['O_ID'])
        ret['studyid'] = record['STUDYID']
        info = {}
        info['created'] = str(record['CREATED']).replace(' ', 'T')
        ret['info'] = info

        return ret

    @staticmethod
    def create_table(tablename, keyschema, attributedefinitions, provisionedthroughput):
        dynamodb = boto3.resource('dynamodb')
        try:
            table = dynamodb.create_table(
                TableName=tablename,
                KeySchema=keyschema,
                AttributeDefinitions=attributedefinitions,
                ProvisionedThroughput=provisionedthroughput
            )

            # Wait until the table exists.
            table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

            # Print out some data about the table.
            #print(table.item_count)
            return True
        except:
            return False

    @staticmethod
    def delete_record(tablename, key):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tablename)
        table.delete_item(
            Key=key
        )
        return True

    @staticmethod
    def delete_table(tablename):
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(tablename)
            table.delete()
            #wait for the table to be gone
            table.meta.client.get_waiter('table_not_exists').wait(TableName=tablename)
            return True
        except:
            return False

    @staticmethod
    def get_record(tablename, key):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tablename)
        response = table.get_item(
            Key=key
        )
        item = response['Item']
        return item

    @staticmethod
    def get_recordset(tablename, key, keyval):
        from boto3.dynamodb.conditions import Key, Attr
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tablename)
        response = table.query(
            KeyConditionExpression=Key(key).eq(keyval)
        )
        items = response['Items']
        return items

    @staticmethod
    def insert_record(tablename, item):
        dynamodb = boto3.resource('dynamodb')
        try:
            table = dynamodb.Table(tablename)
            table.put_item(
                Item=item
            )
            return True
        except:
            return False

    @staticmethod
    def insert_record_batch(tablename, itemlist):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tablename)
        with table.batch_writer() as batch:
            for i in itemlist.count:
                batch.put_item(
                    Item=itemlist[i]
                )
        return True

    @staticmethod
    def read_table(tablename):
        dynamodb = boto3.resource('dynamodb')
        try:
            table = dynamodb.Table(tablename)
            return table.creation_date_time
        except:
            return False

    @staticmethod
    def update_record(tablename, key, updateexpression, expressionattributevalues):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(tablename)
        table.update_item(
            Key=key,
            UpdateExpression=updateexpression,
            ExpressionAttributeValues=expressionattributevalues
        )
        return True
