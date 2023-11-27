import allure
from Locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from Pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):
    locators = RecoveryPasswordPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Личный Кабинет" в шапке справа')
    def click_on_password_recovery_button(self):
        self.element_is_visible(self.locators.TEXT_BUTTON_RECOVERY_PASSWORD).click()