from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields

    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #created form

    CREATED_FULL_NAME = "//p[@id='name']"
    CREATED_EMAIL = ("//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ("//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = ("//p[@id='permanentAddress']")

