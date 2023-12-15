import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class canvas_Editor():
    #Import skus summary modal OK button
    OK_button = "//div[@class='ImportListOfSkuSummaryModal-module__modalContent__L_BTM']/descendant::button[text()='OK']"
    #canvas locator
    canvas = "//canvas[@id='owViewport']"
    furnish_panel_xpath = "//div[normalize-space()='FURNISH']"
    search_bar = "//input[@class='ProductSearch-module__input__acJLP']"
    search_results = "//div[@class='ProductList-module__root__v_tWO']"
    search_button_svg_xpath = "//*[local-name()='svg'][contains(@viewBox,'5 0 25 25')]"
    first_item_search_results_productlist = "//div[@class = 'ProductList-module__root__v_tWO']/div/div[1]"

    def __init__(self,driver):
        self.driver = driver

    #import sku summary modal in editor OK button
    def OK_ImportSkuSummryModal(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.OK_button))).click()


    #check imported skus show up in the canvas
    def Item_InCanvas(self):
        wait = WebDriverWait(self.driver, 10)
        Products = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.canvas)))
        for product in Products:
            print(product.text)

    #search for Chair in Furnish panel
    def search_bar_productlist(self):
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))
        search.send_keys("chair")
        search_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.search_button_svg_xpath)))
        search_button.click()

    #wait until all search products load in furnish panel
    def search_results_productlist(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, self.search_results)))

    #select first search item to open pip page
    def select_firstItem_inSearchResults(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.first_item_search_results_productlist))).click()













