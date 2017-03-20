import sharedlibs.config as _config
import sharedlibs.tools_dynamo as _tools_dynamo

# STUB FOR THE LOADING INTO DYNAMO

class Loader(object):
    @staticmethod
    def loader_read_table_tester(table):
        return _tools_dynamo.ToolsDynamo().read_table(table)


print(Loader.loader_tester("test"))


