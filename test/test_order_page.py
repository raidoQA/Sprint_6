import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from const import Constants

class TestOrder:
    @allure.title("Тест на оформление заказа с кнопки в header")
    def test_order_header_button(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.cookie_button_click()
        main_page.header_order_button_click()

        order_page = OrderPage(driver)
        order_page.fill_order(Constants.metro1, OrderPageLocators.date_first, OrderPageLocators.rental_period_1, OrderPageLocators.color_black)
        successful_order = order_page.get_order_text()
        assert "Заказ оформлен" in successful_order

    @allure.title("Тест на оформление заказа с кнопки в bottom")
    def test_order_bottom_button(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.cookie_button_click()
        main_page.bottom_order_button_click()
        
        order_page = OrderPage(driver)
        order_page.fill_order(Constants.metro2, OrderPageLocators.date_second, OrderPageLocators.rental_period_2, OrderPageLocators.color_gray)
        successful_order = order_page.get_order_text()
        assert "Заказ оформлен" in successful_order