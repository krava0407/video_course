import random
import time

from pages.element_page import TextBoxPage, CheckBoxPage, CheckRadioButton, CheckWebTable, CheckClickButton, \
    CheckClickLinksCl, UploadDownloadPage, DinamicPrpetiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
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

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            check_web_table_page = CheckWebTable(driver, "https://demoqa.com/webtables")
            check_web_table_page.open()
            new_person = check_web_table_page.add_new_person()
            table_result = check_web_table_page.check_add_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            check_web_table_page = CheckWebTable(driver, "https://demoqa.com/webtables")
            check_web_table_page.open()
            key_word = check_web_table_page.add_new_person()[random.randint(0, 5)]
            print(key_word)
            time.sleep(1)
            check_web_table_page.search_some_person(key_word)
            table_result = check_web_table_page.check_search_person()
            print(table_result)
            assert key_word in table_result

        def test_change_info(self, driver):
            check_web_table_page = CheckWebTable(driver, "https://demoqa.com/webtables")
            check_web_table_page.open()
            last_name = check_web_table_page.add_new_person()[1]
            check_web_table_page.search_some_person(last_name)
            age = check_web_table_page.update_person_info()
            row = check_web_table_page.check_search_person()
            assert age in row

        def test_delete_person(self, driver):
            check_web_table_page = CheckWebTable(driver, "https://demoqa.com/webtables")
            check_web_table_page.open()
            email = check_web_table_page.add_new_person()[3]
            check_web_table_page.search_some_person(email)
            check_web_table_page.del_person()
            text = check_web_table_page.check_deleted()
            assert text == "No rows found"

        def test_change_count_row(self, driver):
            check_web_table_page = CheckWebTable(driver, "https://demoqa.com/webtables")
            check_web_table_page.open()
            count = check_web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    class TestClickButtons:

        def test_click(self, driver):
            test_click_button = CheckClickButton(driver, "https://demoqa.com/buttons")
            test_click_button.open()
            test_click_button.double_click_button()
            test_click_button.right_click_button()
            test_click_button.click_button()
            output_result = test_click_button.check_result()
            assert "You have done a double click" in output_result, "Don't work double click"
            assert "You have done a right click" in output_result, "Don't work right-click button"
            assert "You have done a dynamic click" in output_result, "Don't work click button"

    class TestLinks:

        def test_link_opened_new_tab(self, driver):
            test_click_link = CheckClickLinksCl(driver, "https://demoqa.com/links")
            test_click_link.open()
            output_list = test_click_link.check_links()
            assert "https://demoqa.com/" == output_list[0]
            assert "https://demoqa.com/" == output_list[1]

        def test_check_api_links(self, driver):
            test_click_link = CheckClickLinksCl(driver, "https://demoqa.com/links")
            test_click_link.open()
            response_code = test_click_link.check_links_api(url="https://demoqa.com/bad-request")
            assert response_code == 400
            response_code = test_click_link.check_links_api(url="https://demoqa.com/Moved")
            assert response_code == 301
            response_code = test_click_link.check_links_api(url="https://demoqa.com/no-content")
            assert response_code == 204
            response_code = test_click_link.check_links_api(url="https://demoqa.com/Unauthorized")
            assert response_code == 401
            response_code = test_click_link.check_links_api(url="https://demoqa.com/Forbidden")
            assert response_code == 403
            # не смог подобрать адресс
            # response_code = test_click_link.check_links_api(url="https://demoqa.com/Not-Found")
            # assert response_code == 404

    class TestUploadDownloadPage:

        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "The file is not uploaded"

        def test_download_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            check_file = upload_download_page.download_file()
            assert check_file is True, "The file is not downloaded"

    class TestDinamicProperties:

        def test_check_enable_button(self, driver):
            dinamic_properties_page = DinamicPrpetiesPage(driver=driver, url="https://demoqa.com/")
            dinamic_properties_page.open()
            dinamic_properties_page.open_search_page()
            enable_button = dinamic_properties_page.check_enable_button()
            print(enable_button)
            assert enable_button == True

        def test_dinamic_properties(self, driver):
            dinamic_properties_page = DinamicPrpetiesPage(driver=driver, url="https://demoqa.com/")
            dinamic_properties_page.open()
            dinamic_properties_page.open_search_page()
            color_after, color_before = dinamic_properties_page.check_changed_color()
            assert color_before != color_after

        def test_appear_of_button(self, driver):
            dinamic_properties_page = DinamicPrpetiesPage(driver=driver, url="https://demoqa.com/")
            dinamic_properties_page.open()
            dinamic_properties_page.open_search_page()
            appear = dinamic_properties_page.check_appear_of_button()
            print(appear)
            assert appear == True
