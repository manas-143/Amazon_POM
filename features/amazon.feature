Feature: Amazon laptop purchase
  Scenario Outline: Search for laptops,add to cart and verify the total price
    Given User is on the amazon website search for "<items>"
    When User filter by ratings
    And add top "<numbers>" laptops to the cart
    Then the total amount in the cart should match the laptop prices
    Examples:
      |   items    |   numbers   |
      | hp laptops |     3       |
      |dell laptops|     4       |
      |acer laptops|     5       |

