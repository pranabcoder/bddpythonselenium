from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def find_element_and_action(driver, locator_strategy, locator_value, action, *args):
    try:
        locator = getattr(By, locator_strategy.upper())
        element = driver.find_element(locator, locator_value)

        if action == "click":
            element.click()
        elif action == "send_keys":
            element.send_keys(*args)
        elif action == "is_displayed":
            return element.is_displayed()
        elif action == "get_text":
            return element.text

    except NoSuchElementException:
        raise NoSuchElementException(f"Element not found with locator: {locator_strategy}={locator_value}")
