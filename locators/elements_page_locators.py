from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # created form

    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH,"//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    COLLAPSE_ALL_BUTTON = (By.XPATH, "//button[@title='Collapse all']//*[name()='svg']//*[name()='path' and contains(@d,'M19 3H5c-1')]")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITOM = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")

class CheckRadioButtonLocators:

    SELECT_YES = (By.XPATH, "//label[contains(text(),'Yes')]")
    SELECT_IMPRESSIVE = (By.XPATH, "//label[contains(text(),'Impressive')]")
    SELECT_NO = (By.XPATH, "//label[contains(text(),'No')]")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")

class CheckWebTableLocators:

    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME_INPUT =(By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT =(By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT =(By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT =(By.XPATH, "//input[@id='age']")
    SALARY_INPUT =(By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT =(By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")


