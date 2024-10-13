import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.description('Получаем текст ответа')
    def get_answer_text(self, num):
        formatted_question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        formatted_answer_locator = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        last_question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, 7)
        self.cookie_accept(MainPageLocators.COOKIE_BUTTON)
        self.scroll_to_element(last_question_locator)
        self.click_to_element(formatted_question_locator)
        return self.get_text_from_element(formatted_answer_locator)
