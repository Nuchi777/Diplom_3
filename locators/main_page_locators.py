from random import randint

from selenium.webdriver.common.by import By


class MainPageLocators:
    # главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    BUTTON_ORDERS_LINE = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка "Лента заказов"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers"
    TITLE_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок "Собери бургер"
    TITLE_ORDERS_LINE = (By.XPATH, "//h1[text()='Лента заказов']")  # заголовок "Лента заказов"
    BURGER_INGREDIENT = (By.XPATH, f"(//a[contains(@class, 'BurgerIngredient_ingredient')])[{randint(1,15)}]")  # заголовок "Лента заказов"
    POP_UP_WINDOW_INGR_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")  # Всплывающее окно с "деталями ингредиента"
    CLOSE_BUTTON_POP_UP_WINDOW_INGR_DETAILS = (By.XPATH, "(//button[@type='button'])[1]")   # кнопка "закрыть" всплывающее окно с "деталями ингредиента"