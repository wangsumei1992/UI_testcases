import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
from driver import my_driver
from overduepage import OverDuePage

class OverDueTest(unittest.TestCase):

    def setUp(self):
        self.dr = my_driver()
        self.over_p = OverDuePage(self.dr)
        self.over_p.open()

    def test1_content(self):
        '''页面显示内容'''
        content = self.over_p.get_content()
        self.assertIn('逾期信息', content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()

"""
    @classmethod
    def setUpClass(cls):
        print("starting before all method,i just do one times")


    @classmethod
    def tearDownClass(cls):
        print("ending after all method ended,i just do one times")


    def setUp(self):
        print("prepare  before every method,must execute me one times")


    def tearDown(self):
        print("ending after each method finish ,must execute me one time")
"""