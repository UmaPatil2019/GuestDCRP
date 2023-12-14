import os.path
import time

from pageObjects.Login import loginPage
from pageObjects.Whats_NewModal import landingPage
from pageObjects.Get_StartedPage import getstartedPage
from pageObjects.My_Portfolio import myPortfolio
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Portfolio:
    baseURL = ReadConfig.getApplicationURL()
    # create a logger object for LogGen class.loggen method
    logger = LogGen.loggen()

    def test_MyPortfolio(self, setup):
        self.logger.info("**** Navigate to My Portfolio ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

