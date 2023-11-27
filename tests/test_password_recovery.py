import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage
from data import UrlsStellarBurgers
from locators.main_page_locators import MainPageLocators


class TestPasswordRecovery:
    @pytest.mark.parametrize('button_locator', [MainPageLocators.BUTTON_ACCOUNT, MainPageLocators.BUTTON_PERSONAL_ACCOUNT])
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_password_recovery_page_by_click_recover_password_button(self, driver, button_locator):
        main_page = MainPage(driver)
        main_page.open(UrlsStellarBurgers.URL_SB)
        main_page.click_on_button(button_locator)
        login_page = LoginPage(driver)
        login_page.click_on_password_restore_button()
        recovery_password_page = RecoveryPasswordPage(driver)
        current_url = recovery_password_page.get_current_url('https://stellarburgers.nomoreparties.site/forgot-password')
        assert current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @pytest.mark.parametrize('button_locator', [MainPageLocators.BUTTON_ACCOUNT, MainPageLocators.BUTTON_PERSONAL_ACCOUNT])
    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_on_recovery_button(self, driver, button_locator):
        main_page = MainPage(driver)
        main_page.open(UrlsStellarBurgers.URL_SB)
        main_page.click_on_button(button_locator)
        login_page = LoginPage(driver)
        login_page.click_on_password_restore_button()
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.input_email_in_email_field()
        recovery_password_page.click_on_restore_button()
        current_url = recovery_password_page.get_current_url('https://stellarburgers.nomoreparties.site/reset-password')
        assert current_url == 'https://stellarburgers.nomoreparties.site/reset-password'

    @pytest.mark.parametrize('button_locator', [MainPageLocators.BUTTON_ACCOUNT, MainPageLocators.BUTTON_PERSONAL_ACCOUNT])
    @allure.title('Проверка клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_show_or_hide_password_button(self, driver, button_locator):
        main_page = MainPage(driver)
        main_page.open(UrlsStellarBurgers.URL_SB)
        main_page.click_on_button(button_locator)
        login_page = LoginPage(driver)
        login_page.click_on_password_restore_button()
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.input_email_in_email_field()
        recovery_password_page.click_on_restore_button()
        recovery_password_page.click_on_show_or_hide_password_button()
        recovery_password_page.check_show_or_hide_password_button_is_active()


