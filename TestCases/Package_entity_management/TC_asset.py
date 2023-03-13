import time
from page_objects.entity_Management.asset import asset
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure





@pytest.mark.usefixtures("init_driver")
class Test_Asset(unittest.TestCase):
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
    @allure.description("Should navigate to asset page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2)
    def test_navigate_asset(self):
        self.asset = asset(self.driver)
        self.asset.navigate_asset()
    @allure.description("Should display the asset popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(3)
    def test_add_asset(self):
        self.asset = asset(self.driver)
        self.asset.add_asset()
    @allure.description("Should display the validation message on the mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(4)
    def test_mandatory_fields(self):
       self.asset = asset(self.driver)
       self.asset.asset_mandatory_fields()

    @allure.description("Should create the asset")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(5)
    def test_create_asset(self):
       self.asset = asset(self.driver)
       self.asset.modal("Model_10")
       self.asset.rating("9.0")
       self.asset.factory_barcode("OXPWR")
       self.asset.category("Asset Category 512")
       self.asset.Manufacturer("Test_Manufacturer_01")
       self.asset.create_asset()
    
    @allure.description("Should display created asset in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(6)
    def test_created_asset_in_listView(self):
        self.asset = asset(self.driver)
        self.asset.asset_in_listView("Model_10")  
    @allure.description("Should view the created asset")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7)
    def test_view_asset(self):
        self.asset = asset(self.driver)  
        self.asset.view_asset("Model_10")    
    @allure.description("Should display the Edit asset popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(8)
    def test_edit_button_in_view_asset(self):
        self.asset = asset(self.driver)
        self.asset.edit_asset_button()
    @allure.description("Should display validation message on mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9)
    def test_edit_mandatory_fields(self):
        self.asset = asset(self.driver)
        self.asset.edit_asset_mandatory_field()
    @allure.description("Should able to edit and save the asset ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(10)
    def test_edit_asset(self):
        self.asset = asset(self.driver)
        self.asset.modal("Model_15")
        self.asset.save_information() 
    @allure.description("Should able to edit and save the asset category in asset category list view option ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11)
    def test_listView_edit_asset(self):
        self.asset = asset(self.driver)
        self.asset.list_view_edit_option("Model_15")
        self.asset.weblink("www.gmail.com")
        self.asset.description("This created for testing purpose")
        self.asset.save_information()
    @allure.description("Should able to edit and save the asset category in asset category list view option ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(12)
    def test_search_option(self):
        self.asset = asset(self.driver)
        self.asset.search_functionality("Model_15")