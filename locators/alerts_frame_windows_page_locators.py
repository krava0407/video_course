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