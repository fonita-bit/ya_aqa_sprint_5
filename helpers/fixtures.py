# helpers/fixtures.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Настройка WebDriver для Google Chrome
    options = webdriver.ChromeOptions()
    # Для удобства, можно добавить дополнительные опции (например, headless режим)
    options.add_argument("--start-maximized")  # Открывать браузер в максимизированном режиме
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Завершаем работу с драйвером после выполнения теста
    yield driver
    driver.quit()
