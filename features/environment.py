import platform
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from run_tests import get_browser_version
from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = context.config.userdata.get("BROWSER")
    if not browser_name:
        browser_name = ConfigReader.read_configuration('basic info', 'browser')
    browser_name = browser_name.lower()
    browser_version = get_browser_version(browser_name)
    os_name = platform.system()
    os_version = platform.release()
    with open('allure-results/environment.properties', 'w') as f:
        f.write(f"Browser={browser_name}\n")
        f.write(f"Browser.Version={browser_version}\n")
        f.write(f"OS={os_name}\n")
        f.write(f"OS.Version={os_version}\n")
    browser_options = {
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "chrome": ChromeOptions()
    }
    if browser_name.__eq__('chrome'):
        browser_options['chrome'].add_argument('--incognito')
        context.driver = webdriver.Chrome(options=browser_options['chrome'])
    elif browser_name.__eq__('firefox'):
        browser_options['firefox'].add_argument("-private")
        context.driver = webdriver.Firefox(options=browser_options['firefox'])
    elif browser_name.__eq__('edge'):
        browser_options['edge'].add_argument("--inprivate")
        context.driver = webdriver.Edge(options=browser_options['edge'])
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration('basic info', 'url'))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    allure.attach(context.driver.get_screenshot_as_png(), name=step.name, attachment_type=allure.attachment_type.PNG)
