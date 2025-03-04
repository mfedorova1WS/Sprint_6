import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, locator):
        # Ждем, пока элемент станет видимым
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        # Находим элемент
        element = self.driver.find_element(*locator)
        # Прокручиваем страницу до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Ждем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        # Кликаем по элементу
        element.click()

    @allure.step('Получаем ответ вопрос')
    def get_answer(self, locator):
        answer_element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            locator))
        answer_element_text = answer_element.text
        return answer_element_text

    def click_button(self, locator):
        # Ожидание, пока элемент станет видимым
        element = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

        try:
            # Пытаемся кликнуть, если элемент кликабелен
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
            element.click()
        except Exception:
            # Если клик не удался, прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Повторяем попытку клика
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
            element.click()