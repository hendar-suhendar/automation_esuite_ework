import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import allure
from pages.web.login_page import LoginPage
from pages.web.create_company_page import CreateCompanyPage

# === Link ke Feature File ===
scenarios('../../features/web_create_new_company.feature')


# === STEP DEFINITIONS ===

@given(parsers.cfparse('I am logged in as "{email}" with password "{password}"'))
def login_to_esuite(web_driver, email, password):
    """Login ke eSuite sebelum membuat company"""
    with allure.step("Open eSuite Login Page"):
        web_driver.get(web_driver.base_url)
        login_page = LoginPage(web_driver)
        web_driver.login_page = login_page

        login_page.click_use_email()
        login_page.enter_email(email)
        login_page.click_login()
        login_page.enter_password(password)
        login_page.click_login()
        login_page.is_dashboard_displayed()

    web_driver.company_page = CreateCompanyPage(web_driver)


@when("I navigate to the Companies page")
def navigate_to_companies(web_driver):
    web_driver.company_page.navigate_to_companies_page()


@when('I click the "Add New Company" button')
def click_add_new_company(web_driver):
    web_driver.company_page.click_add_new_company()


@when(parsers.cfparse('I enter company name "{company_name}"'))
def enter_company_name(web_driver, company_name):
    web_driver.company_page.enter_company_name(company_name)


@when(parsers.cfparse('I enter company address "{company_address}"'))
def enter_company_address(web_driver, company_address):
    web_driver.company_page.enter_company_address(company_address)


@when(parsers.cfparse('I select company type "{company_type}"'))
def select_company_type(web_driver, company_type):
    web_driver.company_page.select_company_type(company_type)


@when('I click the "Save" button')
def click_save_button(web_driver):
    web_driver.company_page.click_save()


@then(parsers.cfparse('I should see the new company "{company_name}" in the company list'))
def verify_company_created(web_driver, company_name):
    web_driver.company_page.verify_company_created(company_name)
