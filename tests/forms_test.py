import time

from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators
from pages.forms_page import CheckForms


class TestForms:

    def test_text_box(self, driver):
        text_forms = CheckForms(driver, "https://demoqa.com/automation-practice-form")
        text_forms.open()
        p = text_forms.fill_forms()
        r = text_forms.for_result()
        print(' ')
        print(p)
        print(r)
        print(p.first_name, p.last_name, p.email, p.current_address)
        print(r[0], r[1], r[8])
        assert [p.first_name + ' ' + p.last_name, p.email, p.current_address] == [r[0], r[1], r[8]]
