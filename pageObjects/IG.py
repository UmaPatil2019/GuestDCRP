import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from utilities.readProperties import ReadConfig
from base.base_driver import BaseDriver

class InspirationGallery(BaseDriver):

        view_room_details_modal_xpath = "//button[normalize-space()='View Room Details']"
        funrish_RP_modal_xpath = "//button[contains(normalize-space(),'Furnish Room Planner')]"
        furnish_RP_modal_button_xpath = "//button[contains(normalize-space(),'Furnish Room Planner')]"
        brand_filter_icon_xpath = "//span[@data-testid='ig-filter-brand-option']//span[@class='Filter-module__FilterExpandIcon__HJtMw']//*[name()='svg']"
        filter_by_brands_options_xpath = "//div[@class='Filter-module__FilterContainer__QnbET']//div[@class='Filter-module__FilterOptionList__wzras Filter-module__FilterOptionListExpanded__EcmJF']/div/span"
        #PB_xpath = "//span[normalize-space()='Pottery Barn']"

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        def brand_filterBy(self):
            self.wait_presence_of_element_located(By.XPATH, self.brand_filter_icon_xpath).click()
            time.sleep(5)

        def select_brand_PB(self):
            filter_by_options = self.wait_visiblility_of_all_elements_located(By.XPATH, self.filter_by_brands_options_xpath)
            for i in filter_by_options:
                print(f"Checking option: {i.text}")
                if i.text == "Pottery Barn":
                    print("Clicked on Pottery Barn")
                    i.click()
                    break

            else:
                print("Pottery Barn option not found")

        def check_each_brand(self):
            filter_by_options = self.wait_visiblility_of_all_elements_located(By.XPATH, self.filter_by_brands_options_xpath)
            for i in filter_by_options:
                if i.text == "All":
                    print(i.is_enabled())

                else:
                    print(i.text)
                    i.click()
                    print(i.is_enabled())
                    time.sleep(5)
                    i.click()
                    print(i.text)
                    self.wait_presence_of_element_located(By.XPATH, self.brand_filter_icon_xpath).click()
                    continue





























