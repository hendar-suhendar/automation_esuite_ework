Feature: eSuite Web Create New Company
  As a registered user
  I want to create a new company
  So that it appears in my company list

  Scenario Outline: Create a new company successfully
    Given I open the eSuite login page
    And I am logged in as "<email>"
    And I confirm the email to continue
    And I input the OTP code
    And I enter password "<password>"
    And I navigate to the Companies page
    When I click the "Add New Company" button
    And I enter company name "<company_name>"
    And I enter company address "<company_address>"
    And I select company type "<company_type>"
    And I click the "Save" button
    Then I should see the new company "<company_name>" in the company list

    Examples:
      | email                      | password            | company_name       | company_address         | company_type |
      | fans.suhendar@gmail.com     | QWERTYUIOP1!@#$%^&*()   | PT. Unique Person  | Jl. Sudirman No. 1      | Private      |
      | sakhie.suhendar@gmail.com   | myF@milY#ESuite    | CV. Test Company   | Jl. Gatot Subroto No. 5 | Public       |
