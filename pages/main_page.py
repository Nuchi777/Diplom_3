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

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.element_is_clickable(self.locators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Проверка, что заголовок "Соберите бургер" появился на экране')
    def check_title_assemble_burger_is_displayed(self):
        assert self.element_is_visible(self.locators.TITLE_ASSEMBLE_BURGER).is_displayed()

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_line_button(self):
        self.element_is_clickable(self.locators.BUTTON_ORDERS_LINE).click()

    @allure.step('Проверка, что заголовок "Лента заказов" появился на экране')
    def check_title_orders_line_is_displayed(self):
        assert self.element_is_visible(self.locators.TITLE_ORDERS_LINE).is_displayed()

    @allure.step('Клик по ингредиенту для бургера')
    def click_on_burger_ingredient(self):
        self.element_is_visible(self.locators.BURGER_INGREDIENT).click()

    @allure.step('Проверка, что появилось всплывающее окно с "Детали ингредиента"')
    def check_ingredient_pop_up_window_is_displayed(self):
        assert self.element_is_visible(self.locators.POP_UP_WINDOW_INGR_DETAILS).is_displayed()

    @allure.step('Клик по кнопке "крестик" во всплывающем окне с "Детали ингредиента"')
    def click_on_close_button_ingredient_pop_up_window(self):
        self.element_is_visible(self.locators.CLOSE_BUTTON_POP_UP_WINDOW_INGR_DETAILS).click()

    @allure.step('Проверка, что появилось всплывающее окно с "Детали ингредиента"')
    def check_ingredient_pop_up_window_is_enabled(self):
        assert self.element_is_visible(self.locators.POP_UP_WINDOW_INGR_DETAILS).is_enabled()

