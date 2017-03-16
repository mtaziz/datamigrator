import sharedlibs.config as _config
import sharedlibs.tools_dynamo as _tools_dynamo


class Loader(object):
    @staticmethod
    def loader_tester(_json):
        return _tools_dynamo.ToolsDynamo().create_table(_json)
        #return _tools_dynamo.ToolsDynamo().dynamo_insert_record(_json)


Loader.loader_tester(_config.DynamoTestPost)


