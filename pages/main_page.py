import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке: ')
    def click_on_button(self, locator):
        self.element_is_visible(locator).click()


    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_on_personal_account_button(self):
        self.element_is_visible(self.locators.BUTTON_PERSONAL_ACCOUNT).click()


    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_login_in_account_button(self):
        self.element_is_visible(self.locators.BUTTON_ACCOUNT).click()




