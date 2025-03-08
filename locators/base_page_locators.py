from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    SCOOTER_LOGO_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")