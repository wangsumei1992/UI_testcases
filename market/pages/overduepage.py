'''逾期公示'''
from basepage import BasePage
from selenium import webdriver

class OverDuePage(BasePage):
    url = "/data/getoverduelist?scrollpage=1"

    @property
    def content(self):
        return self.by_class_name("panel")

    def get_content(self):
        return self.content.get_attribute("innerHTML")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.3.105/data/getoverduelist?scrollpage=1")
    b = driver.find_element_by_class_name("panel").get_attribute("innerHTML")
    print(b)