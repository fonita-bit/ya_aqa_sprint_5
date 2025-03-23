# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Фикстура для настройки WebDriver
@pytest.fixture
def driver():
    # Настройки Chrome
    options = Options()
    options.add_argument("--start-maximized")  # Открывать браузер в максимизированном режиме
    options.add_argument("--disable-extensions")  # Отключить расширения

    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Убедимся, что драйвер был корректно установлен
    yield driver

    # Закрытие браузера по окончанию теста
    driver.quit()
