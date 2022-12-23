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
        