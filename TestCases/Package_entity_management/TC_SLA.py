import time
from pageObjects.enityManagement.SLA import sla
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest





@pytest.mark.usefixtures("setup_class")
class Test_SLA(unittest.TestCase):
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
    def test_navigate_sla(self):
        self.sla =sla(self.driver)
        self.sla.navigate_sla() 
    
    @pytest.mark.order(3)
    def test_function_of_add(self):
        self.sla = sla(self.driver)
        self.sla.add_sla()

    @pytest.mark.order(4)
    def test_mandatory_field(self):
        self.sla = sla(self.driver)
        self.sla.sla_mandatory_field()
    
    @pytest.mark.order(5)
    def test_create_sla(self):
        self.sla = sla(self.driver)
        self.sla.level("mobile sla")
        self.sla.description("This is created for testing purpose")
        self.sla.create_sla()
    
    @pytest.mark.order(6)
    def test_created_sla_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.level_in_listView("mobile sla")

    @pytest.mark.order(7)
    def test_view_sla(self):
        self.sla = sla(self.driver)
        self.sla.view_level("mobile slaa")
   
    @pytest.mark.order(8)
    def test_edit_option_in_view(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_button()
    
    @pytest.mark.order(9)
    def test_edit_sla_mandatory_field(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_mandatory_field()
    
    @pytest.mark.order(10)
    def test_edit_sla(self):
        self.sla = sla(self.driver)
        self.sla.edit_level("adaptor sla")
        self.sla.edit_description("this sla is created for testing purpose")
        self.sla.save_information()
        
    @pytest.mark.order(11)
    def test_edited_sla_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.level_in_listView("adaptor sla")
    
    @pytest.mark.order(12)
    def test_edit_option_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.list_view_edit_option("adaptor sla")
    
    @pytest.mark.order(13)
    def test_listView_edit_sla_mandatory_fields(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_mandatory_field()
    
    @pytest.mark.order(14)
    def test_listView_edit_sla(self):
        self.sla = sla(self.driver)
        self.sla.edit_level("adaptor sla_01")
        self.sla.edit_description("This is created for testing purpose")
        self.sla.save_information()
    
    @pytest.mark.order(15)
    def test_search_option(self):
        self.sla = sla(self.driver)
        self.sla.search_functionality("adaptor sla_01")