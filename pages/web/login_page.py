import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.web.login_locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # tunggu maksimal 20 detik

    def _screenshot(self, name="Screenshot"):
        """Attach screenshot ke Allure"""
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Click 'Use Email or Username' button")
    def click_use_email(self):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.USE_EMAIL_BTN)).click()
        self._screenshot("Clicked 'Use Email or Username'")

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)
        self._screenshot(f"Entered email: {email}")

    @allure.step("Click 'Log In' button")
    def click_login(self):
        btn_login = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BTN))
        btn_login.click()
        self._screenshot("Clicked 'Log In'")

    @allure.step("Enter password: {password}")
    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)
        self._screenshot(f"Entered password: {'*' * len(password)}")

    @allure.step("Verify dashboard is displayed")
    def is_dashboard_displayed(self):
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.DASHBOARD_TITLE))
        self._screenshot(f"Dashboard Displayed")
        return True
