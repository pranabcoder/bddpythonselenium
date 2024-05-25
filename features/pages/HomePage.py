from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage
from utilities import ConfigReader


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
        self.find_element_and_action('xpath', self.my_account_option, 'click')

    def click_login(self):
        self.find_element_and_action('link_text', self.login_option, 'click')
        return LoginPage(self.driver)

    def verify_title(self):
        expected_title = self.expected_title
        assert self.verify_page_title(expected_title)

    def enter_product_into_search_box_field(self, product_name):
        self.find_element_and_action('css_selector', self.search_bx_css, 'send_keys', product_name)

    def click_on_search_button(self):
        self.find_element_and_action('css_selector', self.search_button_css, 'click')
        return SearchPage(self.driver)

    def click_register(self):
        self.find_element_and_action('LINK_TEXT', self.register_option, 'click')
        return RegisterPage(self.driver)
