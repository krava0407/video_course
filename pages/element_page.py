import random

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, CheckRadioButtonLocators, \
    CheckWebTableLocators
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
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)

        cnt = 21
        while cnt != 0:
            if cnt > 0:
                item = item_list[random.randint(0, 15)]
                self.go_to_element(item)
                item.click()
                cnt -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITOM)
        data = []
        for i in checked_list:
            title_item = i.find_element_by_xpath(self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').lower().replace('.doc', '')

    def get_output_results(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for i in result_list:
            data.append(i.text)
        return str(data).lower().replace(' ', '')


class CheckRadioButton(BasePage):
    locators = CheckRadioButtonLocators

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.SELECT_YES,
            'no': self.locators.SELECT_NO,
            'impressive': self.locators.SELECT_IMPRESSIVE
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class CheckWebTable(BasePage):
    locators = CheckWebTableLocators

    def add_new_person(self):
        count = 1
        while count != 0:
            print(' ')
            print(f'First Count = {count}')
            personal_info = next(generator_person())
            first_name = personal_info.first_name
            last_name = personal_info.last_name
            email = personal_info.email
            age = personal_info.age
            salary = personal_info.salary
            department = personal_info.department
            self.element_is_clickable(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_add_person(self):
        people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data
