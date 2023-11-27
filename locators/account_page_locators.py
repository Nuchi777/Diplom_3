from selenium.webdriver.common.by import By

class AccountPageLocators:
    # форма "Личный Кабинет"
    TEXT_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # текст-кнопка "Выход"