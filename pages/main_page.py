import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import URLs


class MainPage(BasePage):

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        self.get_driver(URLs.URL_MAIN_PAGE)
        formatted_question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        formatted_answer_locator = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        last_question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, 7)
        self.cookie_accept(MainPageLocators.COOKIE_BUTTON)
        self.scroll_to_element(last_question_locator)
        self.click_to_element(formatted_question_locator)
        return self.get_text_from_element(formatted_answer_locator)

    @allure.step('Переход к форме заказа через кнопку в хедере')
    def go_to_order_header_button(self):
        self.cookie_accept(MainPageLocators.COOKIE_BUTTON)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Переход к форме заказа через кнопку на странице')
    def go_to_order_page_button(self):
        self.cookie_accept(MainPageLocators.COOKIE_BUTTON)
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_ON_PAGE)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_ON_PAGE)
