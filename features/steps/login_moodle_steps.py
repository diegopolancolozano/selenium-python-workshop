from behave import given, when, then
from selenium import webdriver
from pages.login_moodle_page import LoginMoodlePage
from pages.dashboard_page import DashboardPage
#from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@given('the user is on the moodle login page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.LoginMoodlePage = LoginMoodlePage(context.driver)

@when('the user logs in with valid credentials in moodle login')
def step_when_user_logs_in_valid(context):
    context.LoginMoodlePage.login("Usuario", "Contraseña") #No voy a poner mis datos en git público

@then('the user should be redirected to the moodle dashboard page')
def step_then_dashboard_page(context):
    dashboardPage = DashboardPage(context.driver)
    assert dashboardPage.isTopBarDisplayed()