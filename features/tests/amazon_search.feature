# Created by omar at 5/29/2021
Feature: # Test amazon search
  # Enter feature description here

  Scenario: # User can search for a product
    # Enter steps here
    Given Open Amazon Page
    When input customer in search field
    And Click on Amazon search icon
    Then Verify search worked