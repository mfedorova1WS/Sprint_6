from pages.base_page import BasePage
import allure
from url import Url


class MainPage(BasePage):
    @allure.step('Кликаем на вопрос')
    def click_on_question(self, locator):
        self.get_url(Url.BASE_PAGE_URL)
        """Клик по вопросу из FAQ"""
        self.scroll_and_click(locator)

    @allure.step('Получаем ответ вопрос')
    def get_answer(self, locator):
        """Получаем текст ответа на вопрос"""
        return self.wait_and_find_element(locator).text

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        """Открывает страницу оформления заказа."""
        self.get_url(Url.BASE_PAGE_URL)

