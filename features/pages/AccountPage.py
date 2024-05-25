from features.pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    edit_account_information_link_text = 'Edit your account information'

    def is_edit_account_information_link_displayed(self):
        assert self.find_element_and_action('link_text', self.edit_account_information_link_text,
                                            'is_displayed')
