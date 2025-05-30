from selenium.webdriver.common.by import By

class LoginLocators:
    # Элементы формы
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')
    
    # Кнопки и ссылки
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    RECOVERY_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]')
