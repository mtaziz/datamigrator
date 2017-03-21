from sharedlibs.tools_odm import ToolsODM
import tests.configtests as _config
from unittest import TestCase


class TestODMIntegration(TestCase):
    def test_integration(self):
        # write a test file
        ret = ToolsODM.write_file(_config.ODMTestFilename, _config.ODMTestString)
        self.assertTrue(ret, msg="write file failed")

        # read from the test file
        ret = ToolsODM.read_file(_config.ODMTestFilename)
        self.assertEqual(ret, _config.ODMTestString, msg=ret)

        # cleanup
        ret = ToolsODM.delete_file(_config.ODMTestFilename)
        self.assertTrue(ret)
