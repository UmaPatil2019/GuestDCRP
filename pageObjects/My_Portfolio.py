import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class myPortfolio():
    #locators for edit-> NewPlan -> New Plan modal header msg in Portfolio
    edit_xpath = "//span[normalize-space()='Edit']"
    newPlan_xpath = "(//li[@class='style-module__subMenuColItem__sqFMG'])[1]"
    new_Plan_Modal_header_msg = "//h2[normalize-space()='Create New Plan']"
    #locator for Plan Name under Create New Plan modal
    new_PlanModal_PlanName = "//form[@class='CreateNewPlanModal-module__form__GOT3N']/descendant::input"
    add_skus = "//form[@class='CreateNewPlanModal-module__form__GOT3N']/descendant::textarea"
    create_button = "//form[@class='CreateNewPlanModal-module__form__GOT3N']/descendant::button[text()='Create']"


    def __init__(self, driver):
        self.driver = driver

    #method to find Edit menu by mouse hovering action and then find NewPlan option and open NewPlan modal by clicking on it
    def clickonNewPlan(self):
        wait = WebDriverWait(self.driver, 5)
        Action = ActionChains(self.driver)
        #edit object to find the edit menu
        edit = wait.until(EC.visibility_of_element_located((By.XPATH, self.edit_xpath)))
        #Hover over edit menu
        Action.move_to_element(edit).move_to_element_with_offset(edit,0,50).perform()
        #wait for NewPlan option to become visible after the mouse hover
        newPlan = wait.until(EC.element_to_be_clickable((By.XPATH, self.newPlan_xpath)))
        time.sleep(5)
        #click on NewPlan option
        newPlan.click()

    #method to confirm if NewPlan modal is displayed
    def newPlanModalMsg(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            #locator to find the New Plan modal header text
            header = wait.until(EC.presence_of_element_located((By.XPATH, self.new_PlanModal_PlanName)))
            return header.text

        except:
            None

    #method to enter plan name in the Plan name field
    def planName_in_CreateNewPlan(self):
        Plan_name = self.driver.find_element(By.XPATH, self.new_PlanModal_PlanName)
        return Plan_name.send_keys("Plan1")

    def addskus_in_CreateNewPlan(self):
        Add_skus_inNewPlan = self.driver.find_element(By.XPATH, self.add_skus)
        return Add_skus_inNewPlan.send_keys("3531930,404040")

    def create_newPlan(self):
        self.driver.find_element(By.XPATH, self.create_button).click()














