import sharedlibs.config as _config
import cx_Oracle

__author__ = 'sbowers'


class ToolsOracle(object):
    @staticmethod
    def get_record(_sql):
        # returning one record
        dsn_tns = cx_Oracle.makedsn(_config.OracleIP, _config.OraclePort, service_name=_config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(_config.OracleUser, _config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_sql)

            # just printing out some sample values for now...
            for row in c:
                print(row[0], "-", row[1])

            conn.close()
            return True
        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print(x)
            if x == "ORA-12541: TNS:no listener":
                print("run the following in the terminal, then try again")
                print("ssh -L " + _config.OraclePort + ":" + _config.OracleHost \
                      + ":" + _config.SSHPort + " -N " + _config.SSHHost)
            return False

    @staticmethod
    def get_recordset(_sql):
        # debug.debug("oracle_get_recordset BEGIN")
        dsn_tns = cx_Oracle.makedsn(_config.OracleIP, _config.OraclePort, service_name=_config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(_config.OracleUser, _config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_sql)

            # just printing out some sample values for now...
            # we will want to return this recordset to the caller instead.
            for row in c:
                print(row[0], "-", row[1])

            conn.close()
            return True
        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print(x)
            if x == "ORA-12541: TNS:no listener":
                print("run the following in the terminal, then try again")
                print("ssh -L " + _config.OraclePort + ":" + _config.OracleHost \
                      + ":" + _config.SSHPort + " -N " + _config.SSHHost)
            return False

        # debug.debug_timer("oracle_get_recordset_timer", time.time() - t)
