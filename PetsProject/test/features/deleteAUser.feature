@DeleteAUser
Feature: Delete a user created previously

  @Acceptance
  Scenario: delete a user
    When a user delete a user created previously
    Then the status code is 200
