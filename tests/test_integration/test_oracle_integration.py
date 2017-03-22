from sharedlibs.tools_oracle import ToolsOracle
import tests.configtests as _config
from unittest import TestCase


class TestOracleIntegration(TestCase):
    def test_get_record(self):
        sql = _config.OracleTestQueryOneRecord
        response = ToolsOracle().get_record(sql)
        self.assertEquals(response['STUDYID'], 1, msg=response)
        self.assertEquals(response['PROJECTID'], 2, msg=response)
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
        self.assertEquals(response[0]['STUDYID'], 1, msg=response)
        self.assertEquals(response[1]['PROJECTID'], 3, msg=response)
        try:
            a = response[0]['FALSE DICT']
            self.fail(msg="did not fail false dict, but should have")
        except KeyError as k:
            pass
        except:
            self.fail(msg="Should fail false dict as key error")
