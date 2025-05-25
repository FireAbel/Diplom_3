from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Поля ввода
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    RECOVER_SUBMIT_BUTTON = RECOVER_BUTTON
    SHOW_PASSWORD_ICON = (By.XPATH, '//input[@name="Пароль"]/following-sibling::div')

    # Ссылки
    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]')

    # Ошибки
    REGISTER_ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]')

    LOGIN_FORM = (By.CSS_SELECTOR, '.Auth_form__3qKeq')
