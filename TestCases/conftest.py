# import pytest 
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService


# @pytest.fixture(scope="class")
# def setup_class(request):
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(10)
#     driver.get("https://bge.tkea.in/auth-login")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield driver
#     driver.close()
