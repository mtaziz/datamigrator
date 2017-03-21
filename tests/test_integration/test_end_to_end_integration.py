from sharedlibs.tools_dynamo import ToolsDynamo
from sharedlibs.tools_odm import ToolsODM
from sharedlibs.tools_oracle import ToolsOracle
import tests.configtests as _config
from unittest import TestCase


class TestEndToEnd(TestCase):
    def test_integration(self):
        sql = _config.OracleTestQueryOneRecord
        response = ToolsOracle().get_record(sql)
        self.fail(msg=response)

        # convert oracle record to odm
        # save the odm
        # verify the odm
        # delete the odm file

        # create the dynamo table from oracle
        # convert oracle record to dynamo
        # save the record on dynamo
        # verify the record on dynamo
        # delete the test dynamo table

