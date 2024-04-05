import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from const import Url

class MainPage(BasePage):
    @allure.step("Открываем сайт")
    def open_site(self):
        self.open_url(Url.url_scooter)

    @allure.step("Нажимаем кнопку Куки")
    def cookie_button_click(self):
        self.click_element(*MainPageLocators.cookie_button)

    @allure.step('Нажимаем на лого Яндекса и переходим на новую вкладку')
    def click_to_yandex_logo(self):
        self.click_to_logo(MainPageLocators.logo_yandex)
        main_window_handle = self.get_current_window_handle()
        self.switch_to_new_tab(main_window_handle)

    @allure.step("Нажимаем на логотип Самокат")
    def scooter_logo_click(self):
        self.click_element(*MainPageLocators.scooter_logo_link)
    
    @allure.step("Нажимаем на кнопку 'Заказать' на начальной странице")
    def header_order_button_click(self):
        self.click_element(*MainPageLocators.header_order_button)
    
    @allure.step("Нажимаем на кнопку 'Заказать' в конце страницы")
    def bottom_order_button_click(self):
        self.click_element(*MainPageLocators.bottom_order_button)
    
    @allure.step("Нажимаем на вопрос")
    def question_click(self, question):
        self.click_element(*question)
        self.wait_element(question, 3)

    @allure.step("Получить текст ответа")
    def answer_take(self, answer):
        return self.find_element(*answer).text
    
    @allure.step("Скролим к блоку с вопросами")
    def scrolling_to_questions(self):
        element = self.find_element(*MainPageLocators.question_7)
        self.scroll_to_element(element)