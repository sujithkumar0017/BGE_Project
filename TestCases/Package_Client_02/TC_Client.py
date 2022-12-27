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
        # # time.sleep(4)
        self.client.add_Client()
        self.client_name = "Test_client_009"
        self.client.name(self.client_name)
        # time.sleep(5)
        # self.client.phone_number()
        # time.sleep(2)
        # self.client.email()
        # self.client.mobile_number()
        # self.client.email_address()
        # self.client.city()
        # self.client.postal_code()
        # self.client.website()
        # self.client.task_visibility(['Open' , 'Completed'])
        # # time.sleep(3)
        # self.client.plant(['Watch Plant','plant_test'])
        # time.sleep(3)
        # #AddPlant
        # self.client.client_add_plant()
        # self.client.plantCreation_mandatory_fields()
        # self.plant_name = "Plant_01"
        # self.client.plant_name(self.plant_name)
        # self.client.size("12")
        # self.client.acronym("APEX123")
        # self.client.on_boardingDate()
        # #time.sleep(3)
        # self.client.status("Active")
        # self.client.add_plant(self.plant_name)
        # time.sleep(3)
        # self.client.client_addUser()
        # self.client.userCreation_mandatory_fields()
        # self.user_name = "Admin"
        # self.client.user_firstName(self.user_name)
        # self.client.user_lastName("test")
        # self.client.user_email("Bge@yopmail.com")
        # self.client.user_password("qwerty123")
        # self.client.addUser(self.user_name)
        self.client.createClient(self.client_name)
        

if __name__ =="__main__":
    unittest.main()
