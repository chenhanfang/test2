#coding=utf-8
from test3 import Widget
import unittest

class WidgetTestCase(unittest.TestCase ) :
    def setUp(self):
        self.widget=Widget()

    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))

    def testSize1(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))

    def tearDown(self):
        # self.widget.dispose()
        self.widget=None

# def suite():#####添加测试类
#     suite = unittest.TestSuite ()
#     suite.addTest(WidgetTestCase("testSize,testSize1"))
#     return suite

#####测试类中所有的测试方法都是以test开头，可以使用pyunit模块中的makeSuite()方法构造一个
def suite():
    return unittest.makeSuite(WidgetTestCase,"test")

if __name__ == "__main__":
     unittest.main(defaultTest='suite')
    # unittest.main()####pyunit模块中定义的main的全局方法，可以很方便的将一个单元测试模块变成直接运行的测试脚本