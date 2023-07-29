@tag
Feature: Verify the status code of CRUD requests in Petstore

  @CreateAPet
  Scenario: Create a pet
    When a user creates a pet
    Then the status code is correct

  @RetrieveAPet
  Scenario: Verify Get status code
    When a user retrieves a pet
    Then the status code is correct

  @UpdateAPet
  Scenario: Verify Put status code
    When a user updates a pet
    Then the status code is correct

  @DeleteAPet
  Scenario: Verify Delete status code
    When a user deletes a pet
    Then the status code is correct