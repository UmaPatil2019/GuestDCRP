import os.path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from datetime import datetime

@pytest.fixture(autouse=True) #applicable for all the packages/functions
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

#to generate HTML reports add the following hook methods
@pytest.mark.optionalhook()
def pytest_configure(config):
    config._metadata['Project Name'] = 'GUEST DCRP'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Uma'

#It's hook to delete/modift environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)

# specifying report folder location and save report with timestamp
#this avoids sending the html command in terminal everytiome
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

# .......
#TO test in multiple browser use the following code and run in command line as
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


#.......
# For testing in specific browser, use following command
# pytest -v -s ./testCases/test_LoginASGuest.py --browser chrome

#For parallel testing, use following command
# pytest -v -s -n=3 ./testCases/test_LoginASGuest.py --browser chrome



