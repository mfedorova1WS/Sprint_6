import allure
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from url import Url

class OrderPage(BasePage):
    @allure.step('Выбираем дату в календаре')
    def date_picker_select_date(self, formatted_date):
        """
            Выбирает дату в календаре.
            :param formatted_date: Дата в формате "суббота, 1-е марта 2025 г."
        """
        # Проверяем, есть ли переданная дата на текущей странице
        while True:
            try:
                # Локатор для дня в календаре
                date_locator = (By.XPATH, OrderPageLocators.DATE_PICKER_DAY.format(formatted_date))

                # Находим и кликаем по дате
                self.scroll_and_click(date_locator)
                break  # Если нашли дату, выходим из цикла
            except:
                # Если даты нет, кликаем на кнопку "Следующий месяц" и ищем дальше
                next_month_button_locator = (By.XPATH, OrderPageLocators.DATE_PICKER_NEXT_MONTH_BUTTON)
                self.scroll_and_click(next_month_button_locator)


    @allure.step('Выбираем период бронирования из списка вариантов')
    def select_rent_period(self, period):
        """
                Выбирает период аренды из списка предопределенных вариантов.
                :param period: строка, например 'сутки'
        """
        # Локатор элемента для выбора периода аренды
        rental_period_locator = OrderPageLocators.RENT_PERIOD_OPTION[0], OrderPageLocators.RENT_PERIOD_OPTION[
                                                                             1] % period

        # Находим элемент и кликаем по нему
        element = self.wait_and_find_element(rental_period_locator)
        element.click()

    @allure.step('Оформляем заказ самоката')
    def make_valid_order(self, name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value ):
        try:
            self.get_url(Url.ORDER_PAGE_URL)
            self.accept_cookie()

            # Заполняем поля формы заказа
            # Имя
            self.wait_and_find_element(OrderPageLocators.NAME_FIELD).send_keys(name_value)
            assert self.wait_and_find_element(OrderPageLocators.NAME_FIELD).get_property("value") == name_value

            # Фамилия
            self.wait_and_find_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname_value)
            assert self.wait_and_find_element(OrderPageLocators.SURNAME_FIELD).get_property("value") == surname_value

            # Адрес
            self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address_value)
            assert self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD).get_property("value") == address_value

            # Станции метро из списка
            metro_field = self.wait_and_find_element(OrderPageLocators.METRO_STATION_FIELD)
            metro_field.click()
            metro_field.send_keys(station_value)
            self.wait_and_find_element(OrderPageLocators.OPTION_STATIONS).click()
            assert metro_field.get_property("value") == station_value

            # Номер телефона
            self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_value)
            assert self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD).get_property("value") == phone_value

            # Переход к следующему шагу формы
            self.scroll_and_click(OrderPageLocators.NEXT_BUTTON)

            # Выбираем дату и срок аренды
            self.scroll_and_click(OrderPageLocators.ARRIVAL_DATE_FIELD)
            self.date_picker_select_date(arrival_date_value)

            self.scroll_and_click(OrderPageLocators.RENT_PERIOD_FIELD)
            self.select_rent_period(rent_period_value)
            assert self.wait_and_find_element(OrderPageLocators.RENT_PERIOD_FIELD).text == rent_period_value

            # Завершаем заказ
            self.scroll_and_click(OrderPageLocators.ORDER_BUTTON)
            self.wait_and_find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

            # Проверяем статус заказа
            status_text = self.wait_and_find_element(OrderPageLocators.ORDER_STATUS).text
            return 'Заказ оформлен' in status_text

        except Exception as e:
            print(f"Ошибка при оформлении заказа: {e}")
            return False

    def open_order_page(self):
        """Открывает страницу оформления заказа."""
        self.get_url(Url.ORDER_PAGE_URL)

    def click_yandex_logo(self):
        """Клик на логотип Яндекса."""
        self.click_button(BasePageLocators.YANDEX_LOGO_BUTTON)

    def click_scooter_logo(self):
        """Клик на логотип Яндекса."""
        self.click_button(BasePageLocators.SCOOTER_LOGO_BUTTON)
