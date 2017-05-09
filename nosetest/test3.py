class testclass():
    arr1=2
    arr2=2

    def setUp(self):
        self.arr1=1
        self.arr2=3
        print('Mytestclass setup')

    def tearDown(self):
        print('Mytestclassteardown')

    def Testfunc1(self):
        assert self.arr1==self.arr2

    def Testfunc2(self):
        assert self.arr1==2