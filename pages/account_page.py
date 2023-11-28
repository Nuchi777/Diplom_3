import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    locators = AccountPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка, что кнопка "Выход" появилась на экране')
    def check_logout_button_is_displayed(self):
        assert self.element_is_clickable(self.locators.TEXT_BUTTON_LOGOUT).is_displayed()

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_history_orders_button(self):
        self.element_is_clickable(self.locators.TEXT_BUTTON_HISTORY_ORDERS).click()

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.element_is_clickable(self.locators.TEXT_BUTTON_LOGOUT).click()
