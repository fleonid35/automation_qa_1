import time

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        personal_info = next(generated_person())
        full_name = personal_info.full_name
        email = personal_info.email
        current_address = personal_info.current_address
        permanent_address = personal_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMAMENT_ADDRESS).send_keys(permanent_address)

        self.element_is_present(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address
    def check_field_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMAMENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address
