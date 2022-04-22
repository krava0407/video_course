import time

from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, CheckRadioButton



class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            #text_box_page.fill_all_fields()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_addr
            assert permanent_address == output_per_addr

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_results()
            assert input_check_box == output_result

    class TestRadioButton:

        def test_check_radio_button(self, driver):
            check_radioButton_page = CheckRadioButton(driver, "https://demoqa.com/radio-button")
            check_radioButton_page.open()
            check_radioButton_page.click_on_the_radio_button('yes')
            output_yes = check_radioButton_page.get_output_result()
            check_radioButton_page.click_on_the_radio_button('impressive')
            output_no = check_radioButton_page.get_output_result()
            check_radioButton_page.click_on_the_radio_button('no')
            output_impression = check_radioButton_page.get_output_result()


            assert output_yes == "Yes"
            assert output_impression == "Impressive"
            assert output_no == "No"




