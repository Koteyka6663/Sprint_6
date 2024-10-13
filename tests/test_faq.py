
import allure
import pytest
from pages.main_page import MainPage
from data import Answers
from data import URLs
class TestFAQ:

    @allure.description('Проверяем, что текст ответа правильный')
    @pytest.mark.parametrize(
        'q_number,result',
        [   (0, Answers.ANSWERS_LIST[0]),
            (1, Answers.ANSWERS_LIST[1]),
            (2, Answers.ANSWERS_LIST[2]),
            (3, Answers.ANSWERS_LIST[3]),
            (4, Answers.ANSWERS_LIST[4]),
            (5, Answers.ANSWERS_LIST[5]),
            (6, Answers.ANSWERS_LIST[6]),
            (7, Answers.ANSWERS_LIST[7])
        ]
    )
    def test_questions_and_answers(self, driver, q_number, result):
        driver.get(URLs.URL_MAIN_PAGE)
        page = MainPage(driver)
        assert page.get_answer_text(q_number) == result, f"Ответ на вопрос {q_number} не соответствует ожидаемому"
