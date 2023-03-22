import time
from page_objects.entity_Management.asset import asset
from page_objects.entity_Management.medical_center import medical_centre
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure





@pytest.mark.usefixtures("init_driver")
class Test_Medical_Centre(unittest.TestCase):
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
    @allure.description("Should navigate to medical centre page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_01)
    def test_navigate_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.navigate_medical_centre()
    
    @allure.description("Should display the medical centre popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_02)
    def test_add_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.add_medical_centre() 

    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_03)
    def test_mandatory_fields(self):
       self.medical_centre = medical_centre(self.driver)
       self.medical_centre.create_medical_reason_mandatory_fields()
    
    @allure.description("Should able to create medical centre")
    @allure.severity(severity_level="CRITICAL")  
    @pytest.mark.order(9_04)
    def test_create_medical_centre(self):
       self.medical_centre = medical_centre(self.driver)
       self.medical_centre.hospital("Hospital_01")
       self.medical_centre.phone_number("+91","9933754995")
       self.medical_centre.address("New York")
       self.medical_centre.create_medical_centre()
    @allure.description("Should display the created hospital in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_05)
    def test_created_medical_centre_in_listView(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.medical_centre_in_listView("Hospital_01")
    
    @allure.description("Should view the created hospital")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_06)
    def test_view_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.view_medical_centre("Hospital_01")  
    @allure.description("Should display the edit medical centre popup window ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_07)
    def test_edit_button_in_view_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.edit_medical_center_button()

    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_08)
    def test_edit_mandatory_fields(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.edit_medical_centre_mandatory_field()
    @allure.description("Should able to edit and save the Medical Centre Fields and navigate to Medical Centre page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_09)
    def test_edit_medical_reason(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.hospital("Hospital_02")
        self.medical_centre.phone_number("+91","9933754999")
        self.medical_centre.address("New York")
        self.medical_centre.save_information() 

    @allure.description("Should able to select the edit option in hospital list view and display the edit medical centre popup window.")
    @allure.severity(severity_level="CRITICAL")    
    @pytest.mark.order(9_10)
    def test_listView_edit_asset(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.list_view_edit_option("Hospital_02")
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_11)    
    def test_listView_edit_mandatory_field(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.list_view_edit_mandatory_field()
    @allure.description("Should able to edit and save the medical centre fields in category list view option and navigate to medical centre page")
    @allure.severity(severity_level="CRITICAL")  
    @pytest.mark.order(9_12)
    def test_listView_edit_fields(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.address("USA")
        self.medical_centre.save_information() 
    @allure.description("Should able to search hospital using search functionality")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(9_13)
    def test_search_option(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.search_functionality("Hospital_02")

    