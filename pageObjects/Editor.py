import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from utilities.readProperties import ReadConfig
from base.base_driver import BaseDriver
class canvas_Editor(BaseDriver):
    # Create New Plan web elements
    plan_name_xpath = "//div[@class='CreateNewPlanModal-module__control__uPVER']//input[@id='planName']"
    add_skus = "//textarea[@id='skuList']"
    create_button_xpath = "//div[@class='CreateNewPlanModal-module__actionBar__CHORC']//button[normalize-space()='Create']"
    # Import skus summary modal OK button
    OK_button = "//div[@class='ImportListOfSkuSummaryModal-module__modalContent__L_BTM']/descendant::button[text()='OK']"
    # canvas locator
    destination_element = "//canvas[@id='owViewport']"
    # search bar, search icon , search results and first search item locators
    search_bar = "//input[@class='ProductSearch-module__input__acJLP']"
    search_results = "//div[@class='ProductList-module__root__v_tWO']"
    search_button_svg_xpath = "//*[local-name()='svg'][contains(@viewBox,'5 0 25 25')]"
    source_element = "//div[@class = 'ProductList-module__root__v_tWO']/div/div[1]"
    #source_element = "(//img[@role='img'])[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Create an empty plan
    def create_empty_plan(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.plan_name_xpath))).send_keys("plan2")
        add_skus = self.driver.find_element(By.XPATH, self.add_skus)
        add_skus.send_keys(ReadConfig.add_skus())
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    # import sku summary modal in editor OK button
    def OK_ImportSkuSummryModal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.OK_button))).click()

    # check imported skus show up in the canvas
    def Item_InCanvas(self):
        wait = WebDriverWait(self.driver, 10)
        Products = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.destination_element)))
        for product in Products:
            print(product.text)


    # search for Chair in Furnish panel
    def search_bar_productlist(self):
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))
        search.send_keys("chair")
        search_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.search_button_svg_xpath)))
        search_button.click()

    # wait until all search products load in furnish panel
    def search_results_productlist(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, self.search_results)))

    # select first search item to open pip page
    def select_firstItem_inSearchResults(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.source_element))).click()

    def move_item_tocanvas(self):
        wait = WebDriverWait(self.driver, 10)

        # Double-click on the image to move it to the canvas
        image_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.source_element)))
        actions = ActionChains(self.driver)
        actions.double_click(image_element).perform()
        time.sleep(5)
        print("Image moved to canvas")

        # Wait for the canvas to be visible after the image is moved
        canvas_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.destination_element)))
        print("Canvas is visible")


