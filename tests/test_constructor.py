import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Urls, UserTestData

@allure.feature('Конструктор бургера')
class TestConstructor:
    
    @allure.title('Проверка переключения вкладок ингредиентов')
    def test_ingredient_tabs_switching(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        # Проверка вкладки "Булки"
        main_page.click_buns_tab()
        assert main_page.is_buns_tab_active()
        assert main_page.is_buns_section_visible()
        
        # Проверка вкладки "Соусы"
        main_page.click_sauces_tab()
        assert main_page.is_sauces_tab_active()
        assert main_page.is_sauces_section_visible()
        
        # Проверка вкладки "Начинки"
        main_page.click_fillings_tab()
        assert main_page.is_fillings_tab_active()
        assert main_page.is_fillings_section_visible()
    
    @allure.title('Проверка drag&drop ингредиентов в конструктор')
    def test_drag_and_drop_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        # Перетаскивание булки
        main_page.drag_bun_to_constructor()
        assert main_page.is_bun_in_constructor()
        
        # Перетаскивание соуса
        main_page.drag_sauce_to_constructor()
        assert main_page.is_sauce_in_constructor()
        
        # Перетаскивание начинки
        main_page.drag_filling_to_constructor()
        assert main_page.is_filling_in_constructor()
    
    @allure.title('Проверка открытия и закрытия модального окна ингредиента')
    def test_ingredient_modal_functionality(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        # Открытие модального окна
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_visible()
        assert main_page.is_ingredient_details_visible()
        
        # Закрытие модального окна
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_visible()
    
    @allure.title('Проверка редиректа на логин для неавторизованного пользователя')
    def test_unauthorized_user_redirected_to_login(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        # Добавление ингредиентов в конструктор
        main_page.drag_bun_to_constructor()
        main_page.drag_filling_to_constructor()
        
        # Попытка оформить заказ
        main_page.click_order_button()
        
        # Проверка редиректа на страницу логина
        login_page = LoginPage(driver)
        assert login_page.is_login_form_visible()
        assert login_page.get_current_url() == Urls.LOGIN 