# Created by omar at 6/9/2021
Feature: # Count Amazon Best Sellers clickable link boxes
  # Enter feature description here

  Scenario: Amazon Best sellers navigation link boxes
    # Enter steps here
Given best Amazon sellers page

    Scenario: Amazon Best sellers navigation link boxes LOOP
      Given best Amazon sellers page
      When Find Best sellers tabs
      Then Verify 5 boxes are present
      Then loop 5 links and verify they match the side menu text