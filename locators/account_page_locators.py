from selenium.webdriver.common.by import By


class AccountPageLocators:
    # форма "Личный Кабинет"
    TEXT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # текст-кнопка "Выход"
    TEXT_BUTTON_HISTORY_ORDERS = (By.XPATH, "//a[text()='История заказов']")  # текст-кнопка "История закаов"
