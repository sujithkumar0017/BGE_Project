import time
from page_objects.entity_Management.SLA import sla
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure




@pytest.mark.usefixtures("init_driver")
class Test_SLA(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    # @pytest.mark.order(1)
    # def test_login(self):   
    #     self.driver.get(self.url)
    #     self.lp = login_Module(self.driver)
    #     self.lp.email(self.useremail)
    #     self.lp.password(self.password)
    #     self.lp.login()
    @allure.description("Should navigate to SLA page")
    @allure.severity(severity_level="CRITICAL")   
    @pytest.mark.order(11_01)
    def test_navigate_sla(self):
        self.sla =sla(self.driver)
        self.sla.navigate_sla() 
    @allure.description("Should display the SLA popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_02)
    def test_add_sla(self):
        self.sla = sla(self.driver)
        self.sla.add_sla()
    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_03)
    def test_mandatory_field(self):
        self.sla = sla(self.driver)
        self.sla.sla_mandatory_field()
    
    @allure.description("Should able to create SLA")
    @allure.severity(severity_level="CRITICAL")  
    @pytest.mark.order(11_04)
    def test_create_sla(self):
        self.sla = sla(self.driver)
        self.sla.level("mobile sla")
        self.sla.description("This is created for testing purpose")
        self.sla.create_sla()
    
    @allure.description("Should display the created SLA in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_05)
    def test_created_sla_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.level_in_listView("mobile sla")

    @allure.description("Should view the created SLA")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_06)
    def test_view_sla(self):
        self.sla = sla(self.driver)
        self.sla.view_level("mobile slaa")
   
    @allure.description("Should display the edit SLA popup window ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_07)
    def test_edit_option_in_view(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_button()
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_08)
    def test_edit_sla_mandatory_field(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_mandatory_field()
    @allure.description("Should able to edit and save the SLA Fields and navigate to SLA page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_09)
    def test_edit_sla(self):
        self.sla = sla(self.driver)
        self.sla.edit_level("adaptor sla")
        self.sla.edit_description("this sla is created for testing purpose")
        self.sla.save_information()
    
    @allure.description("Should the edited sla in list view")
    @allure.severity(severity_level="CRITICAL")     
    @pytest.mark.order(11_10)
    def test_edited_sla_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.level_in_listView("adaptor sla")
    @allure.description("Should able to select the edit option in Level list view and display the edit SLA popup window.")
    @allure.severity(severity_level="CRITICAL") 
    @pytest.mark.order(11_11)
    def test_edit_option_in_listView(self):
        self.sla = sla(self.driver)
        self.sla.list_view_edit_option("adaptor sla")
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_12)
    def test_listView_edit_sla_mandatory_fields(self):
        self.sla = sla(self.driver)
        self.sla.edit_sla_mandatory_field()
    @allure.description("Should able to edit and save the SLA fields in category list view option and navigate to SLA page")
    @allure.severity(severity_level="CRITICAL") 
    @pytest.mark.order(11_13)
    def test_listView_edit_sla(self):
        self.sla = sla(self.driver)
        self.sla.edit_level("adaptor sla_01")
        self.sla.edit_description("This is created for testing purpose")
        self.sla.save_information()
    @allure.description("Should able to search level using search functionality")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(11_14)
    def test_search_option(self):
        self.sla = sla(self.driver)
        self.sla.search_functionality("adaptor sla_01")