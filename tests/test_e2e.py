from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()

        homepage = HomePage(self.driver)
        checkoutPage = homepage.getShopBtn()

        log.info("Getting all the product cards!")
        products = checkoutPage.getProducts()

        for product in products :
            productName = checkoutPage.getProductName(product).text
            log.info(productName)

            if productName == "Blackberry":
                checkoutPage.getProductAddBtn(product).click()
        checkoutPage.getcheckoutItemsBtn().click()

        log.info("Clicking on checkout button!")
        confirmPage = checkoutPage.getcheckoutSuccessBtn()

        log.info("Entering the country name as 'ind'!")
        confirmPage.getCountryInputBox().send_keys("ind")

        self.verifyLinkPresence("India")
        confirmPage.getCountryText().click()
        confirmPage.getTnCCheckBox().click()
        confirmPage.getPurchaseBtn().click()
        successText = confirmPage.getSuccessText().text[2:]
        log.info("Text recieved from application is " + successText)

        assert "Success! Thank you!" in successText, log.error("Text didn't Match!")
