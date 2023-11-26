import allure
from Locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Личный Кабинет" в шапке справа')
    def click_on_personal_account_button(self):
        self.element_is_visible(self.locators.BUTTON_PERSONAL_ACCOUNT).click()