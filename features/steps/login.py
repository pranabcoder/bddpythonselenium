from behave import given, when, then
from features.pages.HomePage import HomePage


@given(u'I am on the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.login_page = context.home_page.click_login()


@when(u'I enter valid username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_email_address(username)
    context.login_page.enter_password(password)


@when(u'I click on the login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'I should be redirected to the home page')
def step_impl(context):
    context.account_page.is_edit_account_information_link_displayed()


@when(u'I enter invalid username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_email_address(username)
    context.login_page.enter_password(password)


@then(u'I should see an error message')
def step_impl(context):
    context.login_page.verify_login_warning_message()


@when(u'I enter empty username and password')
def step_impl(context):
    context.login_page.enter_email_address('')
    context.login_page.enter_password('')
