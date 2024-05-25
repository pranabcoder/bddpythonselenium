from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locator_strategy, locator_value, timeout=10):
        locator = getattr(By, locator_strategy.upper())
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator, locator_value))
        )

    def find_element_and_action(self, locator_strategy, locator_value, action, *args):
        try:
            locator = getattr(By, locator_strategy.upper())
            print(locator, locator_value)
            element = self.driver.find_element(locator, locator_value)

            if action == "click":
                element.click()
            elif action == "send_keys":
                element.clear()
                element.send_keys(*args)
            elif action == "is_displayed":
                return element.is_displayed()
            elif action == "get_text":
                return element.text

        except NoSuchElementException:
            raise NoSuchElementException(f"Element not found with locator: {locator_strategy}={locator_value}")

    def verify_page_title(self, expected_title):
        return self.driver.title == expected_title
