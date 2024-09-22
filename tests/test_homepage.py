import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_form_submission(self, getData):
        log = self.get_logger()

        homepage = HomePage(self.driver)

        log.info(f"Entering name as '{getData['name']}'.")
        homepage.getName().send_keys(getData['name'])

        log.info(f"Entering email as '{getData['email']}'.")
        homepage.getEmail().send_keys(getData['email'])

        homepage.getCheckbox().click()
        dropdown = homepage.getGender()

        log.info(f"Selecting gender as '{getData['gender']}'.")
        self.selectDropdownByValue(dropdown, getData['gender'])

        homepage.getSubmitBtn().click()
        alertText = homepage.getAlertText().text[2:]
        log.info(f"Alert Text is {alertText}.")

        self.driver.refresh()
        assert "Success" in alertText, log.error("Text didn't match!")

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param