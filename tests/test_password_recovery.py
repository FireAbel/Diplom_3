import pytest
import allure
from pages.password_recovery_page import PasswordRecoveryPage
from data import Urls

@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    
    @allure.title('Проверка URL страницы восстановления пароля')
    def test_password_recovery_page_url(self, driver):
        # Открываем страницу восстановления пароля напрямую
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page()
        assert driver.current_url == Urls.FORGOT_PASSWORD

    @allure.title('Проверка видимости формы восстановления пароля')
    def test_password_recovery_form_visible(self, driver):
        # Открываем страницу восстановления пароля напрямую
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page()
        assert password_recovery_page.is_recovery_form_visible()

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_enter_email_and_click_recover(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_page()
        recovery_page.enter_email("test@example.com")
        recovery_page.click_recover_button()
        assert recovery_page.is_password_field_active(), "Поле для ввода нового пароля не активно"

    @allure.title('Проверка активации поля при клике на кнопку "Показать пароль"')
    def test_password_field_highlight_on_show_click(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_page()
        recovery_page.enter_email("test@example.com")
        recovery_page.click_recover_button()
        assert recovery_page.is_password_field_active(), "Поле для ввода нового пароля не активно"
        recovery_page.click_show_password_icon()
        assert recovery_page.is_password_field_focused(), "Поле пароля не подсвечено после клика на иконку показать/скрыть"