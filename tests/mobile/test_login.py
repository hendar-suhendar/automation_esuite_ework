import pytest
import allure
from pages.mobile.login_page import MobileLoginPage

@pytest.mark.usefixtures("mobile_driver")
@allure.feature("Mobile Login")
class TestMobileLogin:

    @allure.story("Login with valid company credentials")
    def test_login_mobile(self):
        login_page = MobileLoginPage(self.driver)
        login_page.login("5049209", "qatestsalesman", "it.QA2025")

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from appium.webdriver.common.appiumby import AppiumBy

        wait = WebDriverWait(self.driver, 10)
        dashboard_selector = (AppiumBy.ID, "dashboard")
        dashboard_element = wait.until(EC.presence_of_element_located(dashboard_selector))
        assert dashboard_element.is_displayed()
