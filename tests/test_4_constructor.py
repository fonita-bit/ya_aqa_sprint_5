# tests/test_constructor.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import ConstructorPageLocators, ProfilePageLocators
from helpers.data import generate_email, generate_password


def test_navigate_to_buns_section(driver):
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

    # Явное ожидание перехода на страницу конструктора
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.BUNS_SECTION)
    )

    # Проверяем, что мы в разделе «Булки»
    assert "Булки" in driver.page_source


def test_navigate_to_sauces_section(driver):
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

    # Явное ожидание перехода на страницу конструктора
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.SAUCE_SECTION)
    )

    # Проверяем, что мы в разделе «Соусы»
    assert "Соусы" in driver.page_source


def test_navigate_to_fillings_section(driver):
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

    # Явное ожидание перехода на страницу конструктора
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.FILLING_SECTION)
    )

    # Проверяем, что мы в разделе «Начинки»
    assert "Начинки" in driver.page_source


def test_navigate_between_sections(driver):
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

    # Переход в раздел «Булки»
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.BUNS_SECTION)
    )
    driver.find_element(*ConstructorPageLocators.BUNS_SECTION).click()

    # Явное ожидание перехода в раздел «Соусы»
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.SAUCE_SECTION)
    )
    driver.find_element(*ConstructorPageLocators.SAUCE_SECTION).click()

    # Явное ожидание перехода в раздел «Начинки»
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ConstructorPageLocators.FILLING_SECTION)
    )
    driver.find_element(*ConstructorPageLocators.FILLING_SECTION).click()

    # Проверка на то, что мы вернулись в раздел «Начинки»
    assert "Начинки" in driver.page_source
