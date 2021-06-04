# Created by omar at 6/3/2021
Feature: # Ensure add cart is working
  # Enter feature description here

  Scenario: Item has been added after being selected
    # Enter steps here
  Given Amazon Open Page
    When Search table
    And Click any product
    And Click add to cart
    And Click add next
    Then Verify item is in cart