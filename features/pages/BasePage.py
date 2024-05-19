from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locator_strategy, locator_value, timeout=10):
        locator = getattr(By, locator_strategy.upper())
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator, locator_value))
        )