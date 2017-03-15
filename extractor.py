import sharedlibs.config as _config
import cx_Oracle


class Extractor:
    def extract_tester(self):

        dsn_tns = cx_Oracle.makedsn(_config.OracleIP, _config.OraclePort, service_name=_config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(_config.OracleUser, _config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_config.OracleTestQuery)
            for row in c:
                print row[0], "-", row[1]

            conn.close()
            return True
        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print x
            if x == "ORA-12541: TNS:no listener":
                print "run the following in the terminal, then try again"
                print "ssh -L " + _config.OraclePort + ":" + _config.OracleHost \
                     + ":" + _config.SSHPort + " -N " + _config.SSHHost
            return False

Extractor().extract_tester()