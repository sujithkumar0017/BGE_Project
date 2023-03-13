import time
from page_objects.entity_Management.asset_category import asset_category
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure





@pytest.mark.usefixtures("init_driver")
class Test_Asset_Category(unittest.TestCase):
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
    @allure.description("Should navigate to asset category page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2)
    def test_navigate_asset_category_page(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.navigate_assetCategory()
    
    @allure.description("Should display the asset category popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(3)
    def test_add_asset_category(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.add_assetCategory()
    @allure.description("Should display the validation message")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(4)
    def test_mandatory_fields(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.assetCategory_mandatory_fields()
    @allure.description("Should able to create asset category")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(5)
    def test_create_asset_category(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.Category("Asset Category 6")
        self.asset_category.create_category()
    @allure.description("Should display the created asset category in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(6)
    def test_created_asset_category_in_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.category_in_listView("Asset Category 6")  
    @allure.description("Should view the created asset category")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7)
    def test_view_asset_category(self):
        self.asset_category = asset_category(self.driver)   
        self.asset_category.view_category("Asset Category 6")    
    @allure.description("Should display the edit asset category popup window ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(8)
    def test_edit_button_in_view_asset_category(self):
        self.asset_category = asset_category(self.driver) 
        self.asset_category.edit_category_button()
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9)
    def test_edit_mandatory_fields(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.edit_category_mandatory_field() 
    
    @allure.description("Should able to edit and save the asset category and navigate to asset category page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(10)
    def test_edit_asset_category(self):
        self.asset_category = asset_category(self.driver) 
        self.asset_category.edit_category("Asset Category 61")  
        self.asset_category.save_information_button()
    @allure.description("Should able to edit and save the asset category in asset category list view option")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11)
    def test_edit_option_in_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.list_view_edit_option("Asset Category 61")
        self.asset_category.edit_category_mandatory_field()
        self.asset_category.edit_category("Asset Category 512")  
        self.asset_category.save_information_button()
    @allure.description("Should able to search asset using search functionality")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(12)
    def test_search_option_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.search_functionality("Asset Category 512")
        