# import os
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# def take_screenshot(driver, name):
#     time.sleep(1)
#     os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
#     driver.save_screenshot(os.path.join("screenshot", name))
#
# # def test_example(live_server):
# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# #     driver.get(("%s%s" % (live_server.url, "/admin/")))
# #     take_screenshot(driver, "screenshot/admin.png")
#
#
#
# # def test_example(live_server):
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("--headless")
# #     options.add_argument("--window-size=1920,1080")
# #     chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #     chrome_driver.get(("%s%s" % (live_server.url, "/admin/")))
# #     take_screenshot(chrome_driver, "admin/admin.png")
# #
#
#
# @pytest.fixture(params=["chrome1920", "chrome411"], scope="class")
# def driver_init(request):
#     if request.param == "chrome1920":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--window-size=1920,1080")
#         web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         request.cls.browser = "Chrome1920x1080"
#     if request.param == "chrome411":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--window-size=411,823")
#         web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         request.cls.browser = "Chrome411x823"
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()
#
# # Название классов и функции должно начинаться с test_*(как указано в файле pytest.ini)
# # или добавить имена классов в этот файл.
# @pytest.mark.usefixtures("driver_init")
# class Screenshot:
#     def screenshot_admin(self, live_server):
#         self.driver.get(("%s%s" % (live_server.url, "/admin/")))
#         take_screenshot(self.driver, "admin/" + "admin" + self.browser + ".png")
#         assert "Войти | Административный сайт Django" in self.driver.title
#
#
#
#
#
#
#
#
#
#
#
