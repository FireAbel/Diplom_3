import pytest
import allure
from conftest import login_page, password_recovery_page
from urls import Urls
from data import UserTestData


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка URL страницы восстановления пароля')
    def test_password_recovery_page_url(self, driver, login_page):
        login_page.open_site()
        login_page.click_forgot_password()
        assert driver.current_url == Urls.FORGOT_PASSWORD

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_password_recovery_page_access(self, driver, login_page, password_recovery_page):
        login_page.open_site()
        login_page.click_forgot_password()
        password_recovery_page.input_email()
        password_recovery_page.click_recovery_button()
        assert driver.current_url == Urls.RESET_PASSWORD

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка активации поля при клике на кнопку "Показать пароль"')
    def test_password_field_highlight_on_show_click(self, driver, login_page, password_recovery_page):
        login_page.open_site()
        login_page.click_forgot_password()

        password_recovery_page.input_email(UserTestData.TEST_USER_EMAIL)
        password_recovery_page.click_recovery_button()

        password_recovery_page.input_password(UserTestData.TEST_USER_PASSWORD)
        password_recovery_page.click_show_password()
        assert password_recovery_page.is_password_input_active()