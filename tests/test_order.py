
import allure

import data
from tests import helper
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import URLs


class TestOrder:

    @allure.title('Проверяем, что заказ можно оформить перейдя по кнопке  в хедере')
    def test_order_from_header_button(self, driver):

        page_order = OrderPage(driver)
        page_main = MainPage(driver)
        page_order.get_url()
        page_main.go_to_order_header_button()
        page_order.first_fill_form(
            helper.random_name(),
            helper.random_surname(),
            helper.random_address(),
            helper.generate_phone()
        )
        page_order.second_fill_form(
            "Спасибо, у меня всё"
        )
        page_order.confirm_order()
        assert page_order.order_confirmed() == "Посмотреть статус"

    @allure.title('Проверяем, что заказ можно оформить перейдя по кнопке на странице')
    def test_order_from_page_button(self, driver):

        page_order = OrderPage(driver)
        page_main = MainPage(driver)
        page_order.get_url()
        page_main.go_to_order_page_button()
        page_order.first_fill_form(
            helper.random_name(),
            helper.random_surname(),
            helper.random_address(),
            helper.generate_phone()
        )
        page_order.second_fill_form(
            "Спасибо, у меня всё"
        )
        page_order.confirm_order()

        assert page_order.order_confirmed() == "Посмотреть статус"

    @allure.title('Проверяем, что по клику на лого Самоката происходит редирект на главную страницу')
    def test_switch_to_main_page(self, driver):

        page_order = OrderPage(driver)
        page_main = MainPage(driver)
        page_order.get_url()
        page_order.click_to_logo_scooter()

        assert page_main.get_answer_text(0) == data.Answers.ANSWERS_LIST[0]

    @allure.title('Проверяем, что по клику на лого Яндекса происходит редирект на страницу Дзена')
    def test_switch_to_dzen(self, driver):

        page = OrderPage(driver)
        page.get_url()
        page.click_to_logo_yandex()
        page.switch_tab(driver)

        assert page.find_element_with_wait_dzen().text == "Всё о Дзене"
