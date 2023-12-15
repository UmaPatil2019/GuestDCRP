from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from testCases import conftest

class loginPage():
    #locators for Continue as Guest button in login page and what's new in RP modal
    #button_ContinueAsGuest_xpath = "//form[@class='login-form guest visible']//button[@class='login-item guest-button']"
    new_modal_xpath = "//div[@class='WhatsNewModal-module__container__Vnn6u']//p[starts-with(text(),'What')]"


    def __init__(self, driver):
        self.driver = driver



    #method to click on continue as Guest button in login page
    # def clickContinue(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located((By.XPATH, self.button_ContinueAsGuest_xpath))).click()


    #method to verify that What's new RP modal is displayed by checking the modal header text
    # def getConfirmationmsg(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 10)
    #         element = wait.until(EC.presence_of_element_located((By.XPATH, self.new_modal_xpath)))
    #         return element.text
    #
    #     except:
    #         None




