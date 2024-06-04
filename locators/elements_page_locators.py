from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id = 'userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id = 'userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'permanentAddress']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id = 'submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span.rct-title")

    CHECKED_BOXES_LOCATOR = (By.CSS_SELECTOR, "svg.rct-icon.rct-icon-check")
    EXPECTED_RESULT_LOCATOR = (By.CSS_SELECTOR, "span.text-success")

    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")

class RadioButtonPageLocators:
    RADIO_BUTTONS = (By.CSS_SELECTOR, 'label.custom-control-label')
    SELECTED_BUTTON = (By.CSS_SELECTOR, 'span.text-success')

class WebTablePageLocators:
    #add person form
    ADD_BUTTON =  (By.CSS_SELECTOR, 'button#addNewRecordButton')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, 'input#age')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submit')
    NO_RAWS_ELEMENT = (By.XPATH,".//div[text()='No rows found']")

    #tables

    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")

    SEARCH_INPUT = (By.CSS_SELECTOR,"input#searchBox")
    RAW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span.mr-2")

    #delete
    DELETE_BUTTON = (By.CSS_SELECTOR,"span[title='Delete']")

    #count
    SELECT_ROW_NUMBER = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

class ButtonPageLocators:

    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button#doubleClickBtn")

    RIGHT_BUTTON = (By.CSS_SELECTOR, "button#rightClickBtn")

    CLICK_BUTTON = (By.XPATH, ".//button[text()=\"Click Me\"]")

    DOUBLE_CLICK_RESULT = (By.CSS_SELECTOR, "p#doubleClickMessage") # You have done a double click

    RIGHT_CLICK_RESULT = (By.CSS_SELECTOR, "p#rightClickMessage") # You have done a right click

    CLICK_RESULT = (By.CSS_SELECTOR, "p#dynamicClickMessage") # You have done a dynamic click

class LinksPageLocators:

    SIMPLE_LINK = (By.CSS_SELECTOR, "a#simpleLink")

    BAD_REQUEST = (By.CSS_SELECTOR, "a#bad-request")

class UploadDownloadPageLocators:

    UPLOAD_FILE = (By.CSS_SELECTOR, 'input#uploadFile')
    UPLOADED_FILE= (By.CSS_SELECTOR, 'p#uploadedFilePath')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a#downloadButton')

class DynamicPropertiesPageLocators:

    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button#colorChange")

    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "button#visibleAfter")

    ENABLE_BUTTON = (By.CSS_SELECTOR, "button#enableAfter")





    
