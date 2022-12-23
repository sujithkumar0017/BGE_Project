import time
from pageObjects.login_Module import login_Module
import pytest
from utilities.readProperties import ReadConfig
from utilities import XLUtilis
import unittest
@pytest.mark.usefixtures("setup_class")
class Test_002_DDT_login(unittest.TestCase):
    baseURL = ReadConfig.getApplicationUrl()
    path= "Test_Data/Login_DDT.xlsx"
    #baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def test_PageContents(self):
        self.lp = login_Module(self.driver)
        self.lp.Page_Contents() 
        self.lp.termsConditions_Link()
        time.sleep(3) 
        self.lp.privacyPolicy_Link()
        time.sleep(3)
        self.lp.help_Link()
    def test_login(self):
        self.lp = login_Module(self.driver)
        self.rows=XLUtilis.getRowCount(self.path,'Sheet1')
        lst_status=[]
        for r in range(2,self.rows+1):
                self.user=XLUtilis.readData(self.path,'Sheet1',r,1)
                self.password=XLUtilis.readData(self.path, 'Sheet1', r, 2)
                self.exp=XLUtilis.readData(self.path, 'Sheet1', r, 3)
                self.lp.email(self.user)
                self.lp.password(self.password)
                self.lp.login()
                time.sleep(3)

                act_title = self.driver.title
                exp_title="BGE Dashboard"
                if act_title==exp_title:
                      if self.exp=="Pass":
                          self.lp.signOut()
                          lst_status.append("Pass")
                      elif self.exp=="Fail":
                          #self.logger.info("*****Failed*****")
                          self.lp.signOut()
                          lst_status.append("Fail")
                elif act_title!=exp_title:
                      if self.exp=='Pass':
                         #self.logger.info("*****Failed*****")
                         lst_status.append("Fail")
                      elif self.exp=='Fail':
                          #self.logger.info("******Passed*****")
                          lst_status.append("Pass")
                if "Fail" not in lst_status:
                  #self.logger.info("*******Login DDT test Passed********")
                  #self.driver.close()
                  assert True
                else:
                  #self.logger.info("*******Login DDT test failed********")
                  #self.driver.close()s
                  assert False

if __name__ =="__main__":
    unittest.main()
