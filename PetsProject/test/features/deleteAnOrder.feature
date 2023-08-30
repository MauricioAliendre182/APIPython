@API
Feature: Delete a Pet Order

  @Acceptance @DeleteAPetOrder
  Scenario: Verify that the user can retrieve a pet order previosly created
    When a user deletes a pet order
    Then the status code is 200

  @Negative
  Scenario: Verify that the user can not retrieve an unexistant pet order
    When a user tries to delete an unexistant pet order
    Then the status code is 404