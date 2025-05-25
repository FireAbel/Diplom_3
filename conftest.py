import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from data import Urls, UserTestData

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

@pytest.fixture(scope="function")
def login_to_account(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email(UserTestData.TEST_USER_EMAIL)
    login_page.enter_password(UserTestData.TEST_USER_PASSWORD)
    login_page.click_login_button()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")