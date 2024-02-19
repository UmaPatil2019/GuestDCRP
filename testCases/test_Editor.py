import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login import loginPage
from pageObjects.Whats_NewModal import landingPage
from pageObjects.Get_StartedPage import getstartedPage
from pageObjects.My_Portfolio import myPortfolio
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects import Get_StartedPage
from pageObjects.Editor import canvas_Editor



class Test_Editor:
    # create a logger object for LogGen class.loggen method
    logger = LogGen.loggen()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.regression
    def test_editor(self):
        self.logger.info("**** select empty plan from Get started page ****")
        self.get_startedPage_obj1 = getstartedPage(self.driver)
        self.get_startedPage_obj1.clickEmptyPlan()

        self.editor_obj2 = canvas_Editor(self.driver)
        self.editor_obj2.create_empty_plan()
        time.sleep(6)
        self.editor_obj2.OK_ImportSkuSummryModal()
        self.editor_obj2.search_bar_productlist()
        time.sleep(5)
        self.editor_obj2.search_results_productlist()
        time.sleep(5)
        self.editor_obj2.select_firstItem_inSearchResults()
        time.sleep(5)
        self.editor_obj2.move_item_tocanvas()
        time.sleep(5)














