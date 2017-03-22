from mock import patch
import tests.configtests as _config
from sharedlibs.tools_oracle import ToolsOracle
from unittest import TestCase


@staticmethod
def fake_get_record(sql):
    return _config.OracleTestRecord

@staticmethod
def fake_get_recordset(sql):
    return _config.OracleTestRecordset


class TestOracleUnit(TestCase):
    def create_patch(self, name, fakemethod):
        self.patcher = patch(name, fakemethod)
        thing = self.patcher.start()
        self.client = ToolsOracle()
        self.addCleanup(self.patcher.stop)
        return thing

    def test_get_record_mock(self):
        self.create_patch('sharedlibs.tools_oracle.ToolsOracle.get_record', fake_get_record)
        sql = _config.OracleTestQueryOneRecord
        response = self.client.get_record(sql)
        self.assertIn('STUDYID', response)
        self.assertEqual(response['STUDYID'], 1)

    def test_get_recordset_mock(self):
        self.create_patch('sharedlibs.tools_oracle.ToolsOracle.get_recordset', fake_get_recordset)
        sql = _config.OracleTestQueryRecordset
        response = self.client.get_recordset(sql)
        self.assertIn(_config.OracleTestRecordset[0], response)
        self.assertEqual(response[0]['STUDYID'], _config.OracleTestRecordset[0]['STUDYID'])
        self.assertEqual(response[1]['PROJECTID'], _config.OracleTestRecordset[1]['PROJECTID'])












