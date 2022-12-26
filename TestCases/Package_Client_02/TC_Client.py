
import time
import pytest
import unittest
from pageObjects.client_Module import Client
from pageObjects.login_Module import login_Module
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_class")
class Test_client(unittest.TestCase):
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    def test_client_01(self):
        self.lp = login_Module(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()


    def test_zdd_client_02(self):
        self.client = Client(self.driver)
        self.client.navigate_to_client_page()
        # time.sleep(4)
        self.client.add_Client()
        # self.client.name()
        # # time.sleep(5)
        # self.client.phone_number()
        # time.sleep(4)
        # self.client.email()
        # self.client.mobile_number()
        # self.client.email_address()
        # self.client.city()
        # self.client.postal_code()
        # self.client.website()
        #self.client.task_visibility(['Open' , 'Completed'])
        #time.sleep(3)
        #self.client.plant(['Watch Plant','plant_test'])
        #time.sleep(3)
        #AddPlant
        self.client.client_add_plant()
        self.client.plantCreation_mandatory_fields()
        self.client.plant_name()
        self.client.size()
        self.client.acronym()
        self.client.on_boardingDate()
        #time.sleep(3)
        self.client.status()
        self.client.add_plant()
        time.sleep(3)
        

if __name__ =="__main__":
    unittest.main()
