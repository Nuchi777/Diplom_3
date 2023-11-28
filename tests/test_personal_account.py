import allure
from data import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_account_by_click_personal_account_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button()
        account_page = AccountPage(driver)
        account_page.check_logout_button_is_displayed()

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_history_orders_section(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_history_orders_button()
        current_url = account_page.get_current_url(
            'https://stellarburgers.nomoreparties.site/account/order-history')
        assert current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field(login[0])
        login_page.fill_password_field(login[1])
        login_page.click_on_login_button()
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_logout_button()
        login_page = LoginPage(driver)
        current_url = login_page.get_current_url(
            'https://stellarburgers.nomoreparties.site/login')
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'




