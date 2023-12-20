import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.base_driver import BaseDriver
class getstartedPage():
    #locators for Get started page web elements like IG , empty Plan, My Portfolio
    IG_xpath = "//p[text()='Inspiration Gallery']"
    Empty_plan_xpath = "//p[text()='Empty Plan']"
    My_Portfolio_xpath = "//p[text()='My Portfolio']"


    def __init__(self, driver):
        self.driver = driver #this driver is coming from test_login

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    #method to go to IG
    def clickIG(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.IG_xpath))).click()


    #action method to go to empty plan modal
    # def clickEmptyPlan(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable((By.XPATH, self.Empty_plan_xpath))).click()
    #
    # #action method to go to Portfolio
    # def clickPortfolio(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable((By.XPATH, self.My_Portfolio_xpath))).click()
    #
    #
    #
    #
    #






