  #  created by - <Vikasratna>
    #  Date - 10/11/2023
    #  Name: Orange HRM Application


Feature: Orange HRM Application Tests

    Background:
        Given I am on the login page of Orange HRM Application

    @smoke1
    Scenario Outline: Verify User login successfully
        When User logs with <Username> user
        And User enters password <Password>
        And I click on login button
        When I validate User redirected to Orange HRM Home page
        And I click on logout button
      Examples:
        |Username  |Password|
        | Admin    |admin123|

    @smoke2
    Scenario Outline: Verify System users search Functionality
        When User logs with <Username> user
        And User enters password <Password>
        And I click on login button
        When I validate User redirected to Orange HRM Home page
        When I click on Admin option from left navigation panel
        And I enter <Username> as search criteria as in the username textfield
        And I click on Search button
        Then I validate Admin record is displayed in search results
        When I click on logout button
    Examples:
      |Username  |Password|
      | Admin    |admin123|
    
    @smoke3
    Scenario Outline: Verify Edit user role functinality
        When User logs with <Username> user
        And User enters password <Password>
        And I click on login button
        When I validate User redirected to Orange HRM Home page
        And I click on Admin option from left navigation panel
        And I enter <Username> as search criteria as in the username textfield
        And I click on Search button
        Then I validate Admin record is displayed in search results
        And I click on edit button from displayed record
        When I change user role from Admin to ESS
        And I click on Save button
        Then I validate popup <massage>
        When I click on logout button
    Examples:
      |Username  |Password|   massage |
      | Admin    |admin123| Successfully updated |

