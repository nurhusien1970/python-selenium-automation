# Created by omar at 6/15/2021
Feature: Whole foods Amazon
  # Enter feature description here
  Check price is regular and product item has a name. If locator length is four then all items have regular, discount,
  item label, and animal welfare certified.


  Scenario: Whole foods regular price
    # Enter steps here
  Given Wholefoods Page
    Then If locator list is 5 for any bottom item
