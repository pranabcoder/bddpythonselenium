from behave import given, when, then
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I am on the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_login()
    context.login_page = LoginPage(context.driver)
    context.account_page = AccountPage(context.driver)


@when(u'I enter valid username and password')
def step_impl(context):
    context.login_page.enter_email_address('pranabtest@gmail.com')
    context.login_page.enter_password('1234')


@when(u'I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(u'I should be redirected to the home page')
def step_impl(context):
    context.account_page.is_edit_account_information_link_displayed()


@when(u'I enter invalid username and password')
def step_impl(context):
    context.login_page.enter_email_address('pranabtest@gmail.com')
    context.login_page.enter_password('123456')


@then(u'I should see an error message')
def step_impl(context):
    context.login_page.verify_login_warning_message()


@when(u'I enter empty username and password')
def step_impl(context):
    context.login_page.enter_email_address('')
    context.login_page.enter_password('')
