import allure

from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_password_recovery_button(self):
        self.element_is_visible(self.locators.TEXT_BUTTON_RECOVERY_PASSWORD).click()