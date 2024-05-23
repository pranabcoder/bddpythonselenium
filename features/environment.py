from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration('basic info', 'browser')
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
