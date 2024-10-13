
import allure
from tests import helper
from pages.order_page import OrderPage
from data import URLs


class TestOrder:

    @allure.description('Проверяем, что заказ можно оформить перейдя по кнопке  в хедере')
    def test_order_from_header_button(self, driver):
        driver.get(URLs.URL_MAIN_PAGE)
        page = OrderPage(driver)
        page.go_to_order_header_button()
        page.first_fill_form(
            helper.random_name(),
            helper.random_surname(),
            helper.random_address(),
            helper.generate_phone()
        )
        page.second_fill_form(
            "Спасибо, у меня всё"
        )
        page.confirm_order()
        assert page.order_confirmed() == "Посмотреть статус"

    @allure.description('Проверяем, что заказ можно оформить перейдя по кнопке на странице')
    def test_order_from_page_button(self, driver):
        driver.get(URLs.URL_MAIN_PAGE)
        page = OrderPage(driver)
        page.go_to_order_page_button()
        page.first_fill_form(
            helper.random_name(),
            helper.random_surname(),
            helper.random_address(),
            helper.generate_phone()
        )
        page.second_fill_form(
            "Спасибо, у меня всё"
        )
        page.confirm_order()

        assert page.order_confirmed() == "Посмотреть статус"

    @allure.description('Проверяем, что по клику на лого Самоката происходит редирект на главную страницу')
    def test_switch_to_main_page(self, driver):
        driver.get(URLs.URL_ORDER_PAGE)
        page = OrderPage(driver)
        page.click_to_logo_scooter()

        assert driver.current_url == URLs.URL_MAIN_PAGE

    @allure.description('Проверяем, что по клику на лого Яндекса происходит редирект на страницу Дзена')
    def test_switch_to_dzen(self, driver):
        driver.get(URLs.URL_ORDER_PAGE)
        page = OrderPage(driver)
        page.click_to_logo_yandex()
        driver.switch_to.window(driver.window_handles[1])

        assert page.find_element_with_wait_dzen().text == "Всё о Дзене"
