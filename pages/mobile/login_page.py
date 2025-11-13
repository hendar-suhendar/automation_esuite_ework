from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MobileLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.company_id_input = (AppiumBy.ID, "companyId")
        self.email_input = (AppiumBy.ID, "email")
        self.password_input = (AppiumBy.ID, "password")
        self.login_btn = (AppiumBy.ID, "loginBtn")

    def login(self, company_id, email, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.company_id_input)).send_keys(company_id)
        wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)
        wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_btn)).click()
