from utilities.readProperties import ReadConfig
import time
import pytest

# To run - python3 -m pytest
from pageObjects.login_Module import login_Module
@pytest.mark.usefixtures("setup_class")
class Test_Admin_Login():
    #baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def test_adminLogin(self):
        #self.driver.get(self.baseURL)
        self.lp = login_Module(self.driver)
        self.lp.Page_Contents() 
        self.lp.termsConditions_Link()
        time.sleep(3) 
        self.lp.privacyPolicy_Link()
        time.sleep(3)
        self.lp.help_Link()
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
import json
import unittest
from selenium import webdriver
from parameterized import parameterized

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")

   
    @parameterized.expand([
        ("invalid_password","bge02@yopmail.com", "qwerty", "Email or Password is invalid"),
        ("invalid_username","user04@yopmail.com", "qwerty123", "Email or Password is invalid"),
        ("blank_password","bge02@yopmail.com","","Password is required")
        ("blank_username","","qwerty123","Email is required")
        ("blank_username_and_password","","","Email is required")
    ])
    def test_invalid_login(self, name, username, password, expected):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()
        self.assertTrue(expected in self.driver.page_source)
    @parameterized.expand([
        ("valid_credentials_1", "bge02@yopmail.com", "qwerty123", "Welcome"),
    ])
    def test_valid_login(self, name, username, password, expected):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()
        self.assertTrue(expected in self.driver.page_source)

   
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
