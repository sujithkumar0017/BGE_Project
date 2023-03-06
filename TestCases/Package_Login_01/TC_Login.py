# from utilities.readProperties import ReadConfig
# import time
# import pytest

# # To run - python3 -m pytest
# from pageObjects.login_Module import login_Module
# @pytest.mark.usefixtures("setup_class")
# class Test_Admin_Login():
#     #baseURL = ReadConfig.getApplicationUrl()
#     useremail = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#     def test_adminLogin(self):
#         #self.driver.get(self.baseURL)
#         self.lp = login_Module(self.driver)
#         self.lp.Page_Contents() 
#         self.lp.termsConditions_Link()
#         time.sleep(3) 
#         self.lp.privacyPolicy_Link()
#         time.sleep(3)
#         self.lp.help_Link()
        # time.sleep(3)
        # self.lp.email(self.useremail)
        # self.lp.password(self.password)
        # self.lp.login()
        # time.sleep(5)   
        # act_title = self.driver.title
        # print(act_title)
        # if act_title == "BGE Dashboard":
        #     assert True
        # else:
        #     print("failed")
        #     assert False
        # time.sleep(3)
        # self.lp.signOut()
        # time.sleep(5)
        # print("Logout Successfully")
        
#----------------------------------------------------------------------------------------------------#
import time
import unittest
from selenium import webdriver
from parameterized import parameterized

import pytest
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains

class basetest():
    def __init__(self,driver) -> None:
        self.driver = driver
        
@pytest.mark.usefixtures("setup_class")
class Test_login(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    @pytest.mark.order(1)
    def test_navigate_to_login_page(self):
        self.login = login_Module(self.driver)
        self.driver.get(self.url)
        self.login.navigate_to_login_page()
    @parameterized.expand([
        ("invalid_password","bge02@yopmail.com", "qwerty", "Email or Password is invalid"),
        ("invalid_username","user04@yopmail.com", "qwerty123", "Email or Password is invalid"),
        ("blank_password","bge02@yopmail.com","","Password is required"),
        ("blank_username","","qwerty123","Email is required"),
        ("blank_username_and_password","","","Email is required")])
    @pytest.mark.order(2)
    def test_using_invalid_credentials(self,name, username, password, expected):
           username_element  = self.driver.find_element(By.XPATH,'//input[@name="email"]')
           password_element = self.driver.find_element(By.XPATH,'//input[@name="password"]')
           login_button = self.driver.find_element(By.XPATH,'//button[contains(text(),"Login")]')
           actions = ActionChains(self.driver)
           actions.click(username_element).send_keys(username)
           actions.click(password_element).send_keys(password)
           actions.click(login_button).perform()
           time.sleep(2)
           self.assertTrue(expected in self.driver.page_source)
           username_element.clear()
           password_element.clear()
    @parameterized.expand([
        ("valid_credentials_1", "bge02@yopmail.com", "qwerty123", "Brighter App | Dashboard"),
    ])
    @pytest.mark.order(3)
    def test_using_valid_credentials(self, name, username, password, expected):
        self.driver.find_element(By.XPATH,'//input[@name="email"]').send_keys(username)
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH,'//button[contains(text(),"Login")]').click()
        if WebDriverWait(self.driver, 50).until(
            EC.title_contains(expected)
        ):
            assert True 
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Dashboard_Page",attachment_type=AttachmentType.PNG)
            assert False

    
        

   

if __name__ == "__main__":
    unittest.main()


