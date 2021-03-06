import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from helpcenterpage import HelpCenterPage


class HelpCenterTest(unittest.TestCase):
    """帮助中心"""
    def setUp(self):
        self.dr = my_driver()
        self.hlep_p = HelpCenterPage(self.dr)
        self.hlep_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.hlep_p.get_content()
        self.assertIn("阿朋贷介绍", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()