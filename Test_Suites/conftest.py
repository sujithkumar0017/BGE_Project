import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService



@pytest.fixture(scope="session")
def init_driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    session = request.node
    for item in session.items:

        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield driver
    driver.delete_all_cookies()
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

