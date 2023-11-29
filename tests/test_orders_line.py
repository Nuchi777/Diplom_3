import time
import allure
import pytest
from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestOrdersLine:

    @allure.title('Проверка, если кликнуть на заказ в разделе «Лента заказов», откроется всплывающее окно с деталями')
    def test_click_on_order_open_pop_up_window_with_details_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        main_page.click_on_order_card()
        main_page.check_order_pop_up_window_is_displayed()

    @pytest.mark.parametrize('ingredient_1, ingredient_2', [[MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET]])
    @allure.title('Проверка, заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_from_order_history_display_in_order_line_page(self, driver, login, ingredient_1, ingredient_2):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order(ingredient_1)
        main_page.drag_ingredient_to_order(ingredient_2)
        main_page.click_on_checkout_button()
        main_page.click_on_close_button_order_pop_up_window()
        main_page.click_on_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_history_orders_button()
        main_page = MainPage(driver)
        main_page.check_number_orders_is_in_orders_line()
