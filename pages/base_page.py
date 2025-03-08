import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим до элемента и кликаем')
    def scroll_and_click(self, locator, timeout=3):
         element = self.wait_and_find_element(locator, timeout, condition=expected_conditions.visibility_of_element_located)
         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
         element = self.wait_and_find_element(locator, timeout, condition=expected_conditions.element_to_be_clickable)
         element.click()

    @allure.step('Кликаем по кнопке')
    def click_button(self, locator):
        self.scroll_and_click(locator)

    @allure.step('Получаем элемент')
    def wait_and_find_element(self, locator, timeout=3, condition=expected_conditions.presence_of_element_located):
        """Ожидает заданное состояние элемента и возвращает его"""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    @allure.step('Переходим по адресу')
    def get_url(self,url):
        return self.driver.get(url)

    @allure.step('Получаем текущий адрес веб-страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        """Принимает куки, если кнопка присутствует"""
        try:
            # Ожидаем появления кнопки принятия куки
            cookie_button = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(BasePageLocators.ACCEPT_COOKIE_BUTTON)
                )
            cookie_button.click()

            # Ожидаем, пока кнопка исчезнет (подтверждение принятия)
            WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(BasePageLocators.ACCEPT_COOKIE_BUTTON)
            )
        except TimeoutException:
            # Если кнопка не появилась, значит, куки уже приняты, выходим
            pass

    def switch_to_last_opened_tab(self):
        """Переключается на последнюю открытую вкладку браузера с ожиданием ее загрузки."""
        # Ждем появления новой вкладки, ожидаем увеличения количества вкладок
        time.sleep(2)
        # Переключаемся на последнюю открытую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

