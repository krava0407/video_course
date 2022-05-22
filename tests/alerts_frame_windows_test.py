from pages.alertsframewindowspage import AlertsFrameWindowsPage



class Test_alerts_frame_windows:

    class TestBrowserWindows:
        def test_button_new_tab(self, driver):
            button_new_tab = AlertsFrameWindowsPage(driver=driver, url="https://demoqa.com/browser-windows")
            button_new_tab.open()
            text_fact, url_fact = button_new_tab.check_click_button_new_tab()
            print(text_fact, url_fact)
            assert text_fact == "This is a sample page"
            assert url_fact == "https://demoqa.com/sample"

        def test_button_new_window(self, driver):
            button_new_window = AlertsFrameWindowsPage(driver=driver, url="https://demoqa.com/browser-windows")
            button_new_window.open()
            text_fact, url_fact = button_new_window.check_click_button_new_window()
            assert text_fact == "This is a sample page"
            assert url_fact == "https://demoqa.com/sample"


    class TestAlerts:
        pass

    class TestFrames:
        pass

    class TestNestedFrames:
        pass

    class ModalDialogs:
        pass




