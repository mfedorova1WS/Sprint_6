from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.common_locators import CommonLocators


class CommonMethod:
    def accept_cookie(self, driver):
        try:
            # Ожидаем появления кнопки закрытия кук
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(CommonLocators.ACCEPT_COOKIE_BUTTON)
            )
            # Если кнопка есть, кликаем на принятие кук
            driver.find_element(*CommonLocators.ACCEPT_COOKIE_BUTTON).click()
            # Ждем, пока кнопка исчезнет
            WebDriverWait(driver, 3).until(
                expected_conditions.invisibility_of_element_located(CommonLocators.ACCEPT_COOKIE_BUTTON)
            )
        except TimeoutException:
            # Если кнопка не появилась, просто выходим из метода
            pass