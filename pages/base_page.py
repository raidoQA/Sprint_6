import allure
from const import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, *locator):
        self.find_element(*locator).click()
    
    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator))
    
    def find_elements_located(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator))

    def wait_for_element(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((locator)))                                               
    
    def find_and_click_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator)).click()
    
    @allure.step("Получаем текущий url")
    def get_current_url(self):
        return self.driver.current_url
    
    def click_to_logo(self, logo_locator):
        self.find_and_click_element(logo_locator)
    
    def switch_to_new_tab(self, main_window_handle, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda driver: len(self.driver.window_handles) > 1)
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)
    
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_url(self, url):
        self.driver.get(url)
    