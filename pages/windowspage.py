import time

from locators.alerts_frame_windows_page_locators import WindowsLocators, AlertsLocators, FrameLocators, \
    NestedFramesLocators, ModalDialogsLocators
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

class FramePage(BasePage):
    locators = FrameLocators

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content() #???????????????????????? ???? ???????????? ???? ?????? ????????
            return [width, height, text]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME_2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            return [width, height, text]

class NestedFramePage(BasePage):
    locators = NestedFramesLocators

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.PARENT_TEXT).text
        return [parent_text, child_text]

class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocators

    def check_small_modal(self):
        self.element_is_clickable(self.locators.BUTTON_SMALL_MODAL).click()
        title_small_modal = self.element_is_visible(self.locators.TITLE_TEXT_SMALL_MODAL).text
        len_body_text_small_modal = len(self.element_is_visible(self.locators.BODY_TEXT_SMALL_BODY).text)
        self.element_is_clickable(self.locators.BUTTON_CLOSE_SMALL_MODAL).click()
        return title_small_modal, len_body_text_small_modal

    def check_large_modal(self):
        self.element_is_clickable(self.locators.BUTTON_LARGE_MODAL).click()
        title_large_modal = self.element_is_visible(self.locators.TITLE_TEXT_LARGE_MODAL).text
        len_body_text_large_modal = len(self.element_is_visible(self.locators.BODY_TEXT_LARGE_BODY).text)
        self.element_is_clickable(self.locators.BUTTON_CLOSE_LARGE_MODAL).click()
        return title_large_modal, len_body_text_large_modal