import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options) #Local driver
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver # assigning local driver to class driver via request instance
    yield
    driver.close()

# Passing command line options to select browser at run time
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup1(request):
    browser_name=request.config.getoption("browser_name") #Extra line
    if browser_name=="chrome": #To select chrome browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)  # Local driver
    elif browser_name=="firefox": #To select firefox browser
        driver=webdriver.Firefox()

    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver # assigning local driver to class driver via request instance
    yield
    driver.close()
