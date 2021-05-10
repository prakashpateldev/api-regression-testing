import unittest
from selenium import webdriver
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        cls.driver.implicitly_wait(5)
    def test_search_automationstepbystep(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get("https://bbc.com")
        # self.driver.find_element_by_name("q").send_keys("Automation step by step")
        # self.driver.find_element_by_name("btnK").click()
    def test_search_zerocode(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get("https://bbc.com")
        # self.driver.find_element_by_name("q").send_keys("Zerocode")
        # self.driver.find_element_by_name("btnK").click()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
