from sharedlibs.tools_oracle import ToolsOracle
import tests.configtests as _config
from unittest import TestCase


class TestOracleIntegration(TestCase):
    def test_get_record(self):
        sql = _config.OracleTestQueryOneRecord
        response = ToolsOracle().get_record(sql)
        self.assertNotEquals(response['ENROLLMENTTARGET'], '', msg=response)
        self.assertNotEquals(response['UPDATE_DATE'], '', msg=response)
        try:
            a = response['FALSE DICT']
            self.fail(msg="did not fail false dict, but should have")
        except KeyError as k:
            pass
        except:
            self.fail(msg="Should fail false dict as key error")

    def test_get_recordset(self):
        sql = _config.OracleTestQueryRecordset
        response = ToolsOracle.get_recordset(sql)
        self.assertNotEquals(response[0]['ENROLLMENTTARGET'], '', msg=response)
        self.assertNotEquals(response[0]['UPDATE_DATE'], '', msg=response)
        try:
            a = response[0]['FALSE DICT']
            self.fail(msg="did not fail false dict, but should have")
        except KeyError as k:
            pass
        except:
            self.fail(msg="Should fail false dict as key error")
