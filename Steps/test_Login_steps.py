import time

import pytest
from pytest_bdd.steps import * 
from pytest_bdd import scenario, parsers, scenarios
from Pages.HomePages import HomePage
from Pages.dashboard import DashboardPage
from Pages.Login import LoginPage
from Pages.Logout import LogoutPage
from Pages.User import UserPage

scenarios("../Features/OrangHRM.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def logout_page(driver):
    return LogoutPage(driver)

@pytest.fixture
def user_page(driver):
    return UserPage(driver)




@given("I am on the login page of Orange HRM Application")
def verify_user_on_login_page(login_page):
    login_page.open_application()


@when(parsers.parse("User logs with {Username} user"))
def enter_username_for_login(login_page, Username):
    login_page.enter_username(Username)


@when(parsers.parse("User enters password {Password}"))
def enter_password(login_page, Password):
    login_page.enter_password(Password)


@when("I click on login button")
def click_login_button(login_page):
    login_page.click_login_button()
    time.sleep(5)


@when(parsers.parse("I validate User redirected to Orange HRM Home page"))
def validate_homePage(home_page):
    home_page.validate_homePage()
    time.sleep(3)


@when (parsers.parse("I click on Admin option from left navigation panel"))
def click_on_Admin_Button(home_page):
    home_page.Click_on_Admin()

@when(parsers.parse("I enter {Username} as search criteria as in the username textfield")) 
def enterThe_data_In_UsernameTextbar(user_page,Username):
    user_page.enterUsername_to_The_searchBox(Username)

@when (parsers.parse("I click on Search button")) 
def click_To_Search_Button(user_page):
    user_page.click_on_Search()
    
@when(parsers.parse("I click on logout button"))
def logout_To_Application(logout_page):
    logout_page.clickonProgfileIcone()
    logout_page.clickon_Logout()
    time.sleep(2)

@then (parsers.parse("I validate Admin record is displayed in search results"))  
def validate_record(user_page):
    user_page.validate_user()
      
       
@then(parsers.parse("I click on edit button from displayed record"))
def click_on_edit(user_page):
    user_page.click_on_Edit_button()
   
@when(parsers.parse("I change user role from Admin to ESS"))
def change_admin_ess(user_page):
    user_page.select_ess()   


@when(parsers.parse("I click on Save button"))
def click_on_save_button(user_page):
    user_page.click_save()

@then(parsers.parse("I validate popup {massage}"))
def validate_popup(user_page,massage):
    user_page.popupvalidation(massage)    