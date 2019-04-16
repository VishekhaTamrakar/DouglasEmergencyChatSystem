import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Dcechat_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_chat_close_event(self):
        user = "admin"
        pwd = "1instructor1"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://dcechat.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://dcechat.herokuapp.com/events/event/7/edit/")
        elem = driver.find_element_by_id("id_is_open")
        elem.click();
        time.sleep(5)
        elem = driver.find_element_by_class_name("save")
        elem.click()
        time.sleep(5)




if __name__ == "__main__":
    unittest.main()