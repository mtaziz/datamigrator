import ConfigParser
import os.path

__author__ = 'sbowers'


def config_section_map(section):
    config = ConfigParser.ConfigParser()
    config.read(os.path.dirname(os.path.dirname(__file__)) + "/_config.ini")
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                pass
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


cHEADER = '\033[95m'
cOKBLUE = '\033[94m'
cOKGREEN = '\033[92m'
cWARNING = '\033[93m'
cFAIL = '\033[91m'
cENDC = '\033[0m'
cBOLD = '\033[1m'
cUNDERLINE = '\033[4m'

cDebug = config_section_map("environment")['debug'] == "True"

DynamoHost = config_section_map("dynamo")["host"]
DynamoUser = config_section_map("dynamo")["username"]
DynamoPassword = config_section_map("dynamo")["password"]
DynamoTestPost = config_section_map("dynamo")["testpost"]

OracleDatabase = config_section_map("oracle")["database"]
OracleHost = config_section_map("oracle")["host"]
OracleIP = config_section_map("oracle")["ip"]
OraclePassword = config_section_map("oracle")["password"]
OraclePort = config_section_map("oracle")["port"]
OracleTestQuery = config_section_map("oracle")["testquery"]
OracleUser = config_section_map("oracle")["username"]

SSHHost = config_section_map("ssh")["host"]
SSHPort = config_section_map("ssh")["port"]
















