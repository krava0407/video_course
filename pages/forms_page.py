import os
import time
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators
from generator.generator import *



class CheckForms(BasePage):
    locators = FormsPageLocators

    def fill_forms(self):
        person_info = next(generator_person())
        first_name = person_info.first_name
        last_name =person_info.last_name
        mobile = phone_number_generator(length=10)
        #phone = person_info.phone
        #print(phone)
        date_of_birth = "01 05 1985"
        list_subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
        subject = random.choice(list_subjects)
        file_name, path = generator_file()
        email = person_info.email
        current_address = person_info.current_address

        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)

        #self.element_is_clickable(self.locators.DATE_OF_BIRTH).click()
        #not worked because site
        #self.element_is_clickable(self.locators.DATE_OF_BIRTH).clear()
        # self.element_is_clickable(self.locators.DATE_OF_BIRTH).send_keys(Keys.CONTROL + "a")
        # time.sleep(2)
        # self.element_is_clickable(self.locators.DATE_OF_BIRTH).send_keys(Keys.DELETE)
        # time.sleep(2)

        #self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        #time.sleep(5)
        #self.element_is_clickable(self.locators.SUBJECTS).click()

        self.element_is_clickable(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.scroll_down()
        self.element_is_present(self.locators.HOBBIES_MUSIC).click()
        self.element_is_present(self.locators.HOBBIES_SPORTS).click()
        self.element_is_present(self.locators.HOBBIES_READING).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)
        return person_info

    def for_result(self):
        result_list = self.element_are_present(self.locators.LIST_DATA)
        data = []
        for i in result_list:
            self.go_to_element(i)
            data.append(i.text)
        return data

