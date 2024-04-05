import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    
    @allure.title("Тест на оформление заказа с кнопки в header")
    def test_order_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.cookie_button_click()
        main_page.header_order_button_click()
        order_page = OrderPage(driver)
        order_page.fill_order_1()
        successful_order = order_page.get_order_text()
        assert "Заказ оформлен" in successful_order

    @allure.title("Тест на оформление заказа с кнопки в bottom")
    def test_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.cookie_button_click()
        main_page.bottom_order_button_click()
        order_page = OrderPage(driver)
        order_page.fill_order_2()
        successful_order = order_page.get_order_text()
        assert "Заказ оформлен" in successful_order