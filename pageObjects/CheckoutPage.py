from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH,"//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    productAddBtn = (By.XPATH, "div/button")
    checkoutItems = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkoutSuccess = (By.XPATH,"//button[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductName(self, product):
        return product.find_element(*CheckoutPage.productName)

    def getProductAddBtn(self, product):
        return product.find_element(*CheckoutPage.productAddBtn)

    def getcheckoutItemsBtn(self):
        return self.driver.find_element(*CheckoutPage.checkoutItems)

    def getcheckoutSuccessBtn(self):
        self.driver.find_element(*CheckoutPage.checkoutSuccess).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
