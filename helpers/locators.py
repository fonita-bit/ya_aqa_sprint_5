# helpers/locators.py

from selenium.webdriver.common.by import By

# Локаторы главной страницы
class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка на главной странице

    # Кнопка "Конструктор" на главной странице
    CONSTRUCTOR_BUTTON = (By.XPATH, "//button[text()='Конструктор']")  # Кнопка на главной странице


# Локаторы страницы регистрации
class RegisterPageLocators:
    # Поле "Имя"
    NAME_FIELD = (By.NAME, "name")  # Поле для ввода имени

    # Поле "Email"
    EMAIL_FIELD = (By.NAME, "email")  # Поле для ввода email

    # Поле "Пароль"
    PASSWORD_FIELD = (By.NAME, "password")  # Поле для ввода пароля

    # Кнопка регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка для регистрации


# Локаторы страницы профиля (личного кабинета)
class ProfilePageLocators:
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка выхода из аккаунта

    # Заголовок личного кабинета
    PROFILE_PAGE_HEADER = (By.XPATH, "//h2[text()='Личный кабинет']")  # Заголовок на странице профиля


# Локаторы конструктора
class ConstructorPageLocators:
    # Раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//a[text()='Булки']")  # Кнопка раздела "Булки"

    # Раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//a[text()='Соусы']")  # Кнопка раздела "Соусы"

    # Раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//a[text()='Начинки']")  # Кнопка раздела "Начинки"
