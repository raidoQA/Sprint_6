import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from const import Constants

class OrderPage(BasePage):

    @allure.step("Ввод данных для первого заказа")
    def fill_order_1(self):
        # имя
        self.find_element(*OrderPageLocators.name_input).send_keys(Constants.name)
        # фамилия
        self.find_element(*OrderPageLocators.surname_input).send_keys(Constants.surname)
        # адрес
        self.find_element(*OrderPageLocators.address_input).send_keys(Constants.address)
        # номер телефона
        self.find_element(*OrderPageLocators.phonenumber_input).send_keys(Constants.phonenumber)
        # метро
        self.click_element(*OrderPageLocators.metro)
        # станция метро
        self.click_element(*OrderPageLocators.metro1)
        self.click_element(*OrderPageLocators.button_next)
        # календарь
        self.click_element(*OrderPageLocators.calendar)
        self.click_element(*OrderPageLocators.date_first)
        # срок аренды
        self.click_element(*OrderPageLocators.rent)
        self.click_element(*OrderPageLocators.rental_period_1)
        # цвет самоката
        self.click_element(*OrderPageLocators.color_black)
        # оформить
        self.click_element(*OrderPageLocators.order_button)
        # подтвердить
        self.wait_element(OrderPageLocators.yes_button)
        self.click_element(*OrderPageLocators.yes_button)

    @allure.step("Ввод данных для второго заказа")
    def fill_order_2(self):
        # имя
        self.find_element(*OrderPageLocators.name_input).send_keys(Constants.name)
        # фамилия
        self.find_element(*OrderPageLocators.surname_input).send_keys(Constants.surname)
        # адрес
        self.find_element(*OrderPageLocators.address_input).send_keys(Constants.address)
        # номер телефона
        self.find_element(*OrderPageLocators.phonenumber_input).send_keys(Constants.phonenumber)
        # метро
        self.click_element(*OrderPageLocators.metro)
        # станция метро
        self.click_element(*OrderPageLocators.metro2)
        self.click_element(*OrderPageLocators.button_next)
        # календарь
        self.click_element(*OrderPageLocators.calendar)
        self.click_element(*OrderPageLocators.date_second)
        # срок аренды
        self.click_element(*OrderPageLocators.rent)
        self.click_element(*OrderPageLocators.rental_period_2)
        # цвет самоката
        self.click_element(*OrderPageLocators.color_gray)
        # оформить
        self.click_element(*OrderPageLocators.order_button)
        # подтвердить
        self.wait_element(OrderPageLocators.yes_button)
        self.click_element(*OrderPageLocators.yes_button)

    @allure.step("Успешное оформление")
    def get_order_text(self):
        return self.find_element(*OrderPageLocators.status).text
    
    