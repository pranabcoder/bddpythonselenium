from features.pages.BasePage import BasePage
from utilities import ConfigReader


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_error_text = None

    valid_product_link_text = 'HP LP3065'
    error_message_xpath = "//input[@id='button-search']/following-sibling::p"
    error_message = ConfigReader.read_configuration('search page info', 'error_message')

    def display_status_of_valid_product(self):
        assert self.find_element_and_action('link_text', self.valid_product_link_text, 'is_displayed')

    def display_error_message(self):
        self.get_error_text = self.find_element_and_action('xpath', self.error_message_xpath, 'get_text')
        print(self.get_error_text)
        assert self.get_error_text.__eq__(self.error_message)
