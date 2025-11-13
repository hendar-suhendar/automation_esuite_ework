# Automation eSuite eWork

Framework automation testing untuk **eSuite eWork** menggunakan **Python, Selenium, Appium, dan Pytest-BDD (Cucumber style)**.  
Mendukung pengujian **Web** dan **Mobile**, serta menghasilkan **Allure Report** dengan screenshot hasil test.

---

##Struktur Folder

```
automation_esuite_ework/
├── features/
│   ├── web_login.feature
│   ├── web_create_new_company.feature
│   └── mobile_login.feature
│
├── locators/
│   └── web/
│       ├── login_locators.py
│       └── create_company_locators.py
│
├── pages/
│   └── web/
│       ├── login_page.py
│       └── create_company_page.py
│
├── tests/
│   ├── web/
│   │   ├── test_login.py
│   │   └── test_create_company.py
│   └── mobile/
│       └── test_mobile_login.py
│
├── config/
│   └── conftest.py
│
├── reports/
├── requirements.txt
└── README.md
```

---

## Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/hendar-suhendar/automation_esuite_ework.git
   cd automation_esuite_ework
   ```

2. **Buat Virtual Environment (opsional)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Example: Web Login Test

### **Feature File**
`features/web_login.feature`
```gherkin
Feature: eSuite Web Login

  Scenario Outline: Login with valid credentials
    Given I am on the login page
    When I enter email "<email>"
    And I enter password "<password>"
    And I click the "Login" button
    Then I should see the eSuite dashboard

    Examples:
      | email                    | password          |
      | myns.suhendar@gmail.com  | ABCkdjieiA12@@#  |
      | sakhie.suhendar@gmail.com| ABCkdjieiA12@@#  |
```

### **Run Test**
```bash
pytest tests/web/test_login.py -v --alluredir=reports/
```

### **Generate Report**
```bash
allure serve reports/
```

---

## Example: Mobile Login Test

### **Feature File**
`features/mobile_login.feature`
```gherkin
Feature: eSuite Mobile Login

  Scenario Outline: Login with valid credentials
    Given I open the eSuite mobile app
    When I input email "<email>"
    And I input password "<password>"
    And I tap the "Login" button
    Then I should see the dashboard screen

    Examples:
      | email                    | password          |
      | myns.suhendar@gmail.com  | ABCkdjieiA12@@#  |
```

### **Run Test**
Pastikan **Appium server** sudah berjalan terlebih dahulu:
```bash
appium
```

Lalu jalankan test:
```bash
pytest tests/mobile/test_mobile_login.py -v --alluredir=reports/
```

---

## How It Works

| Komponen | Deskripsi |
|-----------|------------|
| **Feature File (.feature)** | Berisi skenario pengujian dengan format Gherkin (Given-When-Then). |
| **Step Definition (.py)** | Menghubungkan langkah-langkah Gherkin dengan kode Python. |
| **Page Object (.py)** | Mendefinisikan aksi di halaman seperti klik, input, atau verifikasi. |
| **Locator (.py)** | Menyimpan selector (By.ID, By.XPATH, By.CSS_SELECTOR). |
| **conftest.py** | Mengatur driver, konfigurasi, dan Base URL. |
| **Allure Report** | Menampilkan hasil pengujian lengkap dengan screenshot. |

---

## 👨‍💻 Maintainer

**Suhendar**  
Quality Assurance Automation Engineer  
📧 [myns.suhendar@gmail.com](mailto:myns.suhendar@gmail.com)  
🔗 [GitHub Repository](https://github.com/hendar-suhendar/automation_esuite_ework)

---
