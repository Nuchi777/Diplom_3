from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:

    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода "Email" для восстановления пароля
    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']")  # кнопка "Восстановить"