from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    options_stations = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]')
    option_stations = (By.XPATH, "//ul[contains(@class, 'select-search__options')]/li[1]/button")
    phone_number_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    arrival_date_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.CLASS_NAME, "Dropdown-control")
    color_filed = (By.CLASS_NAME, 'Order_Checkboxes__3lWSI')
    comment_field = (By.XPATH, '//input[@placeholder="* Комментарий для курьера"]')
    confirm_order_button = (By.XPATH, '//button[text()="Да"]')
    rent_period_option = (By.XPATH, "//div[@class='Dropdown-option' and text()='%s']")
    next_button = (By.CSS_SELECTOR, '.Order_NextButton__1_rCA .Button_Button__ra12g')
    date_picker = (By.CLASS_NAME, 'react-datepicker__month-container')
    date_picker_day = "//div[@aria-label='Choose {}']"
    date_picker_current_month = "//div[@class='react-datepicker__current-month']"
    date_picker_next_month_button = "//button[contains(@class, 'react-datepicker__navigation--next')]"
    order_button =  (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(),'Заказать')]")
    order_status = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    see_full_order_info_button = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA .Button_Button__ra12g")

