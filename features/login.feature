# Created by prana at 18/05/2024
Feature: Login Functionality

  @completed_valid_login
  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click on the login button
    Then I should be redirected to the home page

  @completed_invalid_login
  Scenario: Login with invalid credentials
    Given I am on the login page
    When I enter invalid username and password
    And I click on the login button
    Then I should see an error message

  @completed_empty_login
  Scenario: Login with empty credentials
    Given I am on the login page
    When I enter empty username and password
    And I click on the login button
    Then I should see an error message