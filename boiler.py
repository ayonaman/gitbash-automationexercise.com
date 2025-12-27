import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    # def test_donate_link_redirect(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     donate_link = driver.find_element(By.LINK_TEXT, "Donate")
    #     donate_link.click()
    #     self.assertIn("donate", driver.current_url.lower())
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()