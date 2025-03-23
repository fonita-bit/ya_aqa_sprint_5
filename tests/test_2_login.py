
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import MainPageLocators, ProfilePageLocators
from helpers.data import generate_email, generate_password


def test_login_from_main_page(driver):
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Явное ожидание кнопки "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN)
    )
    login_button.click()

    # Ожидаем появления полей для ввода email и пароля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    # Вводим данные для входа
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Нажимаем кнопку "Войти"
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Ожидаем, что мы на странице личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ProfilePageLocators.PROFILE_PAGE_HEADER)
    )

    # Проверяем, что мы на странице личного кабинета
    assert "Личный кабинет" in driver.page_source
