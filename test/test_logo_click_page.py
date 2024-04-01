import allure
from const import Url
from pages.main_page import MainPage
from pages.dzen_page import DzenPage



class TestLogoSite:

    @allure.title("Переход на сайт Самокат")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.header_order_button_click()
        main_page.scooter_logo_click()
        assert main_page.get_current_url() == Url.url_scooter


    @allure.title('Тест клика на лого Яндекс')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.click_to_yandex_logo()
        dzen_page = DzenPage(driver)
        text_from_card = dzen_page.get_elements_news()
        assert any('Новости' in item for item in text_from_card)