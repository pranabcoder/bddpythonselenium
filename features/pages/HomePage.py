from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from utilities.ElementActions import find_element_and_action


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option = "//span[text()='My Account']"
    login_option = 'Login'

    def click_my_account(self):
        find_element_and_action(self.driver, 'xpath', self.my_account_option, 'click')

    def click_login(self):
        find_element_and_action(self.driver, 'link_text', self.login_option, 'click')