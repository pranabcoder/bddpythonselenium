from features.pages.BasePage import BasePage
from utilities import ConfigReader
from utilities.ElementActions import find_element_and_action


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option = "//span[text()='My Account']"
    login_option = 'Login'
    register_option = 'Register'
    expected_title = ConfigReader.read_configuration('basic info', 'application_title')
    search_bx_css = '.form-control.input-lg'
    search_button_css = '.btn.btn-default.btn-lg'

    def click_my_account(self):
        find_element_and_action(self.driver, 'xpath', self.my_account_option, 'click')

    def click_login(self):
        find_element_and_action(self.driver, 'link_text', self.login_option, 'click')

    def verify_title(self):
        expected_title = self.expected_title
        assert self.driver.title.__eq__(expected_title)

    def enter_product_into_search_box_field(self, product_name):
        find_element_and_action(self.driver, 'css_selector', self.search_bx_css, 'send_keys', product_name)

    def click_on_search_button(self):
        find_element_and_action(self.driver, 'css_selector', self.search_button_css, 'click')

    def click_register(self):
        find_element_and_action(self.driver, 'link_text', self.register_option, 'click')
