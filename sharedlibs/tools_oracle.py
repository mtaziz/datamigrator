import sharedlibs.config as _config
import cx_Oracle

__author__ = 'sbowers'


class ToolsOracle(object):
    @staticmethod
    def get_record(_sql):
        dsn_tns = cx_Oracle.makedsn(_config.OracleIP, _config.OraclePort, service_name=_config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(_config.OracleUser, _config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_sql)

            #row = c.fetchone()
            columns = [i[0] for i in c.description]
            return [dict(zip(columns, row)) for row in c][0]
            #return row


        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print(x)
            if x == "ORA-12541: TNS:no listener":
                print("run the following in the terminal, then try again")
                print("ssh -L " + _config.OraclePort + ":" + _config.OracleHost \
                      + ":" + _config.SSHPort + " -N " + _config.SSHHost)
            return x
        finally:
            try:
                conn.close()
            except:
                pass


    @staticmethod
    def get_recordset(_sql):
        dsn_tns = cx_Oracle.makedsn(_config.OracleIP, _config.OraclePort, service_name=_config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(_config.OracleUser, _config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_sql)
            columns = [i[0] for i in c.description]
            return [dict(zip(columns, row)) for row in c]

        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print(x)
            if x == "ORA-12541: TNS:no listener":
                print("run the following in the terminal, then try again")
                print("ssh -L " + _config.OraclePort + ":" + _config.OracleHost \
                      + ":" + _config.SSHPort + " -N " + _config.SSHHost)
            return x
        finally:
            try:
                conn.close()
            except:
                pass


