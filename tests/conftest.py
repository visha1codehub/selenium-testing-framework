import pytest
from selenium import webdriver


def pytest_addoption(parser):      #^ This is for command line argument for which browser we want to invoke..
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

URL = "https://rahulshettyacademy.com/angularpractice/"

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        driver = webdriver.Edge()

    driver.get(URL)
    request.cls.driver = driver

    yield
    driver.quit()