import sharedlibs.config as _config
import sharedlibs.tools_oracle as _tools_oracle

# STUB FOR THE RUNNING OF THE DATABASE PULLER

class Extractor(object):
    @staticmethod
    def extract_test(_sql):
        print(_tools_oracle.ToolsOracle().get_recordset(_sql))


print(_config.OracleTestQuery)
Extractor.extract_test(_config.OracleTestQuery)