import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.web.create_company_locators import CreateCompanyLocators


class CreateCompanyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # tunggu maksimal 20 detik

    def _screenshot(self, name="Screenshot"):
        """Attach screenshot ke Allure"""
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Navigate to Companies page")
    def navigate_to_companies_page(self):
        self.wait.until(EC.element_to_be_clickable(CreateCompanyLocators.MENU_COMPANIES)).click()
        self._screenshot("Navigated to Companies Page")

    @allure.step("Click 'Add New Company' button")
    def click_add_new_company(self):
        self.wait.until(EC.element_to_be_clickable(CreateCompanyLocators.BTN_ADD_NEW_COMPANY)).click()
        self._screenshot("Clicked 'Add New Company' Button")

    @allure.step("Enter company name: {company_name}")
    def enter_company_name(self, company_name):
        name_field = self.wait.until(EC.visibility_of_element_located(CreateCompanyLocators.INPUT_COMPANY_NAME))
        name_field.clear()
        name_field.send_keys(company_name)
        self._screenshot(f"Entered Company Name: {company_name}")

    @allure.step("Enter company address: {company_address}")
    def enter_company_address(self, company_address):
        address_field = self.wait.until(EC.visibility_of_element_located(CreateCompanyLocators.INPUT_COMPANY_ADDRESS))
        address_field.clear()
        address_field.send_keys(company_address)
        self._screenshot(f"Entered Company Address: {company_address}")

    @allure.step("Select company type: {company_type}")
    def select_company_type(self, company_type):
        dropdown = self.wait.until(EC.element_to_be_clickable(CreateCompanyLocators.SELECT_COMPANY_TYPE))
        dropdown.click()
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(., '{company_type}')]")))
        option.click()
        self._screenshot(f"Selected Company Type: {company_type}")

    @allure.step("Click 'Save' button")
    def click_save(self):
        save_button = self.wait.until(EC.element_to_be_clickable(CreateCompanyLocators.BTN_SAVE))
        save_button.click()
        self._screenshot("Clicked 'Save' Button")

    @allure.step("Verify company '{company_name}' is created")
    def verify_company_created(self, company_name):
        company_item = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//td[contains(., '{company_name}')]")))
        self._screenshot(f"Verified Company '{company_name}' Created")
        return True
