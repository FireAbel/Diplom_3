import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage
from data import UserTestData
from urls import Urls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def password_recovery_page(driver):
    password_recovery_page = PasswordRecoveryPage(driver)
    return password_recovery_page

@pytest.fixture
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)
    return order_feed_page

@pytest.fixture
def account_page(driver):
    account_page = AccountPage(driver)
    return account_page

@pytest.fixture(scope="function")
def login_to_account(driver, login_page):
    login_page.open_site()
    login_page.login(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
    yield