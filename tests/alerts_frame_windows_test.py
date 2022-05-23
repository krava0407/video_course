import time

from pages.windowspage import WindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage


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

        def test_frames(self, driver):
            frames = FramePage(driver=driver, url="https://demoqa.com/frames")
            frames.open()
            result_frame_1 = frames.check_frame(frame_num='frame1')
            result_frame_2 = frames.check_frame(frame_num='frame2')
            assert result_frame_1 == ['500px', '350px', 'This is a sample page']
            assert result_frame_2 == ['100px', '100px', 'This is a sample page']

    class TestNestedFrames:
        def test_frames(self, driver):
            frames = NestedFramePage(driver=driver, url="https://demoqa.com/nestedframes")
            frames.open()
            result_text = frames.check_nested_frames()
            assert result_text == ['Parent frame', 'Child Iframe'], "Nested frame does not exist"


    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modals = ModalDialogsPage(driver=driver, url="https://demoqa.com/modal-dialogs")
            modals.open()
            title_small, len_body_small = modals.check_small_modal()
            title_large, len_body_large = modals.check_large_modal()
            assert title_small == "Small Modal"
            assert len_body_small == 47
            assert title_large == "Large Modal"
            assert len_body_large == 574




