Feature: OrangeHRM Login

  Scenario: User successfully login
    Given launch chrome browser
    When open pokemon page
    And click CTA "Pokédex"
    And search Pokemon "Pikachu"
    And select "Pikachu"
    Then scrolling down to show all detail about "Pikachu"
    And click CTA "Explore More Pokemon"
    And scrolling down to show all pokemon
    And close browser
