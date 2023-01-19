import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="class")
def setup_class(browser,request):
    if browser =='chrome':
         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser =='firefox':
         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
         driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
         return driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.delete_all_cookies()
    driver.close()
    
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

######### PYTEST HTML REPORTS ###############

# #It is hook for adding environment info to html reports
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'BGE'
#     config._metadata['Module Name'] = 'Client'
#     config._metadata['Tester']= 'sujith'

# #It is hook for delete/modify Environment info to HTML Report
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)



#pytest -s -v testCases/test_login.py --browser chrome --html=Reports/report.html