import allure
import pytest

from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from data import UrlsStellarBurgers
from Locators.main_page_locators import MainPageLocators


class TestPasswordRecovery:
    @pytest.mark.parametrize('button_locator', [MainPageLocators.BUTTON_ACCOUNT, MainPageLocators.BUTTON_PERSONAL_ACCOUNT])
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_password_recovery_page_by_click_recover_password_button(self, driver, button_locator):
        main_page = MainPage(driver)
        main_page.open(UrlsStellarBurgers.URL_SB)
        main_page.click_on_button(button_locator)
        login_page = LoginPage(driver)
        login_page.click_on_password_recovery_button()
