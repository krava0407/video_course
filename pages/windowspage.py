import time

from locators.alerts_frame_windows_page_locators import WindowsLocators, AlertsLocators
from pages.base_page import BasePage


class WindowsPage(BasePage):
    locator = WindowsLocators

    def check_click_button_new_tab(self):
        self.element_is_clickable(self.locator.BUTTON_NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_present(self.locator.NEW_TAB).text
        new_tab_href = self.driver.current_url
        return new_tab_text, new_tab_href

    # def check_click_button_new_window(self):
    #     id_opened_page = self.driver.window_handles
    #     self.element_is_clickable(self.locators.BUTTON_NEW_WINDOW).click()
    #     id_all_opened_page = self.driver.window_handles
    #     id_search_page = [window for window in id_all_opened_page if window != id_opened_page][1]
    #     self.driver.switch_to.window(id_search_page)
    #     new_window_text = self.element_is_present(self.locators.NEW_WINDOW).text
    #     new_window_href = self.driver.current_url
    #     return new_window_text, new_window_href

    def check_click_button_new_window(self):
        self.element_is_clickable(self.locator.BUTTON_NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_present(self.locator.NEW_WINDOW).text
        new_tab_href = self.driver.current_url
        return new_tab_text, new_tab_href

class AlertsPage(BasePage):
    locators = AlertsLocators

    def check_click_button_alert(self):
        self.element_is_clickable(self.locators.BUTTON_ALERT).click()
        obj_alert = self.driver.switch_to.alert
        msg_alert = obj_alert.text
        print(msg_alert)
        obj_alert.accept()

    def check_click_button_alert_timer(self):
        self.element_is_clickable(self.locators.BUTTON_TIMER_ALERT).click()
        time.sleep(6)
        obj_alert = self.driver.switch_to.alert
        msg_alert = obj_alert.text
        obj_alert.accept()
        return msg_alert

    def open_search_page(self):
        self.element_is_clickable(self.locators.BUTTON_ALERTS_FRAME_WINDOWS).click()
        time.sleep(6)
        self.element_is_clickable(self.locators.BUTTON_ALERTS).click()
        time.sleep(6)


    def check_click_button_alert_confirm(self):

        list = ['accept', 'cancel']
        list_result = []
        for i in list:
            self.element_is_clickable(self.locators.BUTTON_CONFIRM_ALERT).click()
            obj_alert = self.driver.switch_to.alert
            if i == 'accept':
                obj_alert.accept()
                list_result.append(self.element_is_visible(self.locators.RESULT_CONFIRM_ALERT).text)
            elif i == 'cancel':
                obj_alert.dismiss()
                list_result.append(self.element_is_visible(self.locators.RESULT_CONFIRM_ALERT).text)
        return list_result

    def check_click_button_alert_promt(self, text):
        self.element_is_clickable(self.locators.BUTTON_PROMT_ALERT).click()
        obj_alert = self.driver.switch_to.alert
        obj_alert.send_keys(text)
        obj_alert.accept()
        result_text = self.element_is_visible(self.locators.RESULT_PROMT_ALERT).text
        return result_text

