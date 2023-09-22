@EditAUser
Feature: Verify the status code for the endpoint to edit a user

  @Acceptance
  Scenario: Edit a user created
    When the user edit the information of a user
      | username     | firstName | lastName |         email         | password | phone     | userStatus |
      | usertest102  | User      | test102  | usertest102@test.com  | user102  | 123456789 |      0     |
    Then the status code is 200