@CreateUserWithArray
Feature: Verify the status code for the endpoint to create users using a array

  @Acceptance
  Scenario: Create a new user using a array
    When multiple users are created using a array
      | username     | firstName | lastName |         email         | password | phone     | userStatus |
      | usertest101  | User      | test101  | usertest101@test.com  | user101  | 123456789 |      0     |
      | usertest102  | User      | test102  | usertest102@test.com  | user102  | 123456789 |      0     |
      | usertest103  | User      | test103  | usertest103@test.com  | user103  | 123456789 |      0     |
    Then the status code is 200
