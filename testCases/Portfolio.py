import os.path
import time

import pytest

from pageObjects.Login import loginPage
from pageObjects.Whats_NewModal import landingPage
from pageObjects.Get_StartedPage import getstartedPage
from test_LoginASGuest import Test_login
from pageObjects.My_Portfolio import myPortfolio
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# class Test_Portfolio:
#     baseURL = ReadConfig.getApplicationURL()
#     # create a logger object for LogGen class.loggen method
#     logger = LogGen.loggen()
#
#
#
#     @pytest.mark.sanity
#     def test_MyPortfolio(self, setup):
#         self.logger.info("**** Navigate to My Portfolio ****")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         # Instantiate an object of the Test_login class
#         login_test_obj = Test_login()
#
#         # Call the test_login method on the Test_login object
#         login_test_obj.test_login(self.driver)
#
#
#
#         # Open Create New Plan modal from Edit menu by hovering over
#         # create an object for myPortfolio class, invoke My_portfolio methods(clickonNewPlan() and newPlanModalMsg())
#         self.Portfolio = myPortfolio(self.driver)
#         self.Portfolio.clickonNewPlan()
#         self.PlanName_header_text = self.Portfolio.newPlanModalMsg()
#
#         # validation to confirm new plan modal is diplayed by checking, modal text by invoking newPlanModalMsg() method
#         if self.PlanName_header_text == "Create New Plan":
#             self.logger.info("****Create New Plan modal displayed****")
#             print(self.PlanName_header_text)
#             assert True
#         # else part is giving error, when added, by default else part is executed
#         # else:
#         #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//" + "test_login2.png")
#         #     self.logger.error("***Create New Plan modal not displayed, it failed***")
#         #     assert False
#
#         # invoke method to enter plan name in PlanName filed in Create New Plan modal
#         self.Portfolio.planName_in_CreateNewPlan()
#
#         self.Portfolio.addskus_in_CreateNewPlan()
#
#         self.Portfolio.create_newPlan()
#
#         self.driver.close()
#
