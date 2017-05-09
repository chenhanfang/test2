from Employee import Employee
import unittest
class Employee_unittest(unittest.TestCase):
    def setUp(self):####初始设置了员工信息，不需要多次输入了
        self.employee=Employee('xe','kj',8000)
    def test_give_default_raise(self):
        # self.empdef=Employee('HH','XX',6000)
        self.assertEqual(self.employee.give_raise(),13000)
    def test_give_custom_raise(self):
        # self.empcus=Employee('jj','cde',5000)
        self.assertEqual(self.employee.give_raise(133),8133)

if __name__=='__main__':
    unittest.main()