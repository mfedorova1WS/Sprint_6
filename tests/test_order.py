import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from url import Url

@pytest.mark.parametrize("locator, error_message",
                         [(MainPageLocators.order_button_upper, "Кнопка 'Заказать' из хедера не найдена"),
                          (MainPageLocators.order_button_bottom, "Кнопка 'Заказать' с середины страницы не найдена"),
                          ])
def test_click_order_button_opens_order_page(main_page, driver, locator, error_message):
    driver.get(Url.MAIN_PAGE_URL)
    main_page.click_button(locator)
    assert driver.current_url == Url.ORDER_PAGE_URL, error_message


@pytest.mark.parametrize("name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value, error_message",
                         [("Вася", "Петров", "Москва","Бульвар Рокоссовского","+79999999999", "суббота, 1-е марта 2025 г.","сутки", "Не удалось сделать заказ"),
("Петр", "Васильев", "Питер","Сокольники","+78899999999", "воскресенье, 2-е марта 2025 г.","двое суток", "Не удалось сделать заказ")
                          ])
def test_make_order_with_valid_data(order_page, driver, name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value, error_message):
    is_order_completed_successfully= order_page.make_valid_order(name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value)
    assert is_order_completed_successfully == True

def test_scooter_logo_redirects_from_order_page_to_main(driver):
    driver.get(Url.ORDER_PAGE_URL)
    driver.find_element(*CommonLocators.scooter_logo_button).click()
    assert driver.current_url == Url.MAIN_PAGE_URL

def test_yandex_logo_redirects_from_order_page_to_dzen_in_new_tab(driver):
    driver.get(Url.ORDER_PAGE_URL)
    driver.find_element(*CommonLocators.yandex_logo_button).click()
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 5).until(expected_conditions.url_contains(Url.DZEN_PAGE_URL))
    assert driver.current_url == Url.DZEN_PAGE_URL