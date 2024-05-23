from features.pages.BasePage import BasePage
from utilities import ConfigReader
from utilities.ElementActions import find_element_and_action


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = 'HP LP3065'
    error_message_xpath = "//input[@id='button-search']/following-sibling::p"
    error_message = ConfigReader.read_configuration('search page info', 'error_message')

    def display_status_of_valid_product(self):
        assert find_element_and_action(self.driver, 'link_text', self.valid_product_link_text, 'is_displayed')

    def display_error_message(self):
        get_error_text = find_element_and_action(self.driver, 'xpath', self.error_message_xpath, 'get_text')
        print(get_error_text)
        assert get_error_text.__eq__(self.error_message)
