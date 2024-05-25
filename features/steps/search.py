from behave import given, when, then
from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I am on the homepage')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.verify_title()


@when(u'I enter valid product into the search box field')
def step_impl(context):
    for search_data in context.table:
        context.home_page.enter_product_into_search_box_field(search_data['product_name'])


@when(u'I click on search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid product should be displayed in the search result')
def step_impl(context):
    context.search_page.display_status_of_valid_product()


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    for search_data in context.table:
        context.home_page.enter_product_into_search_box_field(search_data['product_name'])


@then(u'Proper message should be displayed in the search results')
def step_impl(context):
    context.search_page.display_error_message()


@when(u'I don\'t enter anything into the search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field('')
