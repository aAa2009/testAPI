from selenium.webdriver.common.by import By


class SearchLocators:
    LIST_USERS = (By.XPATH, "//li[@data-id='users']")
    USER_SINGLE = (By.XPATH, "//li[@data-id='users-single']")
    USER_NOT_FOUNDED = (By.XPATH, "//li[@data-id='users-single-not-found']")
    LIST_RESOURCES = (By.XPATH, "//li[@data-id='unknown']")
    SINGLE_RESOURCE = (By.XPATH, "//li[@data-id='unknown-single']")
    RESOURCE_NOT_FOUNDED = (By.XPATH, "//li[@data-id='unknown-single-not-found']")
    CREATE_USER = (By.XPATH, "//li[@data-id='post']")
    REWRITE_USER = (By.XPATH, "//li[@data-id='put']")
    UPDATE_USER = (By.XPATH, "//li[@data-id='patch']")
    DELETE_USERS = (By.XPATH, "//li[@data-id='delete']")
    REGISTER_SUCCESSFUL = (By.XPATH, "//li[@data-id='register-successful']")
    REGISTER_WITHOUT_PASSWORD = (By.XPATH, "//li[@data-id='register-unsuccessful']")
    LOGIN_SUCCESSFUL = (By.XPATH, "//li[@data-id='login-successful']")
    LOGIN_WITHOUT_PASSWORD = (By.XPATH, "//li[@data-id='login-unsuccessful']")
    REQUEST_WINDOW = (By.XPATH, "//span[@data-key='url']")
    RESPONSE_CODE = (By.XPATH, "//span[@data-key='response-code']")
    RESPONSE_WINDOW = (By.XPATH, "//pre[@data-key='output-response']")
