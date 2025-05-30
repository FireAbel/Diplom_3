from selenium.webdriver.common.by import By

class AccountPageLocators:
    # Вкладки навигации
    PROFILE = (By.XPATH, '//a[text()="Профиль"]')
    ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    
    # Кнопки
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
