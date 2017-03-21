from mock import patch
import tests.configtests as _config
from sharedlibs.tools_odm import ToolsODM
from unittest import TestCase

@staticmethod
def fake_convert_oracle_record_to_odm(record):
    return _config.ODMTestString

@staticmethod
def fake_read_file(filename):
    return _config.ODMTestString

@staticmethod
def fake_write_file(filename, text):
    return True


class TestODMUnit(TestCase):
    def create_patch(self, name, fakemethod):
        self.patcher = patch(name, fakemethod)
        thing = self.patcher.start()
        self.client = ToolsODM()
        self.addCleanup(self.patcher.stop)
        return thing

    def test_convert_oracle_record_to_odm(self):
        #this is doing a fake, but it should do the actual conversion
        self.create_patch('sharedlibs.tools_odm.ToolsODM.convert_oracle_record_to_odm',
                          fake_convert_oracle_record_to_odm)
        response = self.client.convert_oracle_record_to_odm(_config.OracleTestRecord)
        self.assertEqual(response, _config.ODMTestString)

    def test_read_file(self):
        self.create_patch('sharedlibs.tools_odm.ToolsODM.read_file', fake_read_file)
        response = self.client.read_file("testfile")
        self.assertEqual(response, _config.ODMTestString)

    def test_write_file(self):
        self.create_patch('sharedlibs.tools_odm.ToolsODM.write_file', fake_write_file)
        response = self.client.write_file("testfile", _config.ODMTestString)
        self.assertTrue(response, msg=response)













