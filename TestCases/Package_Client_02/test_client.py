import time
import pytest
import unittest
from page_objects.client_module import Client
from page_objects.login_Module import login_Module
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
import allure
from TestCases.Package_Client_02.Client_json import random_data

# from ddt import ddt, data, file_data, unpack
import json


@pytest.mark.usefixtures("init_driver")
# @pytest.mark.order_class(01)
class Test_client(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def setup_class(self):
        self.faker = random_data()
        self.faker.data()
        with open(
            "/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02/client.json"
        ) as json_file:
            self.data = json.load(json_file)
    # @pytest.mark.order(1_01)
    # def test_login(self):
    #     self.driver.get(self.url)
    #     self.lp = login_Module(self.driver)
    #     self.lp.email(self.useremail)
    #     self.lp.password(self.password)
    #     self.lp.login()
    @allure.description("Should navigate to Client Page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_02)
    def test_navigate_to_client_page2(self):
        self.client = Client(self.driver)
        self.client.navigate_to_client_page()
    @allure.description("Should navigate to Add Client Page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_03)
    def test_add_client_btn(self):
        self.client = Client(self.driver)
        self.client.add_Client()
    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_04)
    def test_create_client_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.client_mandatory_field()
    @allure.description("Should able enter the given data to respective fields")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_05)
    def test_create_client(self):
        self.client = Client(self.driver)
        self.client.name(self.data["name"])
        self.client.phone_number(self.data["phone_number_countryCode"],self.data["phone_number"])
        self.client.address(self.data["address"])
        self.client.mobile_number(self.data["mobile_number_countryCode"],self.data["mobile_number"])
        self.client.email_address(self.data["email"])
        self.client.city(self.data["city"])  
        self.client.postal_code(self.data["postalCode"])
        self.client.website(self.data["website"])
        self.client.task_visibility(["Open", "Completed"])
        self.client.plant(["Mobile_Plant"])
    @allure.description("Should display the Plant Popup.")
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.order(1_06)
    def test_add_plant_btn_in_add_client_page(self):
        self.client = Client(self.driver)
        self.client.add_plant_in_client_page()
    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_07)
    def test_add_plant_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.plantCreation_mandatory_fields()
    @allure.description("Should able to add the plant on the client creation page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_08)
    def test_create_plant(self):
        self.client = Client(self.driver)
        self.client.plant_name(self.data["plant_name"])
        self.client.size(self.data["size"])
        self.client.acronym(self.data["acronym"])
        self.client.on_boardingDate()
        self.client.status("Active")
        self.client.add_plant()
    @allure.description("Should display the created plant on list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_09)
    def test_created_plant_in_list_view(self):
        self.client = Client(self.driver)
        self.client.created_plant_in_list_view(self.data["plant_name"])
    @allure.description("Should display the User Popup Window")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_10)
    def test_add_user_in_add_client_page(self):
        self.client = Client(self.driver)
        self.client.client_page_addUser()
    
    @allure.description("Should display the validation message on mandatory fields")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_11)
    def test_add_user_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.userCreation_mandatory_fields()
    @allure.description("Should add the user on the client creation page")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_12)
    def test_create_user(self):
        self.client = Client(self.driver)
        self.client.user_firstName(self.data["user_first_name"])
        self.client.user_lastName(self.data["user_last_name"])
        self.client.user_email(self.data["user_email"])
        self.client.user_password(self.data["user_password"])
        self.client.addUser()

    @allure.description("Should display the created user on list view")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_13)
    def test_created_user_in_list_view(self):
        self.client = Client(self.driver)
        self.client.created_user_in_list_view(self.data["user_first_name"])
    @allure.description("Should create the client and display the toast message")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_14)
    def test_create_client_button(self):
        self.client = Client(self.driver)
        self.client.createClient()
    @allure.description("Should display the created client on the List View.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_15)
    def test_created_client_in_listview(self):
        self.client = Client(self.driver)
        self.client.created_client_in_listView(self.data["name"])
    @allure.description("Should able to view the created client")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_16)
    def test_view_created_client(self):
        self.client = Client(self.driver)
        self.client.client_view(self.data["name"])
    @allure.description("Should able click the edit button and navigate to Edit Page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_17)
    def test_edit_client_button_view(self):
        self.client = Client(self.driver)
        self.client.view_edit_client_page()
    @allure.description("Should validate the mandatory fields")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_18)
    def test_edit_client_mandatory_field(self):
        self.client = Client(self.driver)
        self.client.edit_client_mandatory_field()
    @allure.description("Should able to edit the client")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_19)
    def test_edit_client(self):
        self.client = Client(self.driver)
        self.client.name(self.data["edit_name"])
    @allure.description("Should save the edited client.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_20)
    def test_edit_client_save_information_btn(self):
        self.client = Client(self.driver)
        self.client.save_information_btn()
    @allure.description("Should able to click on edit button in client listview and navigate to edit client page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_21)
    def test_list_view_edit_option(self):
        self.client = Client(self.driver)
        self.client.edit_client_dropdown(self.data["edit_name"])
    @allure.description("Should able to add attachments in edit client screen")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_22)
    def test_list_view_edit_client(self):
        self.client = Client(self.driver)
        self.client.attachments()

    @allure.description("Should save the attachment and navigate to client page.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_23)
    def test_list_view_edit_save_information(self):
        self.client = Client(self.driver)
        self.client.save_information_btn()
    @allure.description("Should able to click on archive client button in client listview and able to archive the client")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_24)
    def test_archived_client(self):
        self.client = Client(self.driver)
        self.client.archive_user(self.data["edit_name"])
    @allure.description("Should navigate archive page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_25)
    def test_view_client_archive_list(self):
        self.client = Client(self.driver)
        self.client.view_archive_client_list()
    @allure.description("Should able to view the archived client in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_26)
    def test_view_archived_client(self):
        self.client = Client(self.driver)
        self.client.archived_client_listview(self.data["edit_name"])
    @allure.description("Should able to click on unarchive client button in client listview and able to unarchive the client")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(1_27)
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_28)
    def test_total_client_count(self):
        self.client = Client(self.driver)
        self.client.ticket_listview_count()
    @allure.description("Should able to search the client using search option")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_29)
    def test_search_client_functionality(self):
        self.client = Client(self.driver)
        self.client.search_client(self.data["edit_name"])
    @allure.description("Should display the validation popup on creating the client with existing email id")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(1_30)
    def test_create_client_existing_client(self):
        self.client = Client(self.driver)
        self.client.add_Client()
        self.client.name(self.data["edit_name"])
        self.client.email_address(self.data["email"])
        self.client.create_client_with_existing_email_id()

    


if __name__ =="__main__":
    # unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()