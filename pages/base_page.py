import allure
from const import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открываем сайт")
    def open_site(self):
        return self.driver.get(Url.url_scooter)
    
    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator))
    
    def find_elements_located(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator))
                                                   
    
    def find_and_click_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator)).click()
    
    @allure.step("Нажимаем кнопку Куки")
    def cookie_button_click(self):
        self.driver.find_element(*MainPageLocators.cookie_button).click()
    
    @allure.step("Получаем текущий url")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Клик на лого Яндекс и переключение на новую вкладку')
    def click_to_yandex_logo(self):
        self.click_to_logo(self.logo_yandex)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)

        
    def click_to_logo(self, logo_locator):
        self.find_and_click_element(logo_locator)
    
    def switch_to_new_tab(self, main_window_handle, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda driver: len(self.driver.window_handles) > 1)
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)