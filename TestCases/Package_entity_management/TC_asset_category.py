import time
from pageObjects.enityManagement.asset_category import asset_category
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest





@pytest.mark.usefixtures("setup_class")
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
    @pytest.mark.order(2)
    def test_navigate_entity_management(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.navigate_assetCategory()
   
    @pytest.mark.order(3)
    def test_add_asset_category(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.add_assetCategory()
    
    @pytest.mark.order(4)
    def test_mandatory_fields(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.assetCategory_mandatory_fields()
    
    @pytest.mark.order(5)
    def test_create_asset_category(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.Category("Asset Category 5")
        self.asset_category.create_category()

    @pytest.mark.order(6)
    def test_created_asset_category_in_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.category_in_listView("Asset Category 5")  

    @pytest.mark.order(7)
    def test_view_asset_category(self):
        self.asset_category = asset_category(self.driver)   
        self.asset_category.view_category("Asset Category 5")    

    @pytest.mark.order(8)
    def test_edit_button_in_view_asset_category(self):
        self.asset_category = asset_category(self.driver) 
        self.asset_category.edit_category_button()
    
    @pytest.mark.order(9)
    def test_edit_mandatory_fields(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.edit_category_mandatory_field() 

    @pytest.mark.order(10)
    def test_edit_asset_category(self):
        self.asset_category = asset_category(self.driver) 
        self.asset_category.edit_category("Asset Category 51")  
        self.asset_category.save_information_button()

    @pytest.mark.order(11)
    def test_edit_option_in_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.list_view_edit_option("Asset Category 51")
        self.asset_category.edit_category("Asset Category 512")  
        self.asset_category.save_information_button()
    
    @pytest.mark.order(12)
    def test_search_option_listView(self):
        self.asset_category = asset_category(self.driver)
        self.asset_category.search_functionality("Asset Category 512")
    