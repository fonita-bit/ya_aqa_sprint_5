import time
from helpers.locators import MainPageLocators, ProfilePageLocators, ConstructorPageLocators

# Проверяет, что при нажатии на кнопку «Личный кабинет» на главной странице, происходит вход в личный кабинет, и на странице появляется кнопка «Конструктор».

def test_profile_button(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    time.sleep(2)  # Ждем, чтобы форма входа загрузилась

    # Вводим данные для входа (пример, необходимо изменить для реального теста)
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Пауза, чтобы удостовериться, что мы на странице личного кабинета
    time.sleep(2)

    # Проверяем, что на странице личного кабинета есть кнопка "Конструктор"
    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).is_displayed()

#  Проверяет, что при нажатии на кнопку «Выйти» в личном кабинете происходит выход из аккаунта и мы возвращаемся на главную страницу.
def test_logout(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    time.sleep(2)  # Ждем, чтобы форма входа загрузилась

    # Вводим данные для входа (пример, необходимо изменить для реального теста)
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Пауза, чтобы удостовериться, что мы на странице личного кабинета
    time.sleep(2)

    # Нажимаем кнопку "Выйти"
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    time.sleep(2)

    # Проверяем, что мы вернулись на главную страницу
    assert "Stellar Burgers" in driver.title

#Проверяет, что при нажатии на кнопку «Конструктор» на странице личного кабинета, мы переходим на страницу конструктора, и на странице конструктора видим элементы, уникальные для неё (например, логотип).
def test_go_to_constructor_from_profile(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    time.sleep(2)  # Ждем, чтобы форма входа загрузилась

    # Вводим данные для входа (пример, необходимо изменить для реального теста)
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Пауза, чтобы удостовериться, что мы на странице личного кабинета
    time.sleep(2)

    # Нажимаем кнопку "Конструктор"
    driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).click()

    # Пауза, чтобы удостовериться, что мы на странице конструктора
    time.sleep(2)

    # Проверяем, что мы на странице конструктора (смотрим, есть ли элементы, уникальные для конструктора)
    assert driver.find_element(*ConstructorPageLocators.LOGO_BUTTON).is_displayed()

# Проверяет, что при нажатии на логотип на странице конструктора, мы возвращаемся на главную страницу.
def test_go_to_main_from_constructor(driver):
    # Открываем страницу конструктора
    driver.get("https://stellarburgers.nomoreparties.site/constructor")

    # Нажимаем на логотип Stellar Burgers, чтобы вернуться на главную
    driver.find_element(*ConstructorPageLocators.LOGO_BUTTON).click()

    # Пауза, чтобы удостовериться, что мы вернулись на главную страницу
    time.sleep(2)

    # Проверяем, что мы на главной странице
    assert "Stellar Burgers" in driver.title