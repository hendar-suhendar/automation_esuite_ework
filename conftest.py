import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from appium import webdriver as appium_webdriver

# ===== Base Configuration =====
BASE_URL = "https://esuite.edot.id"  # ganti jika perlu pointing ke staging/dev/prod

# ===== Web Driver Fixture =====
@pytest.fixture(scope="class")
def web_driver(request):
    """Setup Chrome WebDriver"""
    print(f"\n[Setup] Launching Chrome WebDriver for: {BASE_URL}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    # tambahkan base_url ke atribut driver
    driver.base_url = BASE_URL
    
    yield driver

    keep_browser = request.config.getoption("--keep-browser")
    if not keep_browser:
        print("\n[Teardown] Closing browser...")
        driver.quit()


# ===== Mobile Driver Fixture =====
@pytest.fixture(scope="class")
def mobile_driver(request):
    """Setup Appium Mobile Driver"""
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "app": "/path/to/ework.apk"
    }
    print("\n[Setup] Launching Appium Driver...")
    driver = appium_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    
    # tambahkan base_url agar konsisten (kalau app mobile ada API base URL)
    driver.base_url = BASE_URL
    
    request.cls.driver = driver
    yield driver
    print("\n[Teardown] Closing Appium Driver...")
    driver.quit()
