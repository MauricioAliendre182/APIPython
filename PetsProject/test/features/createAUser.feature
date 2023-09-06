@API
Feature: Create a User

  @Acceptance @CreateAUser
  Scenario: Verify that a user can be created correctly
    When a user creates a user in the pet store
      | id | username | firstName | lastName | email            | password | phone   | userStatus |
      | 1  | maps182  | Gonzalo   | Guedes   | gonchi@gmail.com | gonza123 | 7686886 | 1          |
    Then the status code is 200

  @Negative @CreateAUser
  Scenario: Verify that a user can not create a user with string in the status user field
    When a user creates a user in the pet store
      | id | username | firstName | lastName | email            | password | phone   | userStatus |
      | 1  | maps182  | Gonzalo   | Guedes   | gonchi@gmail.com | gonza123 | 7686886 | "dskkds"   |
    Then the status code is 400

  @Negative @CreateAUser
  Scenario: Verify that a user can not create a user with a string in the ID field
    When a user creates a user in the pet store
      | id       | username | firstName | lastName | email            | password | phone   | userStatus |
      | "dsdsd"  | maps182  | Gonzalo   | Guedes   | gonchi@gmail.com | gonza123 | 7686886 | 3          |
    Then the status code is 400

