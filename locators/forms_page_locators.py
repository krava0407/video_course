import random

from selenium.webdriver.common.by import By


class FormsPageLocators:

    #fill forms
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SELECT_MONTH = (By.XPATH, "//option[@value='5']")   #0-11
    SELECT_YEAR = (By.XPATH, "//option[@value='1991']") #1900-2022
    SUBJECTS = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES_SPORTS = (By.XPATH, "//label[contains(text(),'Sports')]")
    HOBBIES_READING = (By.XPATH, "//label[contains(text(),'Reading')]")
    HOBBIES_MUSIC = (By.XPATH, "//label[contains(text(),'Music')]")
    FILE_INPUT = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SELECT_STATE = (By.XPATH, "//div[@id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.XPATH, "//div[@id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    #check forms
    LIST_DATA = (By.XPATH, "//div[@class='table-responsive']//td[2]")



