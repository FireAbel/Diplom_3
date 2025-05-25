from selenium.webdriver.common.by import By

class BasePageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_LINK = (By.XPATH, '//p[text()="Лента Заказов"]')
    CONSTRUCTOR_LINK = (By.XPATH, '//p[text()="Конструктор"]')
    STELLAR_BURGERS_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    LOADER = (By.XPATH, '//div[contains(@class, "loader")]')
    ERROR_MESSAGE = (By.XPATH, '//p[contains(@class, "error")]')
    SUCCESS_MESSAGE = (By.XPATH, '//p[contains(@class, "success")]')

    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close')
    MODAL_TITLE = (By.CSS_SELECTOR, '.Modal_modal__title')