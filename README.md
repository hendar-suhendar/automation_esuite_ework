automation_esuite_ework/
│
├── features/ # BDD feature files (Gherkin)
│ ├── web_login.feature
│ └── mobile_login.feature
│
├── locators/ # Element locators
│ ├── web/
│ │ ├── login_locators.py
│ │ └── create_company_locators.py
│ └── mobile/
│ └── login_locators.py
│
├── pages/ # Page Object Model
│ ├── web/
│ │ ├── login_page.py
│ │ └── create_company_page.py
│ └── mobile/
│ └── login_page.py
│
├── tests/ # Step definitions & test runners
│ ├── web/
│ │ ├── test_login.py
│ │ └── test_create_company.py
│ └── mobile/
│ └── test_mobile_login.py
│
├── reports/ # Allure reports
├── conftest.py # Fixtures and base configuration
├── pytest.ini # Pytest settings
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## Installation

1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/automation_esuite_ework.git
   cd automation_esuite_ework


Buat virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


(Opsional) Install Allure Command Line:

scoop install allure   # untuk Windows

Example: Web Login Test
Feature File (features/web_login.feature)
Feature: eSuite Web Login

  Scenario Outline: Login with valid credentials
    Given I am on the login page
    When I enter email "<email>"
    And I enter password "<password>"
    And I click the "Login" button
    Then I should see the eSuite dashboard

    Examples:
      | email                      | password          |
      | sakhie.suhendar@gmail.com  | myF@milY#ESuite  |

Run Test
pytest tests/web/test_login.py -v --alluredir=reports/

Generate Report
allure serve reports/

Example: Mobile Login Test
Feature File (features/mobile_login.feature)
Feature: eSuite Mobile Login

  Scenario Outline: Login with valid credentials
    Given I open the eSuite mobile app
    When I input email "<email>"
    And I input password "<password>"
    And I tap the "Login" button
    Then I should see the dashboard screen

    Examples:
      | email                      | password          |
      | sakhie.suhendar@gmail.com  | myF@milY#ESuite  |

Run Test

Pastikan Appium server sudah berjalan:

appium
pytest tests/mobile/test_mobile_login.py -v --alluredir=reports/

How It Works

Feature File (.feature) → berisi skenario test menggunakan Gherkin.

Step Definition (.py) → menghubungkan langkah-langkah Gherkin ke kode Python.

Page Object (.py) → mendefinisikan aksi di halaman (klik, input, dll).

Locator (.py) → menyimpan selector elemen halaman.

conftest.py → mengatur driver, konfigurasi, dan base URL.

Allure Report → menampilkan hasil test lengkap dengan screenshot.