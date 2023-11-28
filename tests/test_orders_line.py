import time
import allure
from data import Urls
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
