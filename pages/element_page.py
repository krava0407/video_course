from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generator_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators

    def fill_all_fields(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.scroll_down()
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.read_f_n(self.locators.CREATED_FULL_NAME)
        email = self.read_f_n(self.locators.CREATED_EMAIL)
        current_address = self.read_f_n(self.locators.CREATED_CURRENT_ADDRESS)
        permanent_address = self.read_f_n(self.locators.CREATED_PERMANENT_ADDRESS)
        return full_name, email, current_address, permanent_address
