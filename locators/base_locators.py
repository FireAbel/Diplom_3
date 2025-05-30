from selenium.webdriver.common.by import By

class BasePageLocators:
    # Элементы шапки
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_LINK = (By.XPATH, '//p[text()="Лента Заказов"]')
    STELLAR_BURGERS_LOGO = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]/a')
    ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    
    # Общие элементы модальных окон
    MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    MODAL_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
