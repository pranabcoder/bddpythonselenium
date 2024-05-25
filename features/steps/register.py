from behave import given, when, then
from features.pages.HomePage import HomePage


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.register_page = context.home_page.click_register()


@when(u'I fill in the mandatory fields')
def step_impl(context):
    for registration_data in context.table:
        context.register_page.enter_first_name(registration_data['first_name'])
        context.register_page.enter_last_name(registration_data['last_name'])
        context.register_page.enter_email(registration_data['email'])
        context.register_page.enter_telephone(registration_data['telephone'])
        context.register_page.enter_password(registration_data['password'])
        context.register_page.enter_confirm_password(registration_data['confirm_password'])
        context.register_page.click_agree_checkbox()


@when(u'I click on register button')
def step_impl(context):
    context.register_page.click_continue_button()


@then(u'I should see the success message')
def step_impl(context):
    context.register_page.verify_register_success_message()


@when(u'I fill in all the fields')
def step_impl(context):
    for registration_data in context.table:
        context.register_page.enter_first_name(registration_data['first_name'])
        context.register_page.enter_last_name(registration_data['last_name'])
        context.register_page.enter_email(registration_data['email'])
        context.register_page.enter_telephone(registration_data['telephone'])
        context.register_page.enter_password(registration_data['password'])
        context.register_page.enter_confirm_password(registration_data['confirm_password'])
        context.register_page.click_subscribe_yes()
        context.register_page.click_agree_checkbox()


@when(u'I enter details into all fields except email')
def step_impl(context):
    for registration_data in context.table:
        context.register_page.enter_first_name(registration_data['first_name'])
        context.register_page.enter_last_name(registration_data['last_name'])
        context.register_page.enter_telephone(registration_data['telephone'])
        context.register_page.enter_password(registration_data['password'])
        context.register_page.enter_confirm_password(registration_data['confirm_password'])
        context.register_page.click_subscribe_yes()
        context.register_page.click_agree_checkbox()


@when(u'I enter existing email address into email field')
def step_impl(context):
    for registration_data in context.table:
        context.register_page.enter_email(registration_data['email'])


@then(u'I should see the error message')
def step_impl(context):
    context.register_page.verify_email_already_exists_warning_message()


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name('')
    context.register_page.enter_last_name('')
    context.register_page.enter_email('')
    context.register_page.enter_telephone('')
    context.register_page.enter_password('')
    context.register_page.enter_confirm_password('')


@then(u'I should see the error message for all the mandatory fields')
def step_impl(context):
    context.register_page.verify_all_mandatory_fields_warning_message()

