from selenium import webdriver
from chat.models import *
from django.contrib.staticfiles.tesing import StaticLiverServerTest
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)