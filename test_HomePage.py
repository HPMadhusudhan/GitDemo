import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log=self.getLogger()
        homepage=HomePage(self.driver)
        log.info("First name is: "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("email120")
        homepage.getCheckbox().click()

        # find element using Xpath
        # Gen Syntax-> //tagname[@attribute='value']

        # find element using CSS Selector
        # Gen Syntax--> tagname[attribute='value'] --> just remove // and @ from Xpath
        # or shortcut #IDvalue--> using ID; .classvalue--> using class

        # How to select static dropdown "Gender"
        self.selectOptionByText(homepage.getGender(),getData["gender"])

        homepage.getEmploymentStatus().click()



        homepage.getSubmitButton().click()



        # To capture success message and print
        message = homepage.getSuccessMessage().text


        # To add assertion whether "Success" is present in the message displayed in webpage after submit
        assert "Success" in message

    # calling getTestData method without creating object
    # since it is declared as static method
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param


