# Created by omar at 6/10/2021
Feature: Test UI elements of Amazon help page
  # Enter feature description here
  User checks the following scenarios on the help page and verifies
each scenario is about functional tab or search box or text.
#ui #1
  Scenario: User sees 'Hello What can we help you with'
    Given Open Amazon Page
     When  hello on page
     Then Verify if Hello. What ..help you with...

#ui #2
  Scenario: User sees 3 columns under 'Check Some things ..'
    When User sees 'Some things you can do here'
    Then Verify number of tabs is 3

#ui #3
  Scenario: User sees 'Search the help library' tab
    When User checks the search box
    Then Verify the search tab

  #ui #4
  Scenario: Browse Help Topics
    When dropdown 12 elements
    Then 12 elements are checked by loops


    #ui #5
  Scenario: Check Recommended Topics
    Then Verify tools icon


    #ui #6
  Scenario: Tools icon
    Then Check tools icon is present


