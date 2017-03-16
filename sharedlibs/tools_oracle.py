import config
import cx_Oracle
import debug

__author__ = 'sbowers'


class ToolsOracle(object):
    @staticmethod
    def get_recordset(_sql):
        #debug.debug("oracle_get_recordset BEGIN")
        dsn_tns = cx_Oracle.makedsn(config.OracleIP, config.OraclePort, service_name=config.OracleDatabase)

        try:
            conn = cx_Oracle.connect(config.OracleUser, config.OraclePassword, dsn_tns)
            c = conn.cursor()
            c.execute(_sql)

            # just printing out some sample values for now...
            # we will want to return this recordset to the caller instead.
            for row in c:
                print row[0], "-", row[1]

            conn.close()
            return True
        except cx_Oracle.DatabaseError as x:
            x = str(x).strip()
            print x
            if x == "ORA-12541: TNS:no listener":
                print "run the following in the terminal, then try again"
                print "ssh -L " + config.OraclePort + ":" + config.OracleHost \
                      + ":" + config.SSHPort + " -N " + config.SSHHost
            return False

        #debug.debug_timer("oracle_get_recordset_timer", time.time() - t)

        return True
