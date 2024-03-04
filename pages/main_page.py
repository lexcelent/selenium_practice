from base.base import BasePage
from locators.main_page import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON))

    def get_search_textarea(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SEARCH_FIELD))

    def click_search_button(self):
        self.get_search_button().click()

    def send_keys_search_textarea(self, str):
        self.get_search_textarea().send_keys(str)
