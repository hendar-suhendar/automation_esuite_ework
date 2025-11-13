from selenium.webdriver.common.by import By

class CreateCompanyLocators:
    #Create Account
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[normalize-space(text())='Create Account']")
    COMPANY_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@name='companyName' or @placeholder='Company Name']")
    
    COMPANY_PHONE_INPUT = (By.XPATH, "//input[@name='companyPhone' or @placeholder='Phone']")
    COMPANY_ADDRESS_INPUT = (By.XPATH, "//input[@name='companyAddress' or @placeholder='Address']")
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Save') or contains(text(), 'Submit')]")
    COMPANY_DETAIL_NAME = (By.XPATH, "//div[contains(@class, 'company-detail')]//span[contains(text(), '')]") 
