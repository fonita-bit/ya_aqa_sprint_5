# Тесты для проверки успешной регистрации и некорректного пароля.
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import RegisterPageLocators, ProfilePageLocators
from helpers.data import generate_email, generate_password


def test_successful_registration(driver):
    """Тест успешной регистрации"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидаем загрузки элементов страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationPageLocators.NAME_FIELD))

    # Заполняем форму регистрации
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Test")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password())

    # Нажимаем кнопку «Зарегистрироваться»
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Ожидаем появления элемента на странице после успешной регистрации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
    assert "Некорректный пароль" not in driver.page_source


def test_invalid_password_registration(driver):
    """Тест регистрации с некорректным паролем"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Ожидаем загрузки элементов страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationPageLocators.NAME_FIELD))

    # Заполняем форму регистрации с некорректным паролем (менее 6 символов)
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Svetlana")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")

    # Нажимаем кнопку «Зарегистрироваться»
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Проверяем наличие ошибки
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
    error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message