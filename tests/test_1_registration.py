
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import RegisterPageLocators, ProfilePageLocators
from helpers.data import generate_email, generate_password

def test_registration_successful(driver):
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Явное ожидание кнопки "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Ожидаем появления формы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Регистрация']"))
    )

    # Вводим данные для регистрации
    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys("TestUser")
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Ожидаем появления страницы профиля (личного кабинета)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ProfilePageLocators.PROFILE_PAGE_HEADER)
    )

    # Проверяем, что мы на странице личного кабинета
    assert "Личный кабинет" in driver.page_source

def test_registration_invalid_password(driver):
    email = generate_email()
    invalid_password = "12345"  # Некорректный пароль (менее 6 символов)

    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Явное ожидание кнопки "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Ожидаем появления формы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Регистрация']"))
    )

    # Вводим данные для регистрации
    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys("TestUser")
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(invalid_password)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Ожидаем появления ошибки на странице
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Пароль должен быть')]]"))
    )

    # Проверяем, что ошибка появилась
    assert "Пароль должен быть не менее 6 символов" in error_message.text
