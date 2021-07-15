# Created by omar at 7/11/2021
Feature: User selects from drop down department selection
  Go to amazon department search drop down and click and select department

  #Scenario:Select department store for computers
   # Given Amazon Open Page
  #  And click the department dropdown
  #  Then Select store for computers

  Scenario:Select department store for computers
    Given Amazon Open Page
    When from the department dropdown select computers
    And Search for HP
    Then verify you selected store for computers

  Scenario:Select department store for products by hovering first New Arrivals
    Given Amazon Open Product Page
      When hover over the New Arrivals
      Then Verify for New Arrivals
