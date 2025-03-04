from selenium.webdriver.common.by import By
class MainPageLocators:
    question_1 = (By.ID, 'accordion__heading-0')
    question_2 = (By.ID, 'accordion__heading-1')
    question_3 = (By.ID, 'accordion__heading-2')
    question_4 = (By.ID, 'accordion__heading-3')
    question_5 = (By.ID, 'accordion__heading-4')
    question_6 = (By.ID, 'accordion__heading-5')
    question_7 = (By.ID, 'accordion__heading-6')
    question_8 = (By.ID, 'accordion__heading-7')

    answer_1 = (By.ID, 'accordion__panel-0')
    answer_2 = (By.ID, 'accordion__panel-1')
    answer_3 = (By.ID, 'accordion__panel-2')
    answer_4 = (By.ID, 'accordion__panel-3')
    answer_5 = (By.ID, 'accordion__panel-4')
    answer_6 = (By.ID, 'accordion__panel-5')
    answer_7 = (By.ID, 'accordion__panel-6')
    answer_8 = (By.ID, 'accordion__panel-7')

    order_button_upper = (By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g')
    order_button_bottom = (By.CSS_SELECTOR, '.Home_FinishButton__1_cWm .Button_Button__ra12g')