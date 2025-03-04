from tests.conftest import main_page
from locators.main_page_locators import MainPageLocators
from url import Url


def test_click_question_1_and_get_answer(main_page, driver):
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_1)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_1)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    assert actual_answer == expected_answer

def test_click_question_2_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_2)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_2)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    assert actual_answer == expected_answer

def test_click_question_3_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_3)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_3)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    assert actual_answer == expected_answer

def test_click_question_4_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_4)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_4)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    assert actual_answer == expected_answer

def test_click_question_5_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_5)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_5)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    assert actual_answer == expected_answer

def test_click_question_6_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_6)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_6)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    assert actual_answer == expected_answer

def test_click_question_7_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_7)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_7)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    assert actual_answer == expected_answer

def test_click_question_8_and_get_answer(main_page, driver):
    # Открываем главную страницу
    driver.get(Url.MAIN_PAGE_URL)
    # Кликаем по вопросу
    main_page.click_button(MainPageLocators.question_8)
    # Получаем ответ на вопрос
    actual_answer = main_page.get_answer(MainPageLocators.answer_8)
    # Сравниваем ожидаемый и фактический текст ответа на вопрос
    expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    assert actual_answer == expected_answer