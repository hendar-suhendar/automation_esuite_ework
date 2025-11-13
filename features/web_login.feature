Feature: eSuite Web Login

  Scenario Outline: Login with multiple credentials
    Given I open the eSuite login page
    When I click Use Email or Username
    And I enter email "<email>"
    And I click login button
    And I enter password "<password>"
    And I click login button
    Then I should see the dashboard

    Examples:
      | email                     | password        |
      | it.qa@edot.id             | it.QA2025       |
