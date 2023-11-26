from selenium.webdriver.common.by import By


class LoginPageLocators:
    # форма авторизации
    EMAIL = (By.XPATH, "//input[@name='name']")  # поле ввода "email" для авторизации
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода "пароль" для авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
    TEXT_BUTTON_REG_ACCOUNT = (By.LINK_TEXT, "Зарегистрироваться")  # текст-кнопка "Войти"
    TEXT_BUTTON_RECOVERY_PASSWORD = (By.LINK_TEXT, "Зарегистрироваться")  # текст-кнопка "Восстановить пароль"