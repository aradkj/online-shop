Feature: Online Shop

  Scenario: Customer creates a product
    Given the shop is running
    When I create a product
    Then the product should be available