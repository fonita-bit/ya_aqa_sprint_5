# test_registration.py
import re
import pytest
from locators import locators


# Функция для проверки формата email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))


# Функция для проверки правильности пароля
def is_valid_password(password):
    return len(password) >= 6


# Функция для проверки успешной регистрации
def successful_registration(driver, name, email, password):
    if not is_valid_email(email):
        print(f"Ошибка: Некорректный формат email: {email}")
        return False

    if not is_valid_password(password):
        print(f"Ошибка: Пароль должен быть минимум из 6 символов.")
        return False

    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ожидание появления кнопки "Зарегистрироваться" и переход на страницу регистрации
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators["submit_button"])).click()

    driver.find_element(*locators['name_field']).send_keys(name)
    driver.find_element(*locators['email_field']).send_keys(email)
    driver.find_element(*locators['password_field']).send_keys(password)
    driver.find_element(*locators['submit_button']).click()

    # Ожидаем, что регистрация завершится, и появляется элемент подтверждения
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators['personal_cabinet']))

    print("Регистрация успешна!")
    return True


# Проверка ошибки при вводе некорректного пароля
def invalid_password_registration(driver, name, email, password):
    if not is_valid_password(password):
        print(f"Ошибка: Пароль должен быть минимум из 6 символов.")
        return False

    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*locators['name_field']).send_keys(name)
    driver.find_element(*locators['email_field']).send_keys(email)
    driver.find_element(*locators['password_field']).send_keys(password)
    driver.find_element(*locators['submit_button']).click()

    # Ожидаем появления ошибки для пароля
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators['error_message']))
    print("Ошибка: Некорректный пароль")
    return False


# Тесты с использованием фикстуры

def test_successful_registration(driver):
    name = "ИмяТест"
    email = "123@ya.ru"
    password = "123456"  # Минимальная длина пароля: 6 символов
    assert successful_registration(driver, name, email, password) == True


def test_invalid_password_registration(driver):
    name = "ИмяТест"
    email = "123@ya.ru"
    password = "123"  # Некорректный пароль (меньше 6 символов)
    assert invalid_password_registration(driver, name, email, password) == False
