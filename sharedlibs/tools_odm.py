import sharedlibs.config as _config
from xml.dom import minidom
import os

__author__ = 'sbowers'


class ToolsODM(object):
    @staticmethod
    def convert_oracle_record_to_odm(record):
        doc = minidom.Document()

        #XXXXXXXXXX ROOT node XXXXXXXXXX#
        odm = doc.createElement('ODM')
        odm.setAttribute('xmlns', 'http://www.cdisc.org/ns/odm/v1.3')
        odm.setAttribute('xmlns:ns2', 'http://www.w3.org/2000/09/xmldsig#')
        odm.setAttribute('FileType', 'Snapshot')
        odm.setAttribute('Granularity', 'All')
        odm.setAttribute('FileOID', 'SomeFileOID')
        odm.setAttribute('CreationDateTime', str(record['CREATED']).replace(' ', 'T'))
        odm.setAttribute('PriorFileOID', 'SomePriorFileOID')

        #++++++++++ Study node ++++++++++#
        study = doc.createElement('Study')
        study.setAttribute('OID', str(record['O_ID']))

        # Begin GlobalVariables Node
        globalvariables = doc.createElement('GlobalVariables')
        # Begin StudyName
        studyname = doc.createElement('StudyName')
        text = doc.createTextNode('SomeStudyName')
        studyname.appendChild(text)
        globalvariables.appendChild(studyname)
        # End StudyName
        # Begin StudyDescription
        studydescription = doc.createElement('StudyDescription')
        text = doc.createTextNode('SomeStudyDescription')
        studydescription.appendChild(text)
        globalvariables.appendChild(studydescription)
        # End StudyDescription
        # Begin ProtocolName
        protocolname = doc.createElement('ProtocolName')
        text = doc.createTextNode('SomeProtocolName')
        protocolname.appendChild(text)
        globalvariables.appendChild(protocolname)
        # End ProtocolName
        study.appendChild(globalvariables)
        # End GlobalVariables Node

        # BasicDefinitions Node
        basicdefinitions = doc.createElement('BasicDefinitions')
        # MeasurementUnit Node
        # for each measurementunit
        measurementunit = doc.createElement('MeasurementUnit')
        measurementunit.setAttribute('OID', "MU.KG")
        measurementunit.setAttribute('Name', "Kilogram")
        # Begin Symbol
        symbol = doc.createElement('Symbol')
        translatedtext = doc.createElement('TranslatedText')
        symbol.appendChild(translatedtext)
        measurementunit.appendChild(symbol)
        # End Symbol
        basicdefinitions.appendChild(measurementunit)
        # next MeasurementUnit
        # End MeasurementUnit Nodes
        study.appendChild(basicdefinitions)
        # End BasicDefinitions

        # MetaDataVersion Node
        metadataversion = doc.createElement('MetaDataVersion')
        metadataversion.setAttribute('OID', 'v1.01')
        metadataversion.setAttribute('Name', 'Version 1.01')
        # Begin Include Node
        include = doc.createElement('Include')
        include.setAttribute('StudyOID', '123-456-789')
        include.setAttribute('MetaDataVersionOID', 'v1.00')
        metadataversion.appendChild(include)
        # End Include Node

        # Protocol Node
        protocol = doc.createElement('Protocol')
        # Begin StudyEventRef Nodes
        # for each studyeventref
        studyeventref = doc.createElement('StudyEventRef')
        studyeventref.setAttribute('StudyEventOID', 'SE.VISIT0')
        studyeventref.setAttribute('OrderNumber', '1')
        studyeventref.setAttribute('Mandatory', 'Yes')
        protocol.appendChild(studyeventref)
        # next StudyEventRef
        # End StudyEventRef Nodes
        metadataversion.appendChild(protocol)
        # End Protocol Node

        # StudyEventDef Nodes
        # for each StudyEventDef
        studyeventdef = doc.createElement('StudyEventDef')
        studyeventdef.setAttribute('OID', 'SE.VISIT0')
        studyeventdef.setAttribute('Name', 'Pre-treatment')
        studyeventdef.setAttribute('Repeating', 'No')
        studyeventdef.setAttribute('Type', 'Scheduled')
        studyeventdef.setAttribute('Category', 'PreTreatment')
        # Begin FormRef Nodes
        # for each FormRef
        formref = doc.createElement('FormRef')
        formref.setAttribute('FormOID', 'FORM.DEMOG')
        formref.setAttribute('OrderNumber', '1')
        formref.setAttribute('Mandatory', 'No')
        studyeventdef.appendChild(formref)
        # next FormRef
        # End FormRef Nodes
        metadataversion.appendChild(studyeventdef)
        # next StudyEventDef
        # End StudyEventDef Nodes
        # Begin FormDef Nodes
        # for each FormDef
        formdef = doc.createElement('FormDef')
        formdef.setAttribute('OID', 'FORM.AE')
        formdef.setAttribute('Name', 'Adverse Events')
        formdef.setAttribute('Repeating', 'No')
        # Begin ItemGroupRef Node
        itemgroupref = doc.createElement('ItemGroupRef')
        itemgroupref.setAttribute('ItemGroupOID', 'IG.AE')
        itemgroupref.setAttribute('OrderNumber', '1')
        itemgroupref.setAttribute('Mandatory', 'No')
        formdef.appendChild(itemgroupref)
        # End ItemGroupRef Node
        metadataversion.appendChild(formdef)
        # next FormDef
        # End FormDef Nodes
        # Begin ItemGroupDef Nodes
        # for each ItemGroupDef
        itemgroupdef = doc.createElement('ItemGroupDef')
        itemgroupdef.setAttribute('OID', 'IG.AE')
        itemgroupdef.setAttribute('Name', 'Adverse Events')
        itemgroupdef.setAttribute('Repeating', 'Yes')
        itemgroupdef.setAttribute('IsReferenceData', 'No')
        itemgroupdef.setAttribute('SASDatasetName', 'AE')
        itemgroupdef.setAttribute('Domain', 'AE Domain')
        itemgroupdef.setAttribute('Origin', 'AE Origin')
        itemgroupdef.setAttribute('Role', 'AE Role')
        itemgroupdef.setAttribute('Comment', 'AE Comment')
        # Begin ItemRef Nodes
        # for each ItemRef
        itemref = doc.createElement('ItemRef')
        itemref.setAttribute('ItemOID','IT.REC_ID')
        itemref.setAttribute('OrderNumber','1')
        itemref.setAttribute('Mandatory','No')
        itemgroupdef.appendChild(itemref)
        # next ItemRef
        metadataversion.appendChild(itemgroupdef)
        # next ItemGroupDef
        # End ItemGroupDef Nodes
        # Begin ItemDef Nodes
        # for each ItemDef
        itemdef = doc.createElement('ItemDef')
        itemdef.setAttribute('OID','IT.ABNORM')
        itemdef.setAttribute('Name','Normal/Abnormal/Not Done')
        itemdef.setAttribute('DataType','integer')
        itemdef.setAttribute('Length','2')
        itemdef.setAttribute('SignificantDigits','1')
        itemdef.setAttribute('SASFieldName','ABNORM')
        itemdef.setAttribute('Origin','ABNORM Origin')
        itemdef.setAttribute('Comment','ABNORM Comment')
        # Begin Question Node
        question = doc.createElement('Question')
        # Begin TranslatedText Nodes
        # for each TranslatedText
        translatedtext = doc.createElement('TranslatedText')
        translatedtext.setAttribute('xml:lang', 'en')
        text = doc.createTextNode('English: Normal/Abnormal/Not Done?')
        translatedtext.appendChild(text)
        question.appendChild(translatedtext)
        # next TranslatedText
        # End TranslatedText
        itemdef.appendChild(question)
        # End Question Node
        # Begin ExternalQuestion Node
        externalquestion = doc.createElement('ExternalQuestion')
        externalquestion.setAttribute('Dictionary', 'Websters')
        externalquestion.setAttribute('Version', '2001 Unabridged')
        externalquestion.setAttribute('Code', 'NormAbnormNotDone')
        itemdef.appendChild(externalquestion)
        # End ExternalQuestion Node
        # Begin MeasurementUnitRef
        # for each MeasurementUnitRef
        measurementunitref = doc.createElement('MeasurementUnitRef')
        measurementunitref.setAttribute('MeasurementUnitOID', 'NU.DPML')
        itemdef.appendChild(measurementunitref)
        # next MeasurementUnitRef
        # End MeasurementUnitRef
        # Begin RangeCheck Nodes
        # for each RangeCheck
        rangecheck = doc.createElement('RangeCheck')
        rangecheck.setAttribute('Comparator', 'LT')
        rangecheck.setAttribute('SoftHard', 'Hard')
        # Begin CheckValue Node
        checkvalue = doc.createElement('CheckValue')
        text = doc.createTextNode('1')
        checkvalue.appendChild(text)
        rangecheck.appendChild(checkvalue)
        # End CheckValue Node
        # Begin MeasurementUnitRef Node
        measurementunitref = doc.createElement('MeasurementUnitRef')
        measurementunitref.setAttribute('MeasurementUnitOID', 'MU.DPML')
        rangecheck.appendChild(measurementunitref)
        # End MeasurementUnitRef Node
        # Begin ErrorMessage Node
        errormessage = doc.createElement('ErrorMessage')
        # Begin TranslatedText Nodes
        # for each TranslatedText
        translatedtext = doc.createElement('TranslatedText')
        translatedtext.setAttribute('xml:lang', 'en')
        text = doc.createTextNode('English: Normal/Abnormal/Not Done?')
        translatedtext.appendChild(text)
        errormessage.appendChild(translatedtext)
        # next TranslatedText
        #End TranslatedText Nodes
        rangecheck.appendChild(errormessage)
        # End ErrorMessage Node
        itemdef.appendChild(rangecheck)
        # next RangeCheck
        # End RangeCheck Nodes
        # Begin CodeListRef Node
        codelistref = doc.createElement('CodeListRef')
        codelistref.setAttribute('CodeListOID', 'CL.N_A_ND')
        itemdef.appendChild(codelistref)
        # End CodeListRef
        # Begin Role Node
        role = doc.createElement('Role')
        text = doc.createTextNode('ABNORM Role')
        role.appendChild(text)
        itemdef.appendChild(role)
        # End Role Node
        metadataversion.appendChild(itemdef)
        # next itemdef
        # End ItemDef nodes
        # Begin CodeList Nodes
        # for each CodeList
        codelist = doc.createElement('CodeList')
        codelist.setAttribute('OID', 'CL.AEACTTR')
        codelist.setAttribute('Name', 'AE Action Taken, Study Drug')
        codelist.setAttribute('DataType', 'text')
        codelist.setAttribute('SASFormatName', 'AEACTTR')
        # Begin CodeListItem Nodes
        # for each CodeListItem
        codelistitem = doc.createElement('CodeListItem')
        codelistitem.setAttribute('CodedValue', '0')
        # Begin Decode Node
        decode = doc.createElement('Decode')
        # Begin TranslatedText Nodes
        # for each TranslatedText
        translatedtext = doc.createElement('TranslatedText')
        translatedtext.setAttribute('xml:lang', 'en')
        text = doc.createTextNode('English: Normal/Abnormal/Not Done?')
        translatedtext.appendChild(text)
        decode.appendChild(translatedtext)
        # next TranslatedText
        # End Translated Text
        codelistitem.appendChild(decode)
        # End Decode
        codelist.appendChild(codelistitem)
        # next CodeListItem
        # End CodeListItem
        metadataversion.appendChild(codelist)
        # next CodeList
        # End CodeList
        # Begin Presentation Nodes
        # for each Presention
        presentation = doc.createElement('Presentation')
        presentation.setAttribute('OID', 'PRS.EN')
        presentation.setAttribute('xml: lang', 'en')
        text = doc.createTextNode('English')
        presentation.appendChild(text)
        metadataversion.appendChild(presentation)
        # next Presentation
        # End Presentation
        study.appendChild(metadataversion)
        # End MetaDataVersion Node

        odm.appendChild(study)
        #++++++++++ End Study ++++++++++#

        #++++++++++ Begin AdminData Node ++++++++++#
        admindata = doc.createElement('AdminData')
        admindata.setAttribute('StudyOID', '123-456-789')
        # Begin User Nodes
        # for each User
        user = doc.createElement('User')
        user.setAttribute('OID', 'USR.cdisc001')
        # Begin FullName
        fullname = doc.createElement('FullName')
        text = doc.createTextNode('Shirley Williams')
        fullname.appendChild(text)
        user.appendChild(fullname)
        # End FullName
        # Begin FirstName
        firstname = doc.createElement('FirstName')
        text = doc.createTextNode('Shirley')
        firstname.appendChild(text)
        user.appendChild(firstname)
        # End FirstName
        # Begin LastName
        lastname = doc.createElement('LastName')
        text = doc.createTextNode('Williams')
        lastname.appendChild(text)
        user.appendChild(lastname)
        # End LastName
        # Begin Organization
        organization = doc.createElement('Organization')
        text = doc.createTextNode('CDISC')
        organization.appendChild(text)
        user.appendChild(organization)
        # End Organization
        # Begin LocationRef
        locationref = doc.createElement('LocationRef')
        locationref.setAttribute('LocationOID', 'LOC.CDISCHome')
        user.appendChild(locationref)
        # End LocationRef
        admindata.appendChild(user)
        # next User
        # End User
        # Begin Location
        # for each Location
        location = doc.createElement('Location')
        location.setAttribute('OID', 'LOC.site002')
        location.setAttribute('Name', 'Roswell Park')
        location.setAttribute('LocationType', 'Site')
        # Begin MetaDataVersionRef
        metadataversionref = doc.createElement('MetaDataVersionRef')
        metadataversionref.setAttribute('StudyOID', '123-456-789')
        metadataversionref.setAttribute('MetaDataVersionOID', 'v1.01')
        metadataversionref.setAttribute('EffectiveDate', '20011019T10:45:57-05:00')
        location.appendChild(metadataversionref)
        # End MetaDataVersionRef
        admindata.appendChild(location)
        # next Location
        # End Location
        # Begin SignatureDef
        signaturedef = doc.createElement('SignatureDef')
        signaturedef.setAttribute('OID', 'SD.cdisc001-es')
        signaturedef.setAttribute('Methodology', 'Electronic')
        # Begin Meaning
        meaning = doc.createElement('Meaning')
        text = doc.createTextNode('Signature')
        meaning.appendChild(text)
        signaturedef.appendChild(meaning)
        # End Meaning
        # Begin LegalReason
        legalreason = doc.createElement('LegalReason')
        text = doc.createTextNode('Legal reason')
        legalreason.appendChild(text)
        signaturedef.appendChild(legalreason)
        #End LegalReason
        admindata.appendChild(signaturedef)
        # End SignatureDef

        odm.appendChild(admindata)
        #++++++++++ End AdminData ++++++++++#

        #++++++++++ BEGIN ReferenceData ++++++++++#
        referencedata = doc.createElement('ReferenceData')
        referencedata.setAttribute('StudyOID', '123-456-789')
        referencedata.setAttribute('MetaDataVersionOID', 'v1.01')
        # Begin ItemGroupData
        # for each ItemGroupData
        itemgroupdata = doc.createElement('ItemGroupData')
        itemgroupdata.setAttribute('ItemGroupOID', 'IG.REFSAMP')
        itemgroupdata.setAttribute('ItemGroupRepeatKey', '1')
        # Begin ItemData
        # for each ItemData
        itemdata = doc.createElement('ItemData')
        itemdata.setAttribute('ItemOID', 'IT.REF1')
        itemdata.setAttribute('Value', '1')
        itemgroupdata.appendChild(itemdata)
        # next ItemData
        # End ItemData
        referencedata.appendChild(itemgroupdata)
        # next ReferenceData

        odm.appendChild(referencedata)
        #++++++++++ END ReferenceData ++++++++++#

        #++++++++++ BEGIN ClinicalData ++++++++++#
        clinicaldata = doc.createElement('ClinicalData')
        clinicaldata.setAttribute('StudyOID', '123-456-789')
        clinicaldata.setAttribute('MetaDataVersionOID', 'v1.01')
        # Begin SubjectData
        # for each SubjectData
        subjectdata = doc.createElement('SubjectData')
        subjectdata.setAttribute('SubjectKey', '001')
        # Begin InvestigatorRef
        investigatorref = doc.createElement('InvestigatorRef')
        investigatorref.setAttribute('UserOID', 'USR.inv001')
        subjectdata.appendChild(investigatorref)
        # End InvestigatorRef
        # Begin SiteRef
        siteref = doc.createElement('SiteRef')
        siteref.setAttribute('LocationOID', 'LOC.site002')
        subjectdata.appendChild(siteref)
        # End SiteRef
        # Begin StudyEventData
        # for each StudyEventData
        studyeventdata = doc.createElement('StudyEventData')
        studyeventdata.setAttribute('StudyEventOID', 'SE.VISIT0')
        # Begin FormData
        # for each FormData
        formdata = doc.createElement('FormData')
        formdata.setAttribute('FormOID', 'FORM.DEMOG')
        # Begin Signature
        signature = doc.createElement('Signature')
        # Begin UserRef
        userref = doc.createElement('UserRef')
        userref.setAttribute('UserOID', 'USR.cdisc001')
        signature.appendChild(userref)
        # End UserRef
        # Begin LocationRef
        locationref = doc.createElement('LocationRef')
        locationref.setAttribute('LocationOID', 'LOC.CDISCHome')
        signature.appendChild(locationref)
        # End LocationRef
        # Begin SignatureRef
        signatureref = doc.createElement('SignatureRef')
        signatureref.setAttribute('SignatureOID', 'SD.cdisc001-es')
        signature.appendChild(signatureref)
        # End SignatureRef
        # Begin DateTimeStamp
        datetimestamp = doc.createElement('DateTimeStamp')
        text = doc.createTextNode('20010530T10:06:32')
        datetimestamp.appendChild(text)
        signature.appendChild(datetimestamp)
        # End DataTimeStamp
        formdata.appendChild(signature)
        # End Signature
        # Begin ItemGroupData
        itemgroupdata = doc.createElement('ItemGroupData')
        itemgroupdata.setAttribute('ItemGroupOID', 'IG.DEMOG')
        itemgroupdata.setAttribute('ItemGroupRepeatKey', '1')
        # Begin ItemData
        # for each ItemData
        itemdata = doc.createElement('ItemData')
        itemdata.setAttribute('ItemOID', 'IT.REC_ID')
        itemdata.setAttribute('Value', '46902604')
        itemgroupdata.appendChild(itemdata)
        # next ItemData
        # End ItemData
        formdata.appendChild(itemgroupdata)
        # End ItemGroupData
        studyeventdata.appendChild(formdata)
        # next FormData
        # End FormData
        subjectdata.appendChild(studyeventdata)
        # Next StudyEventData
        # End StudyEventData
        clinicaldata.appendChild(subjectdata)
        # Next SubjectData
        # End SubjectData

        odm.appendChild(clinicaldata)
        #++++++++++ END ClinicalData ++++++++++#

        doc.appendChild(odm)
        #XXXXXXXXXX End ROOT XXXXXXXXXX#

        return str(doc.toxml(encoding='utf-8').decode('utf-8'))

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



