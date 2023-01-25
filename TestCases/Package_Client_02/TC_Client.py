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
    
    def setup_class(self):
        self.faker= random_data()
        self.faker.data()
        with open('/home/sujith/codebase/BGE_Framework_Design/utilities/client.json') as json_file:
            self.data = json.load(json_file)
    @pytest.mark.order(1)
    def test_client_01(self):
        self.driver.get(self.url)
        self.lp = login_Module(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()
    @pytest.mark.order(2)    
    def test_add_client_02(self):
        self.client = Client(self.driver)
        self.client.navigate_to_client_page()
    #     self.client.add_Client()
    #     self.client.client_mandatory_field()
    #     time.sleep(3)
    #     self.client.name(self.data["name"])
    #     self.client.phone_number(self.data["phone_number_countryCode"],self.data["phone_number"])
    #     self.client.address(self.data["address"])
    #     self.client.mobile_number(self.data["mobile_number_countryCode"],self.data["mobile_number"])
    #     self.client.email_address(self.data["email"])
    #     self.client.city(self.data["city"])        # self.client.email_address(data["email"])
    #     self.client.city(self.data["city"])
    #     self.client.postal_code(self.data["postalCode"])   
    #     self.client.website("www.google.com")
    #     self.client.task_visibility(['Open' , 'Completed'])
    #     self.client.plant(['airpods plant','Coffee plant'])
       
    #     # #AddPlant
    #     self.client.client_add_plant()
    #     self.client.plantCreation_mandatory_fields()
    #     #self.plant_name = "Plant_01"
    #     self.client.plant_name(self.data["plant_name"])
    #     self.client.size(self.data["size"])
    #     self.client.acronym(self.data["acronym"])
    #     self.client.on_boardingDate()
        
    #     self.client.status("Active")
    #     self.client.add_plant(self.data["plant_name"])
      
    #     self.client.client_addUser()
    #     # self.client.userCreation_mandatory_fields()
    #     # print(self.data["user_first_name"])
    #     self.client.user_firstName(self.data["user_first_name"])
    #     self.client.user_lastName(self.data["user_last_name"])
    #     self.client.user_email(self.data["user_email"])
    #     self.client.user_password(self.data["user_password"])
    #     self.client.addUser(self.data["user_first_name"])
    #     self.client.createClient()
    # @pytest.mark.order(3) 
    # def test_username_in_listview(self):
    #     for x in self.driver.find_elements(By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]'):
    #             if x.text in self.data["name"]:
    #                 assert True
    #                 break
    #             else:
    #                 assert False
    # @pytest.mark.order(4)
    # def test_search_option(self):
    #     self.client = Client(self.driver)
    #     self.client.search_client(self.data["name"])
    #     time.sleep(3)
    #     element = self.driver.find_elements(By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]')
    #     for x in element:
    #         if x.text in self.data["name"]:
    #             assert True
    #         else:
    #             assert False
    # @pytest.mark.order(5)
    def test_client_view(self):
        self.client = Client(self.driver)
        # self.client.client_view(self.data["name"])
        # time.sleep(2)
        self.client.client_view("TESARK")
    def test_edit_client(self):
        self.client = Client(self.driver)
        self.client.view_edit_client_page()
        self.client.mandatory_field()
        self.client.edit_client("TESARK")

    

    # @pytest.mark.order(5)
    # def test_menuOption_in_listView(self):
    #     self.client = Client(self.driver)
    #     self.client.edit_client_dropdown(self.data["name"])
               
   
if __name__ =="__main__":
    unittest.main()
