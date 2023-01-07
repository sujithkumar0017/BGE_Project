import time
import pytest
import unittest
from pageObjects.client_Module import Client
from pageObjects.login_Module import login_Module
from utilities.dd_using_json import random_data
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
# from ddt import ddt, data, file_data, unpack
import json

@pytest.mark.usefixtures("setup_class")
class Test_client(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_client_01(self):
        self.driver.get(self.url)
        self.lp = login_Module(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()
    def test_zdd_client_02(self):
        self.client = Client(self.driver)
        self.faker= random_data()
        self.faker.data()
        with open('/home/sujith/codebase/BGE_Framework_Design/utilities/client.json') as json_file:
            data = json.load(json_file)
        self.client.navigate_to_client_page()
        # self.client.add_Client()
        # # time.sleep(4)
        # self.client.name(data["name"])
        # self.client.phone_number(data["phone_number_countryCode"],data["phone_number"])
        # #time.sleep(2)
        # self.client.address(data["address"])
        # #time.sleep(3)
        # self.client.mobile_number(data["mobile_number_countryCode"],data["mobile_number"])
        # self.client.email_address(data["email"])
        # self.client.city(data["city"])        # self.client.email_address(data["email"])
        # self.client.city(data["city"])
        # self.client.postal_code(data["postalCode"])   
        # self.client.website("www.google.com")
        # self.client.task_visibility(['Open' , 'Completed'])
        # #time.sleep(3)
        # self.client.plant(['Watch Plant','plant_test'])
        # #time.sleep(3)
        # #AddPlant
        # self.client.client_add_plant()
        # self.client.plantCreation_mandatory_fields()
        # #self.plant_name = "Plant_01"
        # self.client.plant_name(data["plant_name"])
        # self.client.size(data["size"])
        # self.client.acronym(data["acronym"])
        # self.client.on_boardingDate()
        # #time.sleep(3)
        # self.client.status("Active")
        # self.client.add_plant(data["plant_name"])
        # time.sleep(3)
        # self.client.client_addUser()
        # #self.client.userCreation_mandatory_fields()
        # self.client.user_firstName(data["user_first_name"])
        # self.client.user_lastName(data["user_last_name"])
        # self.client.user_email(data["user_email"])
        # self.client.user_password(data["user_password"])
        # self.client.addUser(data["user_first_name"])
        # self.client.createClient(data["name"])
        # time.sleep(3)
        # # print("initialized Data ",data["name"]) 
        # for x in self.driver.find_elements(By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]'):
        #     if x.text in data["name"]:
        #         assert True
        #         time.sleep(3)
        #         break
        #     else:
        #        assert False
        self.client.list_view("Lindsey Robinson")
        # self.client.delete_client("Lindsey Robinson")
        

if __name__ =="__main__":
    unittest.main()
