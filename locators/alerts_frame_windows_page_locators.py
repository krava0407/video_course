from selenium.webdriver.common.by import By


class WindowsLocators:

    BUTTON_NEW_TAB = (By.XPATH, "//button[@id='tabButton']")
    BUTTON_NEW_WINDOW = (By.XPATH, "//button[@id='windowButton']")
    BUTTON_NEW_WINDOW_MESSAGE = (By.XPATH, "//button[@id='messageWindowButton']")

    NEW_TAB = (By.XPATH, "//h1[@id='sampleHeading']")
    NEW_WINDOW = (By.XPATH, "//h1[@id='sampleHeading']")

class AlertsLocators:

    BUTTON_ALERT = (By.XPATH, "//button[@id='alertButton']")
    BUTTON_TIMER_ALERT = (By.XPATH, "//button[@id='timerAlertButton']")
    BUTTON_CONFIRM_ALERT = (By.XPATH, "//button[@id='confirmButton']")
    RESULT_CONFIRM_ALERT = (By.XPATH, "//span[@id='confirmResult']")

    BUTTON_PROMT_ALERT = (By.XPATH, "//button[@id='promtButton']")
    RESULT_PROMT_ALERT = (By.XPATH, "//span[@id='promptResult']")

    BUTTON_ALERTS_FRAME_WINDOWS = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[3]")
    BUTTON_ALERTS = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]")

class FrameLocators:
    FRAME_1 = (By.XPATH, "//iframe[@id='frame1']")
    FRAME_2 = (By.XPATH, "//iframe[@id='frame2']")
    FRAME_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")

class NestedFramesLocators:
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_TEXT = (By.XPATH, "//p")

class ModalDialogsLocators:

    #small modal
    BUTTON_SMALL_MODAL = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    TITLE_TEXT_SMALL_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    BODY_TEXT_SMALL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    BUTTON_CLOSE_SMALL_MODAL = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    #large modal
    BUTTON_LARGE_MODAL = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    TITLE_TEXT_LARGE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    BODY_TEXT_LARGE_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    BUTTON_CLOSE_LARGE_MODAL = (By.CSS_SELECTOR, "button[id='closeLargeModal']")

