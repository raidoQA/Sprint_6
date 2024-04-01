import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажимаем на лого Яндекса и переходим на новую вкладку')
    def click_to_yandex_logo(self):
        self.click_to_logo(MainPageLocators.logo_yandex)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)

        
    
    @allure.step("Нажимаем на логотип Самокат")
    def scooter_logo_click(self):
        return self.driver.find_element(*MainPageLocators.scooter_logo_link).click()
    
    @allure.step("Нажимаем на кнопку 'Заказать' на начальной странице")
    def header_order_button_click(self):
        return self.driver.find_element(*MainPageLocators.header_order_button).click()
    
    @allure.step("Нажимаем на кнопку 'Заказать' в конце страницы")
    def bottom_order_button_click(self):
        return self.driver.find_element(*MainPageLocators.bottom_order_button).click()
    
    @allure.step("Скролим к блоку с вопросами")
    def scrolling_to_questions(self):
        element = self.driver.find_element(*MainPageLocators.question_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Нажимаем на вопрос")
    def question_click(self, question):
        self.driver.find_element(*question).click()
        self.wait_element(question, 3)

    @allure.step("Получить текст ответа")
    def answer_take(self, answer):
        return self.driver.find_element(*answer).text