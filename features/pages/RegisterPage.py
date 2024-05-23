from features.pages.BasePage import BasePage
from utilities.ElementActions import find_element_and_action


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_css = '#input-firstname'
    last_name_field_css = '#input-lastname'
    email_field_css = '#input-email'
    telephone_field_css = '#input-telephone'
    password_field_css = '#input-password'
    confirm_password_field_css = '#input-confirm'
    subscribe_yes_radio_css = 'input[name="newsletter"][value="1"]'
    subscribe_no_radio_css = 'input[name="newsletter"][value="0"]'
    agree_checkbox_xpath = "//input[@name='agree']"
    continue_button_css = 'input[type="submit"]'

    def enter_first_name(self, first_name):
        find_element_and_action(self.driver, 'css_selector',
                                self.first_name_field_css, 'send_keys', first_name)

    def enter_last_name(self, last_name):
        find_element_and_action(self.driver, 'css_selector',
                                self.last_name_field_css, 'send_keys', last_name)

    def enter_email(self, email):
        find_element_and_action(self.driver, 'css_selector',
                                self.email_field_css, 'send_keys', email)

    def enter_telephone(self, telephone):
        find_element_and_action(self.driver, 'css_selector',
                                self.telephone_field_css, 'send_keys', telephone)

    def enter_password(self, password):
        find_element_and_action(self.driver, 'css_selector',
                                self.password_field_css, 'send_keys', password)

    def enter_confirm_password(self, confirm_password):
        find_element_and_action(self.driver, 'css_selector',
                                self.confirm_password_field_css, 'send_keys', confirm_password)

    def click_subscribe_yes(self):
        find_element_and_action(self.driver, 'css_selector',
                                self.subscribe_yes_radio_css, 'click')

    def click_subscribe_no(self):
        find_element_and_action(self.driver, 'css_selector',
                                self.subscribe_no_radio_css, 'click')

    def click_agree_checkbox(self):
        find_element_and_action(self.driver, 'css_selector',
                                self.agree_checkbox_xpath, 'click')

    def click_continue_button(self):
        find_element_and_action(self.driver, 'css_selector',
                                self.continue_button_css, 'click')