@API
Feature: Retrieve a pet order

  @Acceptance @RetrieveAPetOrder
  Scenario: Verify that the user can retrieve a pet order previosly created
    When a user retrieves a pet order
    Then the status code is 200

  @Negative
  Scenario: Verify that the user can not retrieve an unexistant pet order
    When a user tries to retrieve an unexistant pet order
    Then the status code is 404