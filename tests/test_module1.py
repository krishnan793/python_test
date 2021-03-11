import unittest
from python_test.modules.module1 import Module1

class Module1Test(unittest.TestCase):
    def setUp(self):
        self.module = Module1()
    
    def test_case(self):
        self.assertEqual(self.module.sum(1,2,3), 1)
    
    def test__case2(self):
        self.assertEqual(self.module.sum(2, 4, 2), 3)