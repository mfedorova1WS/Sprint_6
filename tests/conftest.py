import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.base_page import BasePage
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")  # Максимизация окна браузера
    # Создаем объект драйвера
    _driver = webdriver.Firefox(service=service, options=options)
    # Передаем драйвер в тест
    yield _driver
    # Закрытие браузера после выполнения теста
    _driver.quit()


@pytest.fixture(scope="function")
def base_page(driver):
    # Создание экземпляра класса MainPage
    return BasePage(driver)

@pytest.fixture(scope="function")
def main_page(driver):
    # Создание экземпляра класса MainPage
    return MainPage(driver)

from pages.order_page import OrderPage
@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)