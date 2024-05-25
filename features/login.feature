# Created by prana at 18/05/2024
Feature: Login Functionality

  @completed_valid_login
  Scenario Outline: Login with valid credentials
    Given I am on the login page
    When I enter valid username as "<username>" and password as "<password>"
    And I click on the login button
    Then I should be redirected to the home page
    Examples:
      | username                 | password |
      | pranabtest@gmail.com     | 1234     |
      | pranabtestone@gmail.com  | 12345    |
      | pranabtestwo@gmail.com   | 12345    |

  @completed_invalid_login
  Scenario Outline: Login with invalid credentials
    Given I am on the login page
    When I enter invalid username as "<username>" and password as "<password>"
    And I click on the login button
    Then I should see an error message
    Examples:
      | username                 | password |
      | pranabtest@gmail.com     | 12345    |
      | pranabtestone@gmail.com  | 1234     |

  @completed_empty_login
  Scenario: Login with empty credentials
    Given I am on the login page
    When I enter empty username and password
    And I click on the login button
    Then I should see an error message