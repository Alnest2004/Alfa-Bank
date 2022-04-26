# # Перед каждым запуском теста будет вызываться этот файл по идеи(но если он унаследован,
# типо унаследовано название функции например "new_user1"),
# НО register работает как-то по-другому
#
# import pytest
# from selenium import webdriver
#
#
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options

#
from pytest_factoryboy import register
from tests.factories import UserFactory, AccountFactory,\
    TransferFactory, User2Factory, Account2Factory, LoanFactory

register(UserFactory)
register(AccountFactory)
register(TransferFactory)
register(User2Factory)
register(Account2Factory)
register(LoanFactory)
#
#
# @pytest.fixture
# def new_user1(db, user_factory):
#     user = user_factory.create()
#     print("Работает")
#     return user
#
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()

# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         from selenium.webdriver.chrome.service import Service
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     if request.param == "firefox":
#         from selenium.webdriver.firefox.service import Service
#         from webdriver_manager.firefox import GeckoDriverManager
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()




#
# # from users.models import User
# #
# # @pytest.fixture
# # def user_1(db):
# #     user = User.objects.create_user("test-user")
# #     print('create-user')
# #     return user
# #
# # @pytest.fixture
# # def new_user_factory(db):
# #     def create_app_user(
# #             username: str,
# #             password: str = None,
# #             first_name: str = "firstname",
# #             last_name: str = "lastname",
# #             email: str = "test@test.com",
# #             is_staff: str = False,
# #             is_superuser: str = False,
# #             is_active: str = True,
# #     ):
# #         user = User.objects.create_user(
# #             username = username,
# #             password = password,
# #             first_name = first_name,
# #             last_name = last_name,
# #             email = email,
# #             is_staff = is_staff,
# #             is_superuser = is_superuser,
# #             is_active = is_active,
# #         )
# #         return user
# #     return create_app_user
# #
# # @pytest.fixture
# # def new_user1(db, new_user_factory):
# #     return new_user_factory("Test_user", "password", "MyName")
# #
# # @pytest.fixture
# # def new_user2(db, new_user_factory):
# #     return new_user_factory("Test_user", "password", "MyName", is_staff="True")
# #
#
