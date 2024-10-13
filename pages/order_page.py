import allure
from pages.base_page import BasePage
from data import URLs
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def get_url(self):
        self.get_driver(URLs.URL_MAIN_PAGE)

    @allure.step('Заоплняем форму "Для кого самокат"')
    def first_fill_form(self,
                        name,
                        surname,
                        addres,
                        phone):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT_LOCATOR, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT_LOCATOR, addres)
        self.click_to_element(OrderPageLocators.STATION_INPUT_LOCATOR)
        self.click_to_element(OrderPageLocators.STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT_LOCATOR, phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму "Про аренду"')
    def second_fill_form(self, comment):
        self.click_to_element(OrderPageLocators.DATE_INPUT_LOCATOR)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_MONTH_LOCATOR)
        self.click_to_element(OrderPageLocators.DAY_INPUT_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.COLOR_LOCATOR)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT_LOCATOR, comment)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)

    @allure.step('Подтвержадем заказ')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.POPUP_BUTTON_YES)

    @allure.step('Получаем текст из элемента в попапе подтвержденного заказа')
    def order_confirmed(self):
        element = self.find_element_with_wait(OrderPageLocators.POPUP_BUTTON_STATUS)
        return element.text

    @allure.step('Клик по лого Самоката')
    def click_to_logo_scooter(self):
        self.click_to_element(OrderPageLocators.LOGO_SCOOTER_LOCATOR)

    @allure.step('Клик по лого Яндекса')
    def click_to_logo_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX_LOCATOR)

    @allure.step('Получаем элемент со страницы Дзена')
    def find_element_with_wait_dzen(self):
        element = self.find_element_with_wait(OrderPageLocators.DZEN_LOCATOR)
        return element
