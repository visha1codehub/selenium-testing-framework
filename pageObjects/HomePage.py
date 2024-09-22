from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopBtn = (By.CSS_SELECTOR," a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    alertText = (By.CLASS_NAME, "alert-success")

    def getShopBtn(self):
        self.driver.find_element(*HomePage.shopBtn).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alertText)
