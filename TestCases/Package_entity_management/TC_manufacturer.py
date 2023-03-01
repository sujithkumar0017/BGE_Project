import time
from pageObjects.enityManagement.manufacturer import manufacturer
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest
import allure





@pytest.mark.usefixtures("setup_class")
class Test_Manufacturer(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    @pytest.mark.order(1)
    def test_login(self):   
        self.driver.get(self.url)
        self.lp = login_Module(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()
    @allure.description("Should navigate to failure reason page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2)
    def test_navigate_manufacturer(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.navigate_manufacturer()

    @allure.description("Should display the manufacturer popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(3)
    def test_add_manufacturer(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.add_manufacturer()

    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(4)
    def test_create_manufacturer_mandatory_fields(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.manufacturer_mandatory_field()
    
    
    @allure.description("Should able to create Manufacturer")
    @allure.severity(severity_level="CRITICAL")     
    @pytest.mark.order(5)
    def test_create_manufacturer(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.corporate_brand_name("Test_Manufacturer_01")
        self.manufacturer.address("New York")
        self.manufacturer.phone_number("+91","9939442000")
        self.manufacturer.email("manufacturer_01@yopmail.com")
        self.manufacturer.create_manufacturer()

    @allure.description("Should display the created manufacturer in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(6)
    def test_created_manufacturer_in_listView(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.manufacturer_in_listView("Test_Manufacturer_01") 

    @allure.description("Should view the created manufacturer")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7)
    def test_view_manufacturer(self):
        self.manufacturer = manufacturer(self.driver) 
        self.manufacturer.view_manufacturer("Test_Manufacturer_01")    
    
    @allure.description("Should display the edit Manufacturer popup window ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(8)
    def test_edit_button_in_view_manufacturer(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.edit_manufacturer_button()
    
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9)
    def test_edit_mandatory_fields(self):
        self.manufacturer = manufacturer(self.driver)
        self.manufacturer.edit_manufacturer_mandatory_field() 

    @allure.description("Should able to edit and save the manufacturer and navigate to Manufacturer page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(10)
    def test_edit_manufacturer(self):
        self.manufacturer= manufacturer(self.driver)
        self.manufacturer.email("manufacturer_040@yopmail.com")
        self.manufacturer.phone_number("+91","99394420205")
        self.manufacturer.edit_manufacturer()   

    @allure.description("Should able to edit and save the manufacturer in category list view option")
    @allure.severity(severity_level="CRITICAL")    
    @pytest.mark.order(11)
    def test_listView_edit_manufacturer(self):
        self.manufacturer= manufacturer(self.driver)
        self.manufacturer.list_view_edit_option("Test_Manufacturer_01")
        self.manufacturer.website("www.gmail.com")
        self.manufacturer.edit_manufacturer()
    @allure.description("Should able to search Corporation Brand Name using search functionality")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(12)
    def test_search_option(self):
        self.manufacturer= manufacturer(self.driver)
        self.manufacturer.search_functionality("Test_Manufacturer_01")