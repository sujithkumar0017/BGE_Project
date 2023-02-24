import time
from pageObjects.enityManagement.asset import asset
from pageObjects.enityManagement.medical_center import medical_centre
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest





@pytest.mark.usefixtures("setup_class")
class Test_Medical_Centre(unittest.TestCase):
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
    def test_navigate_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.navigate_medical_centre()
    @pytest.mark.order(3)
    def test_add_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.add_medical_centre() 
    @pytest.mark.order(4)
    def test_mandatory_fields(self):
       self.medical_centre = medical_centre(self.driver)
       self.medical_centre.create_medical_reason_mandatory_fields()
    
    @pytest.mark.order(5)
    def test_create_medical_centre(self):
       self.medical_centre = medical_centre(self.driver)
       self.medical_centre.hospital("Hospital_01")
       self.medical_centre.phone_number("+91","9933754995")
       self.medical_centre.address("New York")
       self.medical_centre.create_medical_centre()
    
    @pytest.mark.order(6)
    def test_created_medical_centre_in_listView(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.medical_centre_in_listView("Hospital_01")
    
    @pytest.mark.order(7)
    def test_view_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.view_medical_centre("Hospital_01")  
    
    @pytest.mark.order(8)
    def test_edit_button_in_view_medical_centre(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.edit_medical_center_button()
    
    @pytest.mark.order(9)
    def test_edit_mandatory_fields(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.edit_medical_centre_mandatory_field()
    
    @pytest.mark.order(10)
    def test_edit_medical_reason(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.hospital("Hospital_02")
        self.medical_centre.phone_number("+91","9933754999")
        self.medical_centre.address("New York")
        self.medical_centre.save_information() 
    
    @pytest.mark.order(11)
    def test_listView_edit_asset(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.list_view_edit_option("Hospital_02")
    @pytest.mark.order(12)    
    def test_listView_edit_mandatory_field(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.list_view_edit_mandatory_field()
    @pytest.mark.order(13)
    def test_listView_edit_fields(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.address("USA")
        self.medical_centre.save_information() 
    @pytest.mark.order(14)
    def test_search_option(self):
        self.medical_centre = medical_centre(self.driver)
        self.medical_centre.search_functionality("Hospital_02")

    