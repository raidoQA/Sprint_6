import allure
import pytest
from pages.main_page import MainPage
from faq import faq

class TestQuestions:

    @allure.title("Тест блока с вопросами")
    @pytest.mark.parametrize('locator_q, locator_a, answer', faq)
    def test_faq(self, driver, locator_a, locator_q, answer):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.cookie_button_click()
        main_page.scrolling_to_questions()
        main_page.question_click(locator_q)
        actual_answer = main_page.answer_take(locator_a)
        assert actual_answer == answer