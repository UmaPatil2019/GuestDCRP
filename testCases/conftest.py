import os.path
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


# conftest file has data of most commony used. Optimization/code reusability
# This setup fixture is designed to perform some common setup steps that are applicable to all test cases in your suite.
# the driver and wait instances available to all the test methods within the test class. This is beneficial because it allows you to reuse the same WebDriver instance across multiple test methods, avoiding the overhead of creating a new WebDriver for each test method.
# removed get_application_url method from readProperties.py and added here
@pytest.fixture(autouse=True)  # applicable for all the packages/functions
def setup(
        request):


    # Use request when need to declare variables like wait, driver. The request object is automatically available in the context of a fixture function in Pytest. It provides information and methods related to the executing test.
    #wait_time_out = 5
    ## It initiates chrome webdriver,This line sets up a Chrome WebDriver using the webdriver_manager package to manage the ChromeDriver. It automatically downloads and installs the appropriate version of ChromeDriver.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    # This line navigates the WebDriver to the specified URL
    driver.get("https://designcrew-roomplanner-we.outwardinc.com/splash")
    driver.maximize_window()
    # Waiting for Continue as guest Button and Clicking:
    wait.until(EC.presence_of_element_located((By.XPATH, "//form[@class='login-form guest visible']//button[@class='login-item guest-button']"))).click()
    time.sleep(5)
    # Waiting to click Continue to RP button in what's new in RP mpdal"
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue to room planner']"))).click()
    # setting up request context. These lines make the driver and wait instances available in the context of the test class.
    request.cls.driver = driver  # assigns the WebDriver instance to the driver attribute of the test class.
    request.cls.wait = wait  # assigns the WebDriverWait instance to the wait attribute of the test class.

    yield
    # Teardown - Quitting WebDriver:
    driver.quit()


# to generate HTML reports add the following hook methods
@pytest.mark.optionalhook()
def pytest_configure(config):
    config._metadata['Project Name'] = 'GUEST DCRP'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Uma'


# It's hook to delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)


# specifying report folder location and save report with timestamp
# this avoids sending the html command in terminal everytiome
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"

# .......
# TO test in multiple browser use the following code and run in command line as
#
# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     elif browser == "edge":
#         pass #create edge related driver
#
#     elif browser == 'firefox':
#           return driver
# pass #create firefox related driver. #to pass chrome as a default browser, put it in else part. This works when none of the browsers
#
#
#
# following is the hook method, doesn't require calling
# def pytest_addoption(parser):
#     parser.addoption("--browser") # this will get the browser name from terminal command
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser") #this will return the browser name from addoption method to setup method


# To run test cases in Selenium with Python for the Safari browser, you need to use the webdriver.Safari() class. Here's a simple example of how you can set up a Selenium test case for Safari:
#
# python
# Copy code
# from selenium import webdriver
#
# # Create a Safari WebDriver instance
# driver = webdriver.Safari()
#
# # Navigate to a website
# driver.get("https://www.example.com")
#
# # Perform actions (e.g., click buttons, fill forms)
# # ...
#
# # Close the browser window
# driver.quit()
# Before running Selenium test cases with Safari, make sure you meet the following requirements:
#
# Enable Developer Menu in Safari:
#
# Open Safari.
# Go to Safari > Preferences.
# In the Advanced tab, check the "Show Develop menu in menu bar" option.
# Enable Remote Automation in Safari:
#
# In Safari, go to Develop > Allow Remote Automation.
# Install Selenium WebDriver:
#
# Ensure that you have the selenium package installed. You can install it using:
# bash
# Copy code
# pip install selenium
# Enable Safari Driver:
#
# Ensure that Safari WebDriver is enabled. You can enable it by going to Safari > Preferences > Advanced and checking the "Show Develop menu in menu bar" option. Then, go to Develop > Allow Remote Automation.
# Once you have met these requirements, you should be able to run your Selenium test cases with Safari.
#
# If you encounter any issues, such as WebDriver not being found, you might need to download the Safari WebDriver executable from the official SafariDriver releases page (https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) and specify its path when creating the WebDriver instance:
#
# python
# Copy code
# from selenium import webdriver
#
# # Path to Safari WebDriver executable
# safari_driver_path = '/path/to/safaridriver'
#
# # Create a Safari WebDriver instance with the specified path
# driver = webdriver.Safari(executable_path=safari_driver_path)
#
# # Navigate to a website
# driver.get("https://www.example.com")
#
# # Perform actions (e.g., click buttons, fill forms)
# # ...
#
# # Close the browser window
# driver.quit()
# Make sure to replace /path/to/safaridriver with the actual path to the Safari WebDriver executable on your system.


# .......
# For testing in specific browser, use following command
# pytest -v -s ./testCases/test_LoginASGuest.py --browser chrome

# For parallel testing, use following command
# pytest -v -s -n=3 ./testCases/test_LoginASGuest.py --browser chrome
