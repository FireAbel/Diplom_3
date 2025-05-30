from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.BASE_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator)
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    def wait_for_element_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )

    def is_element_present(self, locator, time=10):
        try:
            self.find_element(locator, time)
            return True
        except:
            return False

    def go_to_constructor(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)

    def go_to_order_feed(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)

    def go_to_account(self):
        self.click_element(BasePageLocators.ACCOUNT_BUTTON)

    def go_to_login(self):
        self.click_element(BasePageLocators.LOGIN_BUTTON)

    def wait_for_modal_to_disappear(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]"))
            )
        except TimeoutException:
            pass  # Если модальное окно не появилось, продолжаем выполнение

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False