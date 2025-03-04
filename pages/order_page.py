import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.common_methods import CommonMethod
from url import Url

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.common = CommonMethod()

    @allure.step('Выбираем дату в календаре')
    def date_picker_select_date(self, formatted_date):
        """
               Выбирает дату в календаре.
               :param formatted_date: Дата в формате "суббота, 1-е марта 2025 г."
        """
        # Ждём, пока появится заголовок текущего месяца
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, OrderPageLocators.date_picker_current_month))
        )

        # Проверяем, есть ли нужная дата на текущей странице
        while True:
            try:
                date_locator = (By.XPATH, OrderPageLocators.date_picker_day.format(formatted_date))
                WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(date_locator)).click()
                break  # Если нашли дату, выходим из цикла
            except:
                # Если даты нет, кликаем "Вперёд" и ищем дальше
                self.driver.find_element(By.XPATH, OrderPageLocators.date_picker_next_month_button).click()

    @allure.step('Выбираем период бронирования из списка вариантов')
    def select_rent_period(self, period):
        """
                       Выбирает период аренды из списка предопределенных вариантов.
                       :param period: строка, например 'сутки'"
                """
        # Находим элемент с нужным текстом и кликаем на него
        rental_period_locator = OrderPageLocators.rent_period_option[0], OrderPageLocators.rent_period_option[1] % period
        self.driver.find_element(*rental_period_locator).click()

    @allure.step('Оформляем заказ самоката')
    def make_valid_order(self, name_value, surname_value, address_value, station_value, phone_value, arrival_date_value, rent_period_value ):
        try:
            # Открываем главную страницу
            self.driver.get(Url.ORDER_PAGE_URL)
            self.common.accept_cookie(self.driver)
            # Ждем, пока элемент Имя станет видимым
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.name_field))
            # Находим элемент Имя
            name_field = self.driver.find_element(*OrderPageLocators.name_field)
            # Заполняем имя
            name_field.send_keys(name_value)
            # Проверяем, что поле заполнено
            actual_name_value = self.driver.find_element(*OrderPageLocators.name_field).get_property("value")
            assert actual_name_value == name_value, f'Ожидалось значение поля Имя: "{name_value}", получено "{actual_name_value}"'

            # Ждем, пока элемент Фамилия станет видимым
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.surname_field))
            # Находим элемент Фамилия
            surname_field = self.driver.find_element(*OrderPageLocators.surname_field)
            # Заполняем Фамилия
            surname_field.send_keys(surname_value)
            # Проверяем, что поле заполнено
            actual_surname_value = self.driver.find_element(*OrderPageLocators.surname_field).get_property("value")
            assert actual_surname_value == surname_value, f'Ожидалось значение поля Фамилия: "{surname_value}", получено "{actual_surname_value}"'

            # Ждем, пока элемент Адрес станет видимым
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.address_field))
            # Находим элемент Адрес
            surname_field = self.driver.find_element(*OrderPageLocators.address_field)
            # Заполняем Адрес
            surname_field.send_keys(address_value)
            # Проверяем, что поле заполнено
            actual_address_value = self.driver.find_element(*OrderPageLocators.address_field).get_property("value")
            assert actual_address_value == address_value, f'Ожидалось значение поля Адрес: "{address_value}", получено "{actual_address_value}"'

            # Ждем, пока элемент Станция Метро станет видимым
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.metro_station_field))
            # Находим элемент Станция Метро
            metro_station_field = self.driver.find_element(*OrderPageLocators.metro_station_field)
            metro_station_field.click()
            # Вводим название станции
            metro_station_field.send_keys(station_value)
            # Ожидаем появления значений со станциями в списке
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.options_stations))

            # Находим и выбираем нужную опцию
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.option_stations))
            self.driver.find_element(*OrderPageLocators.option_stations).click()
            # Проверяем, что поле заполнено
            actual_station_value = self.driver.find_element(*OrderPageLocators.metro_station_field).get_property("value")
            assert actual_station_value == station_value, f'Ожидалось значение поля Станция метро: "{station_value}", получено "{actual_station_value}"'

            # Ждем, пока элемент Телефон станет видимым
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.phone_number_field))
            # Находим элемент Телефон
            phone_field = self.driver.find_element(*OrderPageLocators.phone_number_field)
            # Заполняем
            phone_field.send_keys(phone_value)
            # Проверяем, что поле заполнено
            actual_phone_value = self.driver.find_element(*OrderPageLocators.phone_number_field).get_property("value")
            assert actual_phone_value == phone_value, f'Ожидалось значение поля Телефон: "{phone_value}", получено "{actual_phone_value}"'
            # Жмем Далее
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.next_button))
            self.driver.find_element(*OrderPageLocators.next_button).click()
            # Ждем, пока элемент "Когда привезти самокат" станет видимым
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.arrival_date_field))
            # Находим элемент "Когда привезти самокат"
            self.driver.find_element(*OrderPageLocators.arrival_date_field).click()
            # Появляется календарь
            WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.date_picker))
            # Выбираем дату
            self.date_picker_select_date(arrival_date_value)

            # Находим и кликаем элемент "Срок аренды"
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.rent_period_field))
            self.driver.find_element(*OrderPageLocators.rent_period_field).click()
            self.select_rent_period(rent_period_value)
            # Проверяем, что поле заполнено
            actual_rent_period_value = self.driver.find_element(*OrderPageLocators.rent_period_field).text
            assert actual_rent_period_value == rent_period_value, f'Ожидалось значение поля "Срок аренды": "{rent_period_value}", получено "{actual_rent_period_value}"'
            # Кликаем Заказать
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.order_button))
            self.driver.find_element(*OrderPageLocators.order_button).click()
            # Ждем появления кнопки подтверждения заказа
            WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(OrderPageLocators.confirm_order_button))
            # Подтверждаем заказ
            self.driver.find_element(*OrderPageLocators.confirm_order_button).click()
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(OrderPageLocators.order_status))
            status_text = self.driver.find_element(*OrderPageLocators.order_status).text
            print(f"Получен статус заказа: {status_text}")
            if 'Заказ оформлен' in status_text:
                return True
            else:
                return False

        except Exception as e:
            # Если возникло исключение
            print(f"Ошибка при оформлении заказа: {e}")
            return False

