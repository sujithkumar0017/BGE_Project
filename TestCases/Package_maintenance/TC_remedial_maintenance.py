import time
from pageObjects.remedial_maintenance import remedial_maintenance
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest


@pytest.mark.usefixtures("setup_class")
class Test_Remedial(unittest.TestCase):
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
    def test_navigate_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.navigate_to_remedial_maintenance()

    @pytest.mark.order(3)
    def test_add_remedial_ticket_btn(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.add_remedial_maintenance()

    @pytest.mark.order(4)
    def test_create_remedial_mandatory_fields(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_mandatory_fields()

    @pytest.mark.order(5)
    def test_create_remedial_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("ticket_issue_01")
        self.remedial.priority("Low")
        self.remedial.status("Open")
        self.remedial.plant_name("Mobile_Plant")
        self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.asset_category("Asset Category 51")
        self.remedial.create_remedial_maintenance()

    @pytest.mark.order(6)
    def test_created_ticket_in_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("ticket_issue_01")

    @pytest.mark.order(7)
    def test_view_created_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.view_remedial_task("ticket_issue_01")

    @pytest.mark.order(8)
    def test_edit_button_in_view_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.ticketView_edit_button()

    @pytest.mark.order(9)
    def test_edit_ticket_mandatory_fields(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.edit_mandatory_field()

    @pytest.mark.order(10)
    def test_edit_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("ticket_issue_02")
        # self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.comment("This Created for testing purpose")
        self.remedial.save_information()

    @pytest.mark.order(11)
    def test_edited_ticket_in_listview(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("ticket_issue_02")

    @pytest.mark.order(12)
    def test_listview_menu_editClient(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.edit_plant_dropdown("ticket_issue_02")
        self.remedial.edit_mandatory_field()
        self.remedial.task_name("ticket_issue_03")
        # self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.save_information()

    @pytest.mark.order(13)
    def test_archive_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.archive_ticket("ticket_issue_03")

    @pytest.mark.order(14)
    def test_view_ticket_in_archive_list(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.view_archive_list()
        self.remedial.archived_ticket_listview("ticket_issue_03")

    @pytest.mark.order(15)
    def test_unarchived_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.unarchived_ticket("ticket_issue_03")

    @pytest.mark.order(16)
    def test_unarchived_ticket_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.unarchived_ticket_listView("ticket_issue_03")

    @pytest.mark.order(17)
    def test_ticket_count_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.ticket_listview_count()

    @pytest.mark.order(18)
    def test_search_created_ticket(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.search_remedial_ticket("ticket_issue_03")
