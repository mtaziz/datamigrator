import sharedlibs.config as _config
import sharedlibs.tools_oracle as _tools_oracle


class Extractor(object):
    @staticmethod
    def extract_tester(_sql):
        return _tools_oracle.ToolsOracle().get_recordset(_sql)


Extractor.extract_tester(_config.OracleTestQuery)