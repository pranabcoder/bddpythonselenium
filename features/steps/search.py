from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'I am on the homepage')
def step_impl(context):
    expected_title = 'Your Store'
    assert context.driver.title.__eq__(expected_title)


@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.form-control.input-lg').send_keys('HP')


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg').click()


@then(u'Valid product should be displayed in the search result')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.form-control.input-lg').send_keys('Honda')


@then(u'Proper message should be displayed in the search results')
def step_impl(context):
    expected_message = 'There is no product that matches the search criteria.'
    assert (context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
            .__eq__(expected_message))


@when(u'I don\'t enter anything into the search box field')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.form-control.input-lg').send_keys('')
