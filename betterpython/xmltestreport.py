from xml.etree import ElementTree as ET
import os
import lxml.etree as mytree
from lxml import html

class TestReport(object):
    def __init__(self):
        self.testreport = "TestResult.xml"

    def CreateTestResultFile(self):
        if os.path.exists(self.testreport) == False:
            newElem = ET.Element("TestCases")
            newTree = ET.ElementTree(newElem)
            newTree.write(self.testreport)
#####将结果写成下xml
    def WriteResult(self,testcaseInfo):
        self.CreateTestResultFile()
        testeResultFile = ET.parse(self.testreport)
        root = testeResultFile.getroot()
        newElem = ET.Element("TestCase")
        newElem.attrib={
            "ID":testcaseInfo.id,
            "Name":testcaseInfo.name,
            'Owner':testcaseInfo.owner,
            'Result':testcaseInfo.result,
            'StartTime':testcaseInfo.starttime,
            'EndTime':testcaseInfo.endtime,
            'ErrorInfo':testcaseInfo.errprinfo
        }
        root.append(newElem)
        testeResultFile.write(self.testreport)
    ####将结果写成html
    def CreateHtmlFile(self):
        if os.path.exists('TestResult.html') == False:
            f = open('TestResult.html','w')
            message = """<html>
            <head>
                <title>Automation Test Result</title>
                <style>
                      table {
                              border-collapse: collapse;
                              padding:15px;
                              font-family:"Trebuchet MS",Arial,Helvetica,sans-serif;
                              }
                      th {
                           background-color:red;
                           color;white;
                           border:1px solid #ddd;
                           padding-bottom: 13px;
                           padding-top: 15px;
                           }
                      tr{
                          border: 1px solid #008000;
                          padding-bottom:8px;
                          padding-top:8px;
                          text-align:left;
                          }
                      td{
                          border:1px solid #008000;
                          }
                        </style>
                    </head>
                    <body>
                        <h1>Automation Test Result</h1>
                        <table>
                             <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Owner</th>
                                <th>Result</th>
                                <th>StartTime</th>
                                <th>EndTime</th>
                                <th>ErrorMessage</th>
                            </tr>
                        </table>
                    </body>
                    </html>
                    """
            f.write(message)
            f.close()

