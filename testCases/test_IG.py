import time

import pytest
from pageObjects.IG import InspirationGallery
from pageObjects.Get_StartedPage import getstartedPage
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class Test_InspirationGallery():
    logger = LogGen.loggen()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.regression
    def test_IG(self):

        get_startedpage_obj2 = getstartedPage(self.driver)
        get_startedpage_obj2.clickIG()

        self.IG = InspirationGallery(self.driver)
        self.IG.brand_filterBy()
        #IG.select_brand_PB()
        self.IG.check_each_brand()
