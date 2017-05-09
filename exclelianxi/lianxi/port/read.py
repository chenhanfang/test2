import xlrd
import ast#####将字符串转化成数据字典
class readExcel(object):
    def __init__(self,path):
        self.path=path
        ######获取索引
    @property
    def getSheet(self):
        xl=xlrd.open_workbook(self.path)
        sheet=xl.sheets()[0]
        return sheet
    ######获取行数
    @property
    def getRows(self):
        row=self.getSheet.nrows
        return row
    #####获取列数
    @property
    def getCol(self):
        col=self.getSheet.ncols
        return col
    ######获取每列的数据值
    @property
    def getName(self):
        TestName=[]
        for i in range(1,self.getRows):
            TestName.append(self.getSheet.cell(i,0).value)
        return TestName
    @property
    def getData(self):
        TestData=[]
        for i in range(1,self.getRows):
            params=ast.literal_eval(self.getSheet.cell(i,3).value)####将字符串转化成数据字典
            TestData.append(params)
        return TestData
    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell(i, 1).value)
        return TestUrl
    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell(i, 2).value)
        return TestMethod
    @property
    def getResult(self):
        TestResult = []
        for i in range(1, self.getRows):
            TestResult.append(self.getSheet.cell(i, 4).value)
        return TestResult




