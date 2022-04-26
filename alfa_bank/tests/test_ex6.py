import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Example 1
# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Войти | Административный сайт Django" in driver.title

# Example 2
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Войти | Административный сайт Django" in driver.title

# Example 3
# # Fixtire for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()

# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Войти | Административный сайт Django" in self.driver.title



# @pytest.mark.usefixtures("driver_init")
# class Test_URL_Chrome:
#     def test_open_url(self, live_server):
#         self.driver.get(("%s%s" % (live_server.url, "/admin/")))
#         assert "Войти | Административный сайт Django" in self.driver.title












