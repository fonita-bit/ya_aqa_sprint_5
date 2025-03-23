
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Фикстура для инициализации веб-драйвера
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запускать браузер в фоновом режиме
    service = Service('path_to_chromedriver')  # Укажите путь к ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Убедитесь, что браузер открылся правильно
    yield driver  # Это позволяет использовать driver в тестах

    # Закрытие браузера после выполнения теста
    driver.quit()
}



