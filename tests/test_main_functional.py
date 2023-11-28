import allure
from data import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainFunctional:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_constructor_by_click_constructor(self, driver, login):
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
