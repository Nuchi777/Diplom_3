from selenium.webdriver.common.by import By


class MainPageLocators:
    # главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers"