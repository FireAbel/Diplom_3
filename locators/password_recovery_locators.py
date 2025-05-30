from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    # Элементы страницы
    RECOVERY_TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    
    # Элементы формы
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    SHOW_PASSWORD_ICON = (By.XPATH, '//div[contains(@class, "input__icon")]')
    
    # Кнопки
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    RESET_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    
    # Состояния
    PASSWORD_INPUT_ACTIVE = (By.XPATH, '//div[contains(@class, "input") and contains(@class, "input_status_active")]')