from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryInputBox = (By.ID,"country")
    countryText = (By.LINK_TEXT,"India")
    checkboxTnC = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.CSS_SELECTOR,"[type='submit']")
    successText = (By.CLASS_NAME,"alert-success")

    def getCountryInputBox(self):
        return self.driver.find_element(*ConfirmPage.countryInputBox)

    def getCountryText(self):
        return self.driver.find_element(*ConfirmPage.countryText)

    def getTnCCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkboxTnC)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)