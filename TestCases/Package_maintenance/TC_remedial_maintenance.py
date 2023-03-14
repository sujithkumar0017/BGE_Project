import time
from page_objects.remedial_maintenance import remedial_maintenance
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest


@pytest.mark.usefixtures("init_driver")
class Test_Remedial(unittest.TestCase):
    # def __init__(self, driver):
    #     self.driver = driver
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # @pytest.mark.order(3_01)
    # def test_login(self):
    #     self.driver.get(self.url)
    #     self.lp = login_Module(self.driver)
    #     self.lp.email(self.useremail)
    #     self.lp.password(self.password)
    #     self.lp.login()
    
    @pytest.mark.order(4_01)
    def test_navigate_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.navigate_to_remedial_maintenance()

    @pytest.mark.order(4_02)
    def test_add_remedial_ticket_btn(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.add_remedial_maintenance()

    @pytest.mark.order(4_03)
    def test_create_remedial_mandatory_fields(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_mandatory_fields()

    @pytest.mark.order(4_04)
    def test_create_remedial_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("test_ticket_remedial_01")
        self.remedial.priority("Low")
        self.remedial.status("Open")
        self.remedial.plant_name("Mobile_Plant")
        self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.asset_category("Asset Category 51")
        self.remedial.create_remedial_maintenance()

    @pytest.mark.order(4_05)
    def test_created_ticket_in_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("test_ticket_remedial_01")

    @pytest.mark.order(4_06)
    def test_view_created_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.view_remedial_task("test_ticket_remedial_01")

    @pytest.mark.order(4_07)
    def test_edit_button_in_view_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.ticketView_edit_button()

    @pytest.mark.order(4_08)
    def test_edit_ticket_mandatory_fields(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.edit_mandatory_field()

    @pytest.mark.order(4_09)
    def test_edit_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("test_ticket_remedial_02")
        # self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.comment("This Created for testing purpose")
        self.remedial.save_information()

    @pytest.mark.order(4_10)
    def test_edited_ticket_in_listview(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("test_ticket_remedial_02")

    @pytest.mark.order(4_11)
    def test_listview_menu_editClient(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.edit_plant_dropdown("test_ticket_remedial_02")
        self.remedial.edit_mandatory_field()
        self.remedial.task_name("test_ticket_remedial_03")
        # self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.save_information()

    @pytest.mark.order(4_12)
    def test_archive_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.archive_ticket("test_ticket_remedial_03")

    @pytest.mark.order(4_13)
    def test_view_ticket_in_archive_list(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.view_archive_list()
        self.remedial.archived_ticket_listview("test_ticket_remedial_03")

    @pytest.mark.order(4_14)
    def test_unarchived_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.unarchived_ticket("test_ticket_remedial_03")

    @pytest.mark.order(4_15)
    def test_unarchived_ticket_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.unarchived_ticket_listView("test_ticket_remedial_03")

    @pytest.mark.order(4_16)
    def test_ticket_count_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.ticket_listview_count()

    @pytest.mark.order(4_17)
    def test_search_created_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.search_remedial_ticket("test_ticket_remedial_03")
