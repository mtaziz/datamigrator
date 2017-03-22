import sharedlibs.config as _config
import tests.configtests as _configtests
from sharedlibs.tools_dynamo import ToolsDynamo
from sharedlibs.tools_oracle import ToolsOracle
from sharedlibs.tools_odm import ToolsODM

oracleret = ToolsOracle().get_record(_configtests.OracleTestQueryOneRecord)

print("ORACLE RECORD")
print(oracleret)
print(str(oracleret['CREATED']))

#ret = ToolsOracle().get_recordset(_configtests.OracleTestQueryRecordset)
#print("ORACLE RECORDSET")
#print(ret)

odmret = ToolsODM().convert_oracle_record_to_odm(oracleret)
print("ODM RECORD")
print(odmret)
ToolsODM().write_file('test', odmret)

# odmret should be saved to the ODM file system
# _tools_odm.ToolsODM().write_file("STUDY_" + str(ret['STUDYID'), odmret)

dynamoret = ToolsDynamo.convert_oracle_record_to_dynamo(oracleret)
print("DYNAMO RECORD")
print(dynamoret)






