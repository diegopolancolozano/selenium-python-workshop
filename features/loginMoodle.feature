Feature: Login moodle Feature
  Scenario: Successful login with valid credentials
    Given the user is on the moodle login page
    When the user logs in with valid credentials in moodle login
    Then the user should be redirected to the moodle dashboard page
