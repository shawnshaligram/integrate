import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


class TestEnvArgs(unittest.TestCase):
    """
    Example test case for using environment variables.
    """
    def setUp(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()

        self.driver = webdriver.Firefox()

    def test_env_var_google_search(self):
        search_term = os.environ.get("SEARCH_TERM", "test")

        self.driver.get("https://google.com")
        search = self.driver.find_element_by_name("q")
        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)
        self.assertTrue(self.driver.current_url.endswith(search_term))

    def tearDown(self):
        self.driver.quit()
        self.display.stop()