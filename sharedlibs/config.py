import configparser
import os.path

__author__ = 'sbowers'


def config_section_map(section):
    config = configparser.ConfigParser()
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

OracleDatabase = config_section_map("oracle")["database"]
OracleHost = config_section_map("oracle")["host"]
OracleIP = config_section_map("oracle")["ip"]
OraclePassword = config_section_map("oracle")["password"]
OraclePort = config_section_map("oracle")["port"]
OracleUser = config_section_map("oracle")["username"]

SSHHost = config_section_map("ssh")["host"]
SSHPort = config_section_map("ssh")["port"]
















