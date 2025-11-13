# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class CustomerPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.add_customer_btn = (AppiumBy.ID, "addCustomerBtn")
#         self.name_input = (AppiumBy.ID, "customerName")
#         self.save_btn = (AppiumBy.ID, "saveCustomerBtn")
#         self.customer_list = (AppiumBy.CSS_SELECTOR, ".customer-list")

#     def create_customer(self, name):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.element_to_be_clickable(self.add_customer_btn)).click()
#         wait.until(EC.presence_of_element_located(self.name_input)).send_keys(name)
#         wait.until(EC.element_to_be_clickable(self.save_btn)).click()

#     def verify_customer(self, name):
#         wait = WebDriverWait(self.driver, 10)
#         customer_items = wait.until(EC.presence_of_all_elements_located(self.customer_list))
#         return any(name in item.text for item in customer_items)
