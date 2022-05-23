import time

from pages.windowspage import WindowsPage, AlertsPage


class Test_alerts_frame_windows:

    class TestBrowserWindows:
        def test_button_new_tab(self, driver):
            button_new_tab = WindowsPage(driver=driver, url="https://demoqa.com/browser-windows")
            button_new_tab.open()
            text_fact, url_fact = button_new_tab.check_click_button_new_tab()
            print(text_fact, url_fact)
            assert text_fact == "This is a sample page"
            assert url_fact == "https://demoqa.com/sample"

        def test_button_new_window(self, driver):
            button_new_window = WindowsPage(driver=driver, url="https://demoqa.com/browser-windows")
            button_new_window.open()
            text_fact, url_fact = button_new_window.check_click_button_new_window()
            assert text_fact == "This is a sample page"
            assert url_fact == "https://demoqa.com/sample"


    class TestAlerts:
        def test_button_alert(self, driver):
            button_alert = AlertsPage(driver=driver, url="https://demoqa.com/alerts")
            button_alert.open()
            button_alert.check_click_button_alert()

        def test_button_alert_timer(self, driver):
            button_alert = AlertsPage(driver=driver, url="https://demoqa.com")
            button_alert.open()
            time.sleep(3)
            button_alert.open_search_page()
            result_text = button_alert.check_click_button_alert_timer()
            assert "This alert appeared after 5 seconds" == result_text

        def test_button_confirm_alert(self, driver):
            button_alert = AlertsPage(driver=driver, url="https://demoqa.com")
            button_alert.open()
            button_alert.open_search_page()
            result_text = button_alert.check_click_button_alert_confirm()
            print(result_text)
            assert ['You selected Ok', 'You selected Cancel'] == result_text

        def test_click_button_alert_promt(self, driver):
            button_alert = AlertsPage(driver=driver, url="https://demoqa.com")
            button_alert.open()
            button_alert.open_search_page()
            text = "Tol85"
            result_text = button_alert.check_click_button_alert_promt(text=text)
            print(result_text)
            assert "You entered"+' '+text == result_text



    class TestFrames:
        pass

    class TestNestedFrames:
        pass

    class ModalDialogs:
        pass




