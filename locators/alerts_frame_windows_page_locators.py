from selenium.webdriver.common.by import By


class AlertsFrameWindowsLocators:

    BUTTON_NEW_TAB = (By.XPATH, "//button[@id='tabButton']")
    BUTTON_NEW_WINDOW = (By.XPATH, "//button[@id='windowButton']")
    BUTTON_NEW_WINDOW_MESSAGE = (By.XPATH, "//button[@id='messageWindowButton']")

    NEW_TAB = (By.XPATH, "//h1[@id='sampleHeading']")
    NEW_WINDOW = (By.XPATH, "//h1[@id='sampleHeading']")