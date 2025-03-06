from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    OPTIONS_STATIONS = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]')
    OPTION_STATIONS = (By.XPATH, "//ul[contains(@class, 'select-search__options')]/li[1]/button")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    ARRIVAL_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    COLOR_FIELD = (By.CLASS_NAME, 'Order_Checkboxes__3lWSI')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="* Комментарий для курьера"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    RENT_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='%s']")
    NEXT_BUTTON = (By.CSS_SELECTOR, '.Order_NextButton__1_rCA .Button_Button__ra12g')
    DATE_PICKER = (By.CLASS_NAME, 'react-datepicker__month-container')
    DATE_PICKER_DAY = "//div[@aria-label='Choose {}']"
    DATE_PICKER_CURRENT_MONTH = "//div[@class='react-datepicker__current-month']"
    DATE_PICKER_NEXT_MONTH_BUTTON = "//button[contains(@class, 'react-datepicker__navigation--next')]"
    ORDER_BUTTON =  (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(),'Заказать')]")
    ORDER_STATUS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    SEE_FULL_ORDER_INFO_BUTTON = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA .Button_Button__ra12g")

