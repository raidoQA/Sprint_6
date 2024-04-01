import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from const import Answer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestQuestions:
    faq = [
        [MainPageLocators.question_1, MainPageLocators.answer_1, Answer.ans_1],
        [MainPageLocators.question_2, MainPageLocators.answer_2, Answer.ans_2],
        [MainPageLocators.question_3, MainPageLocators.answer_3, Answer.ans_3],
        [MainPageLocators.question_4, MainPageLocators.answer_4, Answer.ans_4],
        [MainPageLocators.question_5, MainPageLocators.answer_5, Answer.ans_5],
        [MainPageLocators.question_6, MainPageLocators.answer_6, Answer.ans_6],
        [MainPageLocators.question_7, MainPageLocators.answer_7, Answer.ans_7],
        [MainPageLocators.question_8, MainPageLocators.answer_8, Answer.ans_8]
    ]

    @allure.title("Тест блока с вопросами")
    @pytest.mark.parametrize('locator_q, locator_a, answer', faq)
    def test_faq(self, driver, locator_a, locator_q, answer):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.scrolling_to_questions()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.question_8))
        main_page.question_click(locator_q)
        actual_answer = main_page.answer_take(locator_a)
        assert actual_answer == answer