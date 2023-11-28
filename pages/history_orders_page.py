import allure

from locators.history_orders_locators import HistoryOrdersPageLocators
from pages.base_page import BasePage


class HistoryOrdersPage(BasePage):
    locators = HistoryOrdersPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_password_restore_button(self):
        self.element_is_visible(self.locators.TEXT_BUTTON_RESTORE_PASSWORD).click()