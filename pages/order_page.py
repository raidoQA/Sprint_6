import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from const import Constants

class OrderPage(BasePage):

    @allure.step("Ввод данных для заказа")
    def fill_order(self, choose_metro, date, rent_time, color):
        # имя
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(Constants.name)
        # фамилия
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(Constants.surname)
        # адрес
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(Constants.address)
        # номер телефона
        self.driver.find_element(*OrderPageLocators.phonenumber_input).send_keys(Constants.phonenumber)
        # метро
        self.driver.find_element(*OrderPageLocators.metro).send_keys(choose_metro)
        # станция метро
        self.driver.find_element(*OrderPageLocators.metro_station).click()
        self.driver.find_element(*OrderPageLocators.button_next).click()
        # календарь
        self.driver.find_element(*OrderPageLocators.calendar).click()
        self.driver.find_element(*date).click()
        # срок аренды
        self.driver.find_element(*OrderPageLocators.rent).click()
        self.driver.find_element(*rent_time).click()
        # цвет самоката
        self.driver.find_element(*color).click()
        # оформить
        self.driver.find_element(*OrderPageLocators.order_button).click()
        # подтвердить
        BasePage(self.driver).wait_element(OrderPageLocators.yes_button)
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step("Успешное оформление")
    def get_order_text(self):
        return self.driver.find_element(*OrderPageLocators.status).text