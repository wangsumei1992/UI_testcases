'''新闻资讯'''
from basepage import BasePage
class NewsReportPage(BasePage):
    url = "/notice/media"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")