import pytest
from locators.main_page_locators import MainPageLocators
from url import Url

@pytest.mark.parametrize("locator, error_message",
                         [(MainPageLocators.order_button_upper, "Кнопка 'Заказать' из хедера не найдена"),
                          (MainPageLocators.order_button_bottom, "Кнопка 'Заказать' с середины страницы не найдена"),
                          ])
def test_click_order_button_opens_order_page(main_page, order_page, locator, error_message):
    main_page.open_main_page()
    main_page.click_button(locator)
    assert order_page.get_current_url() == Url.ORDER_PAGE_URL, error_message


@pytest.mark.parametrize("name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value, error_message",
                         [("Вася", "Петров", "Москва","Бульвар Рокоссовского","+79999999999", "суббота, 1-е марта 2025 г.","сутки", "Не удалось сделать заказ"),
("Петр", "Васильев", "Питер","Сокольники","+78899999999", "воскресенье, 2-е марта 2025 г.","двое суток", "Не удалось сделать заказ")
                          ])
def test_make_order_with_valid_data(order_page, name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value, error_message):
    is_order_completed_successfully= order_page.make_valid_order(name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value)
    assert is_order_completed_successfully == True

def test_scooter_logo_redirects_from_order_page_to_main(order_page):
    order_page.open_order_page()
    order_page.click_scooter_logo()
    assert order_page.get_current_url() == Url.BASE_PAGE_URL

def test_yandex_logo_redirects_from_order_page_to_dzen_in_new_tab(order_page):
    order_page.open_order_page()
    order_page.click_yandex_logo()
    # Переключаемся на новую вкладку
    order_page.switch_to_last_opened_tab()
    # Получаем URL после перехода
    current_url = order_page.get_current_url()
    assert current_url == Url.DZEN_PAGE_URL