import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
class TextBoxPage (BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields (self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sobaka')
        self.element_is_visible(self.locators.EMAIL).send_keys('sobaka@sobaka.sobaka')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Ulita sobaka')
        self.element_is_visible(self.locators.PERMAMENT_ADDRESS).send_keys('Ulita sobaka 2')
        self.element_is_visible(self.locators.SUBMIT).click()


