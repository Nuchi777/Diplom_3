import allure
from Locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке: ')
    def click_on_button(self, locator):
        self.element_is_visible(locator).click()

