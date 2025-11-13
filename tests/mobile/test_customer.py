import pytest
import allure
from pages.mobile.customer_page import CustomerPage
from faker import Faker

fake = Faker()

@pytest.mark.usefixtures("mobile_driver")
@allure.feature("Mobile Customer")
class TestCustomer:

    @allure.story("Create new customer and verify")
    def test_create_customer(self):
        customer_page = CustomerPage(self.driver)
        customer_name = fake.name()
        customer_page.create_customer(customer_name)
        assert customer_page.verify_customer(customer_name), "Customer not found in list"
