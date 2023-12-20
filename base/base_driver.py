import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = W(self.driver, 10)

    def wait_presence_of_element_located(self, locator_type, locator):
        presence_element_wait = self.wait_variable.until(EC.presence_of_element_located((locator_type, locator)))
        return presence_element_wait

    def wait_visiblility_of_all_elements_located(self, locator_type, locator):
        visibility_elements_wait = self.wait_variable.until(EC.visibility_of_all_elements_located((locator_type, locator)))
        return visibility_elements_wait
