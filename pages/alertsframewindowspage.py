from locators.alerts_frame_windows_page_locators import AlertsFrameWindowsLocators
from pages.base_page import BasePage


class AlertsFrameWindowsPage(BasePage):
    locator = AlertsFrameWindowsLocators

    def check_click_button_new_tab(self):
        self.element_is_clickable(self.locator.BUTTON_NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_present(self.locator.NEW_TAB).text
        new_tab_href = self.driver.current_url
        return new_tab_text, new_tab_href

    # def check_click_button_new_window(self):
    #     id_opened_page = self.driver.window_handles
    #     self.element_is_clickable(self.locator.BUTTON_NEW_WINDOW).click()
    #     id_all_opened_page = self.driver.window_handles
    #     id_search_page = [window for window in id_all_opened_page if window != id_opened_page][1]
    #     self.driver.switch_to.window(id_search_page)
    #     new_window_text = self.element_is_present(self.locator.NEW_WINDOW).text
    #     new_window_href = self.driver.current_url
    #     return new_window_text, new_window_href

    def check_click_button_new_window(self):
        self.element_is_clickable(self.locator.BUTTON_NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tab_text = self.element_is_present(self.locator.NEW_WINDOW).text
        new_tab_href = self.driver.current_url
        return new_tab_text, new_tab_href


