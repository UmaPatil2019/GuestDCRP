import os.path
import time

import pytest

from pageObjects.Login import loginPage
from pageObjects.Whats_NewModal import landingPage
from pageObjects.Get_StartedPage import getstartedPage
from pageObjects.My_Portfolio import myPortfolio
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Editor:
    # create a logger object for LogGen class.loggen method
    logger = LogGen.loggen()

    @pytest.mark.usefixtures("setup")
    def test_editor(self, setup):
        self.logger.info("**** Navigate to My Editor ****")


