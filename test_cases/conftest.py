import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify which browser to use: ")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise ValueError("Browser must be either chrome or firefox")
    return driver


###########for pytest html reports ###########
#hook for adding environment info in html report
def pytest_configure(config):
   config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, Swag Labs'
   config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
   config.stash[metadata_key]['Tester Name'] = 'Pavan'


#hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop('Packages',None)
   metadata.pop('Plugins', None)
