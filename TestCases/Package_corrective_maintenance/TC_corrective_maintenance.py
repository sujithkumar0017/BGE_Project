import time
from pageObjects.corrective_maintenance import corrective_maintenance
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest


@pytest.mark.usefixtures("setup_class")
class Test_Corrective(unittest.TestCase):
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
    def test_navigate_corrective_maintenance(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.navigate_to_corrective_maintenance()
    @pytest.mark.order(3)
    def test_add_corrective_maintenance(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_corrective_maintenance()
        self.corrective.corrective_mandatory_fields()
        self.corrective.task_name("task_corrective_ticket")
        self.corrective.priority("High")
        self.corrective.status("open")
        self.corrective.plant_name("Mobile_Plant")
        self.corrective.field_engineer("Mobile User")
        self.corrective.assigned_to("Mobile User")
        self.corrective.asset_category("Asset Category1")
        self.corrective.description("This is created for testing purpose")
        self.corrective.comment("This comment is for testing purpose")
        self.corrective.attachments()
        self.corrective.add_corrective()
    @pytest.mark.order(4)
    def test_corrective_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.corrective_ticket_listView("task_corrective_ticket")
    @pytest.mark.order(5)
    def test_view_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_ticket("task_corrective_ticket")
    @pytest.mark.order(6)
    def test_edit_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.ticketView_edit_button()
    @pytest.mark.order(7)
    def test_edit_fields(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.edit_ticket("Mobile_Sla","8")
    # #------------------Add Followup Task----------------------
    @pytest.mark.order(8)
    def test_add_followUp_task(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_addFollow_up_task()
        self.corrective.create_addfollowup_task_mandatory_fields()
        self.corrective.followup_task_name("Child_task_01")
        self.corrective.followup_priority("high")
        self.corrective.followup_sla("TestName4")
        self.corrective.followup_status("open")
        # self.corrective.plant_name("Dr. Janice Mosciski")
        self.corrective.followup_field_engineer("Mobile User")
        self.corrective.followup_assigned_to("Mobile User")
        self.corrective.followup_asset_category("Asset Category1")
        self.corrective.followup_labour_hours("5")
        self.corrective.followup_description("This is created for testing purpose")
        self.corrective.followup_comment("This comment is for testing purpose")
        # self.corrective.followup_attachments()
        self.corrective.create_add_followup_task_button()
    @pytest.mark.order(9)
    def test_followup_task_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.followup_task_listview("Child_task")
    @pytest.mark.order(10)
    def test_edit_save_information(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.save_information_button()
    @pytest.mark.order(11)
    def test_followup_task_ticket_in_corrective_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.followup_ticket_visible_in_corrective_list_view("Child_task")

    @pytest.mark.order(12)
    def test_archive_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.archive_ticket("task_corrective_ticket")
    @pytest.mark.order(13)
    def test_view_archive_ticket_list(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_archive_ticket_list()
    @pytest.mark.order(14)
    def test_archived_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_archived_ticket_in_list_view("task_corrective_ticket")
    @pytest.mark.order(15)
    def test_unarchived_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.unarchived_ticket("task_corrective_ticket")
    @pytest.mark.order(16)
    def test_unarchived_ticket_in_corrective_listView(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.unarchived_ticket_listView("task_corrective_ticket")
    @pytest.mark.order(17)
    def test_number_of_tickets_count(self): 
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.ticket_listview_count()
    @pytest.mark.order(18)
    def test_search_corrective_ticket(self):  
        self.corrective = corrective_maintenance(self.driver)  
        self.corrective.search_corrective_ticket("task_corrective_ticket")
    def filter(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.status()
        time.sleep(3)
        self.corrective.assigned_engineer()
        time.sleep(3)
        self.corrective.plant_name()
        time.sleep(3)
        self.corrective.start_date()
        time.sleep(3)
        