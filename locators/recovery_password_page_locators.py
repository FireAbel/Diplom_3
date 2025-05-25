from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    SHOW_PASSWORD_ICON = (By.XPATH, '//button[contains(@class, "input__icon-action")]')
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]')
    PAGE_TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    SUCCESS_MESSAGE = (By.XPATH, '//p[contains(text(), "Проверьте почту")]')

    PASSWORD_VISIBILITY_TOGGLE = (By.CSS_SELECTOR, '.input__icon') # Иконка глаза для показа/скрытия пароля
    PASSWORD_INPUT_ACTIVE_STATE = (By.CSS_SELECTOR, '.input_status_active') # CSS-класс для активного/подсвеченного поля

    RECOVERY_FORM = (By.CSS_SELECTOR, '.forgot-password-form')