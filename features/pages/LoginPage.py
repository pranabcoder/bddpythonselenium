from features.pages.BasePage import BasePage
from utilities import ConfigReader
from utilities.ElementActions import find_element_and_action


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = 'input-email'
    password_field_id = 'input-password'
    login_button_css = 'input[value="Login"]'
    warning_message_css = '.alert.alert.alert-danger.alert-dismissible'
    login_warning_message = ConfigReader.read_configuration('login page info', 'warning_message')

    def enter_email_address(self, email_address):
        find_element_and_action(self.driver, 'id', self.email_address_field_id, 'send_keys', email_address)

    def enter_password(self, password):
        find_element_and_action(self.driver, 'id', self.password_field_id, 'send_keys', password)

    def click_login_button(self):
        find_element_and_action(self.driver, 'css_selector', self.login_button_css, 'click')

    def login_to_application(self, email_address, password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_warning_message(self):
        expected_error_message = self.login_warning_message
        assert (find_element_and_action(self.driver, 'css_selector', self.warning_message_css, 'get_text')
                .__contains__(expected_error_message))