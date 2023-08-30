@API
Feature: Create a pet order

  @Acceptance @CreateAPetOrder
  Scenario: Verify that a user can store a pet order correctly
    When a user stores a pet order
      |id_order| id_pet | quantity | status | complete |
      |   1    |   1    |    30    | placed | True     |
    Then the status code is 200

  @Negative
  Scenario: Verify that a user can not store a pet order with an unexistant pet ID
    When a user stores a pet order
      |id_order| id_pet | quantity | status | complete |
      |        |   1    |    30    | placed | True     |
    Then the status code is 400

  @Negative
  Scenario: Verify that the user can not modify the status field with other string
    When a user stores a pet order
    |id_order| id_pet | quantity | status | complete |
    |   1    |   1    |    30    | jjfjdj | True     |
    Then the status code is 400