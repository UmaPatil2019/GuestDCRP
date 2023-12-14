from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class landingPage():

    #locators for what's new in TP modal -> Continue to RP button in that modal
    new_modal_xpath = "//div[@class='WhatsNewModal-module__container__Vnn6u']//p[starts-with(text(),'What')]"
    continue_toRP_button_xpath = "//button[text()='Continue to room planner']"

    #constructor
    def __init__(self, driver):
        self.driver = driver

    # method to verify what's new in RP modal displayed by checking the modal text
    def getConfirmationmsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, self.new_modal_xpath)))
            return element.text

        except TimeoutError:
            print("TimeoutException: The 'What's New in Room Planner' modal did not appear within the expected time.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return None


    #method to Continue to RP by clicking that button
    def continueTORP(self):
        wait = WebDriverWait(self.driver, 10)
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,self.continue_toRP_button_xpath)))
        continue_button.click()









