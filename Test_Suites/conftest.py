import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService

from TestCases.Package_Client_02.test_client import Test_client 
from TestCases.Package_maintenance.test_corrective_maintenance import Test_Corrective


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


# def pytest_collection_modifyitems(items):
#     test_classes = {}
#     for item in items:
#         print(items)


#         if item.cls:
#             class_name = item.cls.__name__
#             if class_name not in test_classes:
#                 test_classes[class_name] = []
#             test_classes[class_name].append(item)
#     items.clear()
#     for class_name, class_items in sorted(test_classes.items()):
#         class_items.sort(key=lambda item: (item.get_closest_marker('order') or 0, item.name))
#         items.extend(class_items)\

# def pytest_collection_modifyitems(items):
#     test_classes = {}
#     for item in items:
#         if item.cls:
#             class_name = item.cls.__name__
#             if class_name not in test_classes:
#                 test_classes[class_name] = []
#             test_classes[class_name].append(item)
#     items.clear()
#     for class_name, class_items in sorted(test_classes.items()):
#         class_items.sort(key=lambda item: item.name)
#         items.extend(class_items)
# def pytest_collection_modifyitems(items):
#     test_class1 = []
#     test_class2 = []
#     for item in items:
#         if item.cls and item.cls.__name__ == 'Test_client':
#             print("summa")
#             test_class1.append(item)
#         elif item.cls and item.cls.__name__ == 'Test_Corrective':
#             test_class2.append(item)
#     items.clear()
#     items.extend(test_class1)
#     items.extend(test_class2)

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