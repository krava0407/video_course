import base64
import os
import random
import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, CheckRadioButtonLocators, \
    CheckWebTableLocators, CheckClickLinksLocators, CheckClickButtonLocators, CheckUploadDownloadLocators, \
    CheckDinamicProperties

from pages.base_page import BasePage
from generator.generator import generator_person, generator_file


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

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        time.sleep(1)
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element_by_xpath(self.locators.ROW_PARENT)
        time.sleep(1)
        return row.text.splitlines()

    def update_person_info(self):
        personal_info = next(generator_person())
        age = personal_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def del_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NOT_FOUND).text

    def select_up_to_some_rows(self):
        count = [5,10,20,25,50,100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class CheckClickButton(BasePage):

    locators = CheckClickButtonLocators

    def double_click_button(self):
        source = self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON)
        action = ActionChains(self.driver)
        action.double_click(source).perform()

    def right_click_button(self):
        source = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        action = ActionChains(self.driver)
        action.context_click(source).perform()

    def click_button(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()

    def check_result(self):
        result_double_click = self.element_is_present(self.locators.OUTPUT_RESULT_DOUBLE_CLICK_BUTTON)
        result_right_click = self.element_is_present(self.locators.OUTPUT_RESULT_RIGHT_CLICK_BUTTON)
        result_click = self.element_is_present(self.locators.OUTPUT_RESULT_CLICK_BUTTON)
        return result_double_click.text, result_right_click.text, result_click.text

    #вариант 2, сделан по видео запись-8



class CheckClickLinksCl(BasePage):

    locators = CheckClickLinksLocators

    def check_links(self):
        list_locators = [self.locators.LINK_FIRST, self.locators.LINK_SECOND]
        output_links = []
        print(output_links)
        for link in list_locators:
            simple_link = self.element_is_visible(self.locators.LINK_FIRST)
            request = simple_link.get_attribute('href')
            response = requests.get(request)
            if response.status_code == requests.codes.ok:
                self.element_is_visible(link).click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                output_links.append(self.driver.current_url)
                self.close_active_tab()
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                return link, response.status_code
        return output_links

    def check_links_api(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.element_is_visible(self.locators.LINK_CREATED).click()
        else:
            return response.status_code


class UploadDownloadPage(BasePage):
    locators = CheckUploadDownloadLocators

    def upload_file(self):
        file_name, path = generator_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        text = self.element_is_visible(self.locators.UPLOADED_FILE).text
        return file_name.split("\\")[-1], text.split("\\")[-1]

    def download_file(self):
        link = self.element_is_clickable(self.locators.DOWNLOAD_BUTTON).get_attribute("href")
        print(link)
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\Тол\PycharmProjects\test_site\test_file_{random.randint(0, 100)}.jpg'
        with open(path_name_file, "wb+") as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
            os.remove(path_name_file)
        return check_file

class DinamicPrpetiesPage(BasePage):
    locators = CheckDinamicProperties

    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(6)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_after, color_button_before

    def check_appear_of_button(self):
        time.sleep(6)
        self.element_is_present(self.locators.DINAMIC_BUTTON).click()

    def open_search_page(self):
        self.element_is_clickable(self.locators.BUTTON_ELEMENTS).click()
        self.scroll_down()
        time.sleep(6)
        self.element_is_clickable(self.locators.BUTTON_DINAMIC_PROPERTIES).click()