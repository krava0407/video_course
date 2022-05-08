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
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    COLLAPSE_ALL_BUTTON = (
    By.XPATH, "//button[@title='Collapse all']//*[name()='svg']//*[name()='path' and contains(@d,'M19 3H5c-1')]")
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
    # add person forms
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    # update info
    UPDATE_BUTTON = (By.XPATH, "//span[@title='Edit']")
    NOT_FOUND = (By.XPATH, "//div[@class='rt-noData']")

    ROW = (By.XPATH, "//div[@class='rt-tr-group']")

    COUNT_ROW_LIST = (By.XPATH, "//select[@aria-label='rows per page']")


class CheckClickButtonLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    OUTPUT_RESULT_DOUBLE_CLICK_BUTTON = (By.XPATH, "//p[@id='doubleClickMessage']")
    OUTPUT_RESULT_RIGHT_CLICK_BUTTON = (By.XPATH, "//p[@id='rightClickMessage']")
    OUTPUT_RESULT_CLICK_BUTTON = (By.XPATH, "//p[@id='dynamicClickMessage']")

class CheckClickLinksLocators:
    LINK_FIRST = (By.XPATH, "//a[@id='simpleLink']")
    LINK_SECOND = (By.XPATH, "//a[@id='dynamicLink']")
    LINK_CREATED = (By.XPATH, "//a[@id='created']")
    LINK_NO_CONTENT = (By.XPATH, "//a[@id='no-content']")
    LINK_MOVED = (By.XPATH, "//a[@id='moved']")
    LINK_BAD_REQUEST = (By.XPATH, "//a[@id='bad-request']")
    LINK_UNAUTHORIZED = (By.XPATH, "//a[@id='unauthorized']")
    LINK_FORBIDDEN = (By.XPATH, "//a[@id='forbidden']")
    LINK_INVALID_URL = (By.XPATH, "//a[@id='invalid-url']")

class CheckUploadDownloadLocators:
    DOWNLOAD_BUTTON = (By.XPATH, "//a[@id='downloadButton']")
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='uploadFile']")
    UPLOADED_FILE = (By.XPATH, "//p[@id='uploadedFilePath']")







