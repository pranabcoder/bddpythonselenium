# Created by prana at 18/05/2024
Feature: Search Functionality

  @completed_valid_search
  Scenario: Search for a valid product
    Given I am on the homepage
    When I enter valid product into the search box field
    And I click on search button
    Then Valid product should be displayed in the search result

  @completed_invalid_search
  Scenario: Search for a invalid product
    Given I am on the homepage
    When I enter invalid product into the search box field
    And I click on search button
    Then Proper message should be displayed in the search results

  @completed_empty_search
  Scenario: Search without entering any product
    Given I am on the homepage
    When I don't enter anything into the search box field
    And I click on search button
    Then Proper message should be displayed in the search results