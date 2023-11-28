import allure
from data import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainFunctional:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_constructor_by_click_constructor_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        main_page.check_title_assemble_burger_is_displayed()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_go_to_orders_line_by_click_orders_line_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        main_page.check_title_orders_line_is_displayed()

    @allure.title('Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient_pop_up_window_appear_with_details(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_burger_ingredient()
        main_page.check_ingredient_pop_up_window_is_displayed()

    @allure.title('Проверка, всплывающее окно с деталями закрывается кликом по крестику')
    def test_ingredient_pop_up_window_closed_on_click_close_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_burger_ingredient()
        main_page.click_on_close_button_ingredient_pop_up_window()
        main_page.check_ingredient_pop_up_window_is_enabled()



