from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    USE_EMAIL_BTN = (By.XPATH, "//button[contains(text(), 'Use Email or Username')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username' or @placeholder='Input Email or Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='password']")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Log In')]")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Create Account')]")
    LOGIN_TITLE = (By.XPATH, "//p[contains(text(), 'Sign In')]")
    DASHBOARD_TITLE = (By.XPATH, "//span[normalize-space(text())='QA Production']")

