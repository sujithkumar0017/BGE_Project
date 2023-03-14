import time
from page_objects.entity_Management.failure_reason import failure_reason
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure





@pytest.mark.usefixtures("init_driver")
class Test_Failure_Reason(unittest.TestCase):
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
    @allure.description("Should navigate to failure reason page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_01)
    def test_navigate_failure_reason(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.navigate_failure_reason()
    @allure.description("Should display the failure reason popup window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_02)
    def test_add_failure_reason(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.add_failure_reason()
    
    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_03)
    def test_mandatory_fields(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.failure_reason_mandatory_fields()
    
    @allure.description("Should able to create failure reason")
    @allure.severity(severity_level="CRITICAL") 
    @pytest.mark.order(7_04)
    def test_create_failure_reason(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.name("Adaptor issue 5")
        self.failure_reason.create_failure_reason()

    @allure.description("Should display the created failure reason in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_05)
    def test_created_failure_reason_in_listView(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.failure_reason_in_listView("Adaptor issue 5")  

    @allure.description("Should view the created failure reason")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_06)
    def test_view_failure_reason(self):
        self.failure_reason =failure_reason(self.driver)  
        self.failure_reason.view_failure_reason("Adaptor issue 5")    
    @allure.description("Should display the edit failure reason popup window ")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_07)
    def test_edit_button_in_view_failure_reason(self):
        self.failure_reason =failure_reason(self.driver) 
        self.failure_reason.edit_failure_reason_button()

    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_08)
    def test_edit_mandatory_fields(self):
        self.failure_reason =failure_reason(self.driver)
        self.failure_reason.edit_failure_reason_mandatory_field() 

    @allure.description("Should able to edit and save the failure reason and navigate to failure reason page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_09)
    def test_edit_failure_reason(self):
        self.failure_reason =failure_reason(self.driver) 
        self.failure_reason.edit_name("Adaptor issue 51")  
        self.failure_reason.save_information_button()
    @allure.description("Should able to edit and save the failure reason in category list view option")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_10)
    def test_edit_option_in_listView(self):
        self.failure_reason = failure_reason(self.driver)
        self.failure_reason.list_view_edit_option("Adaptor issue 51")
        self.failure_reason.edit_failure_reason_mandatory_field()
        self.failure_reason.edit_name("Adaptor issue 512")  
        self.failure_reason.save_information_button()
    @allure.description("Should able to search category using search functionality")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(7_11)
    def test_search_option_listView(self):
        self.failure_reason = failure_reason(self.driver)
        self.failure_reason.search_functionality("Adaptor issue 512")
    