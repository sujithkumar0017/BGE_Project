import time
import pytest
import unittest
from pageObjects.client_Module import Client
from pageObjects.login_Module import login_Module
from utilities.dd_using_json import random_data
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By

# from ddt import ddt, data, file_data, unpack
import json


@pytest.mark.usefixtures("setup_class")
class Test_client(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # def setup_class(self):
    #     self.faker = random_data()
    #     self.faker.data()
    #     with open(
    #         "/home/sujith/codebase/BGE_Framework_Design/utilities/client.json"
    #     ) as json_file:
    #         self.data = json.load(json_file)

    @pytest.mark.order(1)
    def test_login(self):
        self.driver.get(self.url)
        self.lp = login_Module(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()

    @pytest.mark.order(2)
    def test_navigate_to_(self):
        self.client = Client(self.driver)
        self.client.navigate_to_client_page()

    @pytest.mark.order(3)
    def test_add_client_btn(self):
        self.client = Client(self.driver)
        self.client.add_Client()

    @pytest.mark.order(4)
    def test_create_client_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.client_mandatory_field()

    @pytest.mark.order(5)
    def test_create_client(self):
        self.client = Client(self.driver)
        self.client.name("client_user_02")
        self.client.phone_number("+91", "9933227888")
        self.client.address("New York")
        self.client.mobile_number("+91", "8882332311")
        self.client.email_address("admin055@yopmail.com")
        self.client.city("chennai")  # self.client.email_address(data["email"])
        self.client.postal_code("602002")
        self.client.website("www.google.com")
        self.client.task_visibility(["Open", "Completed"])
        self.client.plant(["Mobile_Plant"])

    @pytest.mark.order(6)
    def test_add_plant_btn_in_add_client_page(self):
        self.client = Client(self.driver)
        self.client.add_plant_in_client_page()

    @pytest.mark.order(7)
    def test_add_plant_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.plantCreation_mandatory_fields()

    @pytest.mark.order(8)
    def test_create_plant(self):
        self.client = Client(self.driver)
        self.client.plant_name("user_plant_view")
        self.client.size("90")
        self.client.acronym("NXTP001")
        self.client.on_boardingDate()
        self.client.status("Active")
        self.client.add_plant()

    @pytest.mark.order(9)
    def test_created_plant_in_list_view(self):
        self.client = Client(self.driver)
        self.client.created_plant_in_list_view("user_plant_view")

    # Add User
    @pytest.mark.order(10)
    def test_add_user_in_add_client_page(self):
        self.client = Client(self.driver)
        self.client.client_page_addUser()

    @pytest.mark.order(11)
    def test_add_user_mandatory_fields(self):
        self.client = Client(self.driver)
        self.client.userCreation_mandatory_fields()

    @pytest.mark.order(12)
    def test_create_user(self):
        self.client = Client(self.driver)
        self.client.user_firstName("user")
        self.client.user_lastName("category")
        self.client.user_email("user09333@yopmail.com")
        self.client.user_password("qwerty123")
        self.client.addUser()

    @pytest.mark.order(13)
    def test_created_user_in_list_view(self):
        self.client = Client(self.driver)
        self.client.created_user_in_list_view("user")

    @pytest.mark.order(14)
    def test_create_client_button(self):
        self.client = Client(self.driver)
        self.client.createClient()

    @pytest.mark.order(15)
    def test_created_client_in_listview(self):
        self.client = Client(self.driver)
        self.client.created_client_in_listView("client_user_02")

    @pytest.mark.order(16)
    def test_view_created_client(self):
        self.client = Client(self.driver)
        self.client.client_view("client_user_02")

    @pytest.mark.order(17)
    def test_edit_client_button_view(self):
        self.client = Client(self.driver)
        self.client.view_edit_client_page()

    @pytest.mark.order(18)
    def test_edit_client_mandatory_field(self):
        self.client = Client(self.driver)
        self.client.edit_client_mandatory_field()

    @pytest.mark.order(19)
    def test_edit_client(self):
        self.client = Client(self.driver)
        self.client.name("client_user_03")

    @pytest.mark.order(20)
    def test_edit_client_save_information_btn(self):
        self.client = Client(self.driver)
        self.client.save_information_btn()

    @pytest.mark.order(21)
    def test_list_view_edit_option(self):
        self.client = Client(self.driver)
        self.client.edit_client_dropdown("client_user_03")

    @pytest.mark.order(22)
    def test_list_view_edit_client(self):
        self.client = Client(self.driver)
        self.client.attachments()

    @pytest.mark.order(23)
    def test_list_view_edit_save_information(self):
        self.client = Client(self.driver)
        self.client.save_information_btn()

    @pytest.mark.order(24)
    def test_archived_client(self):
        self.client = Client(self.driver)
        self.client.archive_user("client_user_03")

    @pytest.mark.order(25)
    def test_view_client_archive_list(self):
        self.client = Client(self.driver)
        self.client.view_archive_client_list()

    @pytest.mark.order(26)
    def test_view_archived_client(self):
        self.client = Client(self.driver)
        self.client.archived_client_listview("client_user_03")

    @pytest.mark.order(27)
    def test_unarchived_client(self):
        self.client = Client(self.driver)
        self.client.unarchived_client("client_user_03")

    @pytest.mark.order(28)
    def test_unarchived_client_in_list_view(self):
        self.client = Client(self.driver)
        self.client.unarchived_client_listView("client_user_03")

    @pytest.mark.order(29)
    def test_total_client_count(self):
        self.client = Client(self.driver)
        self.client.ticket_listview_count()

    @pytest.mark.order(30)
    def test_search_client_functionality(self):
        self.client = Client(self.driver)
        self.client.search_client("client_user_03")

    @pytest.mark.order(31)
    def test_create_client_existing_client(self):
        self.client = Client(self.driver)
        self.client.add_Client()
        self.client.email_address("admin055@yopmail.com")
        self.client.create_client_with_existing_emailid()


if __name__ == "__main__":
    unittest.main()
