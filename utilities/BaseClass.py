import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("../logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        if logger.hasHandlers():     #* for stopping the repeating logs
            logger.handlers.clear()
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT,text)
            )
        )

    def selectDropdownByValue(self, dropdown, text):
        Select(dropdown).select_by_visible_text(text)