from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage
from utilities import ConfigReader


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = 'input-email'
    password_field_id = 'input-password'
    login_button_css = 'input[value="Login"]'
    warning_message_css = '.alert.alert.alert-danger.alert-dismissible'
    login_warning_message = ConfigReader.read_configuration('login page info', 'warning_message')

    def enter_email_address(self, email_address):
        self.find_element_and_action('id', self.email_address_field_id, 'send_keys', email_address)

    def enter_password(self, password):
        self.find_element_and_action('id', self.password_field_id, 'send_keys', password)

    def click_login_button(self):
        self.find_element_and_action('css_selector', self.login_button_css, 'click')
        return AccountPage(self.driver)

    def login_to_application(self, email_address, password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_warning_message(self):
        expected_error_message = self.login_warning_message
        assert (self.find_element_and_action('css_selector', self.warning_message_css, 'get_text')
                .__contains__(expected_error_message))