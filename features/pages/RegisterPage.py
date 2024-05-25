from features.pages.BasePage import BasePage
from utilities import ConfigReader


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.warning_message = None
        self.success_message = None

    first_name_field_css = '#input-firstname'
    last_name_field_css = '#input-lastname'
    email_field_css = '#input-email'
    telephone_field_css = '#input-telephone'
    password_field_css = '#input-password'
    confirm_password_field_css = '#input-confirm'
    subscribe_yes_radio_css = 'input[name="newsletter"][value="1"]'
    subscribe_no_radio_css = 'input[name="newsletter"][value="0"]'
    agree_checkbox_xpath = "//input[@name='agree']"
    continue_button_css = '.btn.btn-primary'
    register_success_message_xpath = "//div[@id='content']/h1"
    error_message_css = '.alert.alert-danger.alert-dismissible'
    register_success_message = ConfigReader.read_configuration('register page info', 'success_message')
    email_already_exists_warning_message = ConfigReader.read_configuration('register page info',
                                                                           'email_already_exists_warning_message')
    first_name_field_warning_message = ConfigReader.read_configuration('register page info',
                                                                       'first_name_warning')
    last_name_field_warning_message = ConfigReader.read_configuration('register page info',
                                                                      'last_name_warning')
    email_field_warning_message = ConfigReader.read_configuration('register page info',
                                                                  'email_warning')
    telephone_field_warning_message = ConfigReader.read_configuration('register page info',
                                                                      'telephone_warning')
    password_field_warning_message = ConfigReader.read_configuration('register page info',
                                                                     'password_warning')
    first_name_field_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_field_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_field_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_field_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_field_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name):
        self.find_element_and_action('css_selector',
                                     self.first_name_field_css, 'send_keys', first_name)

    def enter_last_name(self, last_name):
        self.find_element_and_action('css_selector',
                                     self.last_name_field_css, 'send_keys', last_name)

    def enter_email(self, email):
        self.find_element_and_action('css_selector',
                                     self.email_field_css, 'send_keys', email)

    def enter_telephone(self, telephone):
        self.find_element_and_action('css_selector',
                                     self.telephone_field_css, 'send_keys', telephone)

    def enter_password(self, password):
        self.find_element_and_action('css_selector',
                                     self.password_field_css, 'send_keys', password)

    def enter_confirm_password(self, confirm_password):
        self.find_element_and_action('css_selector',
                                     self.confirm_password_field_css, 'send_keys', confirm_password)

    def click_subscribe_yes(self):
        self.find_element_and_action('css_selector',
                                     self.subscribe_yes_radio_css, 'click')

    def click_subscribe_no(self):
        self.find_element_and_action('css_selector',
                                     self.subscribe_no_radio_css, 'click')

    def click_agree_checkbox(self):
        self.find_element_and_action('xpath',
                                     self.agree_checkbox_xpath, 'click')

    def click_continue_button(self):
        self.find_element_and_action('css_selector',
                                     self.continue_button_css, 'click')

    def verify_register_success_message(self):
        self.success_message = self.find_element_and_action('xpath',
                                                            self.register_success_message_xpath, 'get_text')
        print(self.success_message)
        assert self.success_message.__contains__(self.register_success_message)

    def verify_email_already_exists_warning_message(self):
        self.warning_message = self.find_element_and_action('css_selector',
                                                            self.error_message_css, 'get_text')
        assert self.warning_message.__contains__(self.email_already_exists_warning_message)

    def verify_all_mandatory_fields_warning_message(self):
        assert (self.find_element_and_action('xpath',
                                             self.first_name_field_warning_xpath, 'get_text')
                .__contains__(self.first_name_field_warning_message))
        assert (self.find_element_and_action('xpath',
                                             self.last_name_field_warning_xpath, 'get_text')
                .__contains__(self.last_name_field_warning_message))
        assert (self.find_element_and_action('xpath',
                                             self.email_field_warning_xpath, 'get_text')
                .__contains__(self.email_field_warning_message))
        assert (self.find_element_and_action('xpath',
                                             self.telephone_field_warning_xpath, 'get_text')
                .__contains__(self.telephone_field_warning_message))
        assert (self.find_element_and_action('xpath',
                                             self.password_field_warning_xpath, 'get_text')
                .__contains__(self.password_field_warning_message))
