import time
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Urls
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



