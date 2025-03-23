import time
from helpers.locators import MainPageLocators, ProfilePageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators

# Проверяет, что при нажатии на кнопку «Войти в аккаунт» на главной странице мы переходим на страницу входа.
def test_login_button_main(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()

    # Пауза, чтобы убедиться, что мы перешли на страницу входа
    time.sleep(2)

    # Проверяем, что на странице входа есть форма для ввода логина
    assert "Вход" in driver.title  # Проверяем, что мы на странице входа

# Проверяет, что при нажатии на кнопку «Личный кабинет» мы переходим на страницу входа.
def test_login_button_profile(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).click()

    # Пауза, чтобы убедиться, что мы перешли на страницу входа
    time.sleep(2)

    # Проверяем, что на странице входа есть форма для ввода логина
    assert "Вход" in driver.title  # Проверяем, что мы на странице входа

# Проверяет, что при нажатии на кнопку «Войти» на странице регистрации мы переходим на страницу входа.
def test_login_button_registration(driver):
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Нажимаем кнопку "Войти" на форме регистрации
    driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON_REGISTRATION).click()

    # Пауза, чтобы убедиться, что мы перешли на страницу входа
    time.sleep(2)

    # Проверяем, что на странице входа есть форма для ввода логина
    assert "Вход" in driver.title  # Проверяем, что мы на странице входа

#Проверяет, что при нажатии на кнопку «Войти в аккаунт» на странице восстановления пароля мы переходим на страницу входа.
def test_login_button_password_recovery(driver):
    # Открываем страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Нажимаем кнопку "Войти в аккаунт" на форме восстановления пароля
    driver.find_element(*PasswordRecoveryPageLocators.LOGIN_BUTTON_RECOVERY).click()

    # Пауза, чтобы убедиться, что мы перешли на страницу входа
    time.sleep(2)

    # Проверяем, что на странице входа есть форма для ввода логина
    assert "Вход" in driver.title  # Проверяем, что мы на странице входа