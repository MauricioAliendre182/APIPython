@GetAUser
Feature: Retrieve the information of a single user created previously

  @Acceptance
  Scenario: retrieve the information of a user
    When a user retrieve the information of a user created
    Then the status code is 200

