from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
locators = {
    "name_field": (By.NAME, 'name'),
    "email_field": (By.NAME, 'email'),
    "password_field": (By.NAME, 'password'),
    "submit_button": (By.XPATH, "//button[text()='Зарегистрироваться']"),
    "error_message": (By.XPATH, "//div[contains(text(), 'Некорректный пароль')]"),
    "personal_cabinet": (By.XPATH, "//h1[text()='Личный Кабинет']")
}