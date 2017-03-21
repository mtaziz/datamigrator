#Datamigrator

The datamigrator folder represents code that can be used to read data from an external Oracle database.
The intent is the extract the data, transform it, and then load into a DynamoDB instance on AWS.  The code is written based on the native 
Python 2.7 pre-installed on the Mac.

##Development Environment

###DynamoDB
DynamoDB can be run locally on the Mac
1. Download the latest DynamoDB from AWS Website http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html

2. Unzip the downloaded files, and place them into the desired directory.

3. In the terminal, run the following against the diretory<br>

        java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
        
4. enter your keys using the following command
        
        aws configure

###Oracle

There are a number of steps necessary to set up the oracle environment on the mac.
1. Download the Oracle Client from Oracle website http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html
- instantclient-basic-macos.x64-12.1.0.2.0.zip
- instantclient-sdk-macos.x64-12.1.0.2.0.zip

2. Unzip the downloaded files, and place them into the desired directory.

3. In the terminal, create a shortcut for later use in that directory<br>
        
        ln -s libclntsh.dylib.12.1 libclntsh.dylib

4. Modify your .bash_profile

        *Tell cx_Oracle setup.py where to find instantclient libs*
        export ORACLE_HOME=/usr/local/opt/instantclient_12_1
        *Set -rpath option to tell gcc to look in ORACLE_HOME when linking*
        export FORCE_RPATH=1

5. Download and install Oracle<br>

        pip install cx_Oracle

6. Verify install

        python -c "import cx_Oracle"
    
7. If the following step fails then you may see the following exception:

        Traceback (most recent call last):
        File "<string>", line 1, in <module>
        ImportError: dlopen(/Library/Python/2.7/site-packages/cx_Oracle.so, 2): Library not loaded: @rpath/libclntsh.dylib.12.1
        Referenced from: /Library/Python/2.7/site-packages/cx_Oracle.so
        Reason: image not found
        If you are seeing this exception, you either skipped 
        setting ORACLE_HOME and FORCE_RPATH (as described above), 
        or you are using a cached version of the cx_Oracle build 
        when installing. <br><br>
        
8. To force pip to re-build the package, run the following:
  
         pip install --no-cache-dir --allow-external --allow-unverified cx_oracle
  

##Files
###root directory
- .gitignore: Files and directories to be excluded from repository
- _config.ini: Configuration variables
- extractor.py: Extract data from OracleDB Stub
- loader.py: Loads data into Dynamo DB Stub
- readme.md: Documentation

###files
- default: the default file ensures that this file store is created when packaging

###sharedlibs
- __init__.py: initialization to create package
- config.py: loads configuration from _config.ini file
- tools_dynamo.py: interface with DynamoDB
- tools_odm.py: interface with ODM
- tools_oracle: interface with OracleDB

###tests
- __init__.py: initialization to create package
- configtests.py: variables used for testing

####test_integration
- test_odm_integration.py: Tests read/write to actual file system
- test_oracle_integration.py: Tests a read from actual OracleDB
- test_dynamo_integration.py: Tests communication with actual DynamoDB

####test_unit
- test_dependencies.py: unit testing that dependencies are installed correctly
- test_dynamo_unit.py: Mock testing of DynamoDB 
- test_odm_unit.py: Mock testing of ODM
- test_oracle_unit.py Mock testing of OracleDB

##Packages
the following package dependencies need to be installed via pip3 or other
- awscli: handles keys for aws/Dynamo connection
- boto3: communication with DynamoDB
- configparser: _config.ini handling
- cx_Oracle: communication with the OracleDB
- mock: used for mocking unittests
- nose: used for mock unittests
- requests: http library, may not be necessary