# To scroll through list of phones, search for Blackberry
# Add to cart if its Blackberry

from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):


    def test_e2e(self):
        log=self.getLogger()
        homepage=HomePage(self.driver)
        shoppage=homepage.shopItems() # catching next page object here
        log.info("Getting all phones")
        self.driver.execute_script("window.scrollBy(0,500);")


        # To get phone products on a list
        phones=shoppage.getphones()

        for phone in phones:
            phonename=phone.find_element(By.XPATH, ShopPage.phonename).text
            log.info(phonename)
            if phonename == "Blackberry":
                phone.find_element(By.XPATH, "div/button[text()='Add ']").click()
                break

        self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element(By.XPATH, "//li/a[@class='nav-link btn btn-primary']").click()
        checkoutpage=shoppage.checkoutbutton() # catching next page object here

        confirmpage=checkoutpage.confirmbutton()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering Country Name ind")
        confirmpage.textbox().send_keys("ind")
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        #calling explicit wait method which is stored in Base class.
        #No need of creating an object for this class since this class
        # will be inherited by all test cases under class Testone
        self.verifylinkpresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Capture success message
        successmessage = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Success message received: " +successmessage)

        assert "Success! Thank you!" in successmessage