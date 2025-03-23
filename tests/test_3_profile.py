
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import ProfilePageLocators, ConstructorPageLocators
from helpers.data import generate_email, generate_password


def test_logout_from_profile(driver):
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Явное ожидание кнопки "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Вводим данные для входа
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Нажимаем кнопку "Войти"
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Ожидаем, что мы на странице личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ProfilePageLocators.PROFILE_PAGE_HEADER)
    )

    # Нажимаем кнопку "Выйти"
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    # Ожидаем, что нас перебросит на главную страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )

    # Проверяем, что находимся на главной странице
    assert "Конструктор" in driver.page_source


def test_navigate_to_constructor_from_profile(driver):
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Явное ожидание кнопки "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Вводим данные для входа
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Нажимаем кнопку "Войти"
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Ожидаем, что мы на странице личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ProfilePageLocators.PROFILE_PAGE_HEADER)
    )

    # Переход в конструктор
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    # Ожидаем, что мы в разделе конструктора
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.BUNS_SECTION)
    )

    # Проверяем, что мы в конструкторе
    assert "Конструктор" in driver.page_source
