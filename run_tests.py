import subprocess
import argparse
from selenium import webdriver


def get_browser_version(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    version = driver.capabilities['browserVersion']
    driver.quit()
    return version


def run_behave_tests(feature_file=None, tags=None, browser=None):
    command = ["behave"]

    if feature_file:
        command.append(feature_file)

    if tags:
        command.extend(["--tags", tags])

    if browser:
        command.extend(["--define", f"BROWSER={browser}"])

    command.extend(["-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"])

    result = subprocess.run(command)
    if result.returncode != 0:
        raise Exception("Behave tests failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Behave tests with Allure reporting')
    parser.add_argument('--feature', type=str, help='The feature file to run')
    parser.add_argument('--tags', type=str, help='Tags to filter scenarios')
    parser.add_argument('--browser', type=str, help='Browser to use for tests')
    args = parser.parse_args()
    run_behave_tests(args.feature, args.tags, args.browser)
