import sharedlibs.config as _config
import os

__author__ = 'sbowers'


class ToolsODM(object):
    @staticmethod
    def convert_oracle_record_to_odm(record):
        ret = "string of odm generated from oracle record"
        return ret

    @staticmethod
    def delete_file(filename):
        os.remove(_config.ODMPath + filename)
        return True

    @staticmethod
    def read_file(filename):
        f = open(_config.ODMPath + filename, 'r')
        ret = f.read()
        f.close()
        return ret

    @staticmethod
    def write_file(filename, text):
        f = open(_config.ODMPath + filename, 'w')
        f.write(text)
        f.close()
        return True



