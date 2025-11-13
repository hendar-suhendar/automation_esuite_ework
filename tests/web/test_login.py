# conftest.py atau test_login.py
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.web.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from config import Config
# === Link ke feature file ===
scenarios('../../features/web_login.feature')

# === Fixture Setup ===
@pytest.fixture
def driver():
    """Setup Chrome WebDriver"""
    print("\n[Setup] Launching Chrome WebDriver...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    print("\n[Teardown] Closing browser...")
   # driver.quit()


# === Step Definitions ===
@given("I open the eSuite login page")
def open_login_page(driver):
        driver.get(driver.base_url)
        driver.login_page = LoginPage(driver)
       

@when("I click Use Email or Username")
def click_use_email(driver):
        driver.login_page.click_use_email()
      

@when(parsers.cfparse('I enter email "{email}"'))
def enter_email(driver, email):
        driver.login_page.enter_email(email)
       

@when("I click login button")
def click_login(driver):
        driver.login_page.click_login()
       

@when(parsers.cfparse('I enter password "{password}"'))
def enter_password(driver, password):
        driver.login_page.enter_password(password)
       

@then(parsers.parse("I should see the dashboard"))
def check_dashboard(driver):
    driver.login_page.is_dashboard_displayed()
       
