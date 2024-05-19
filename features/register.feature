# Created by prana at 18/05/2024
Feature: Register Account functionality

  @completed_registration_mandatory_field
  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I fill in the mandatory fields
    And I click on register button
    Then I should see the success message

  @completed_registration_all_fields
  Scenario: Register with all fields
    Given I navigate to register page
    When I fill in all the fields
    And I click on register button
    Then I should see the success message

  @completed_registration_duplicate_email
  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email
    And I enter existing email address into email field
    And I click on register button
    Then I should see the error message

  @completed_registration_without_data
  Scenario: Register without entering any details
    Given I navigate to register page
    When I don't enter anything into the fields
    And I click on register button
    Then I should see the error message for all the mandatory fields