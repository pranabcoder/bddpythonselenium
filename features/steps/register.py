from behave import given, when, then
from selenium.webdriver.common.by import By
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.register_page = RegisterPage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_register()


@when(u'I fill in the mandatory fields')
def step_impl(context):
    context.register_page.enter_first_name('Pranab')
    context.register_page.enter_last_name('Ghosh')
    context.register_page.enter_email('pranabtesteight@test.com')
    context.register_page.enter_telephone('1234567')
    context.register_page.enter_password('12345')
    context.register_page.enter_confirm_password('12345')
    context.register_page.click_agree_checkbox()


@when(u'I click on register button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()


@then(u'I should see the success message')
def step_impl(context):
    expected_message = 'Your Account Has Been Created!'
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(expected_message)


@when(u'I fill in all the fields')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#input-firstname').send_keys('Pranab')
    context.driver.find_element(By.CSS_SELECTOR, '#input-lastname').send_keys('Ghosh')
    context.driver.find_element(By.CSS_SELECTOR, '#input-email').send_keys('pranabtestseven@gmail.com')
    context.driver.find_element(By.CSS_SELECTOR, '#input-telephone').send_keys('1234567')
    context.driver.find_element(By.CSS_SELECTOR, '#input-password').send_keys('12345')
    context.driver.find_element(By.CSS_SELECTOR, '#input-confirm').send_keys('12345')
    context.driver.find_element(By.CSS_SELECTOR, "input[value='1'][name='newsletter']").click()
    context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@when(u'I enter details into all fields except email')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#input-firstname').send_keys('Pranab')
    context.driver.find_element(By.CSS_SELECTOR, '#input-lastname').send_keys('Ghosh')
    context.driver.find_element(By.CSS_SELECTOR, '#input-telephone').send_keys('1234567')
    context.driver.find_element(By.CSS_SELECTOR, '#input-password').send_keys('12345')
    context.driver.find_element(By.CSS_SELECTOR, '#input-confirm').send_keys('12345')
    context.driver.find_element(By.CSS_SELECTOR, "input[value='1'][name='newsletter']").click()
    context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@when(u'I enter existing email address into email field')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#input-email').send_keys('pranabtestwo@gmail.com')


@then(u'I should see the error message')
def step_impl(context):
    expected_message = 'Warning: E-Mail Address is already registered!'
    assert (context.driver.find_element(By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible').text
            .__contains__(expected_message))


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#input-firstname').send_keys('')
    context.driver.find_element(By.CSS_SELECTOR, '#input-lastname').send_keys('')
    context.driver.find_element(By.CSS_SELECTOR, '#input-email').send_keys('')
    context.driver.find_element(By.CSS_SELECTOR, '#input-telephone').send_keys('')
    context.driver.find_element(By.CSS_SELECTOR, '#input-password').send_keys('')
    context.driver.find_element(By.CSS_SELECTOR, '#input-confirm').send_keys('')


@then(u'I should see the error message for all the mandatory fields')
def step_impl(context):
    expected_privacy_warning = 'Warning: You must agree to the Privacy Policy!'
    expected_first_name_warning = 'First Name must be between 1 and 32 characters!'
    expected_last_name_warning = 'Last Name must be between 1 and 32 characters!'
    expected_email_warning = 'E-Mail Address does not appear to be valid!'
    expected_telephone_warning = 'Telephone must be between 3 and 32 characters!'
    expected_password_warning = 'Password must be between 4 and 20 characters!'
    assert (context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
            .__contains__(expected_privacy_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text
            .__contains__(expected_first_name_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text
            .__contains__(expected_last_name_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text
            .__contains__(expected_email_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text
            .__contains__(expected_telephone_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text
            .__contains__(expected_password_warning))

