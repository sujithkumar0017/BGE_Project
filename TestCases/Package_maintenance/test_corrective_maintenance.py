import random
import time
from page_objects.corrective_maintenance import corrective_maintenance
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
from faker import Faker
from TestCases.Package_Client_02.test_client import Test_client




@pytest.mark.usefixtures("init_driver")
class Test_Corrective(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    fake = Faker()
    # @pytest.mark.order(2)
    # def test_login(self):
    #     self.driver.get(self.url)
    #     self.lp = login_Module(self.driver)
    #     self.lp.email(self.useremail)
    #     self.lp.password(self.password)
    #     self.lp.login()
    # @unittest.skipUnless(getattr(Test_client,"test_cases_completed",False),'Test_client file testcases did not ru successfully')
    @pytest.mark.order(2_01)
    def test_navigate_corrective_maintenance(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.navigate_to_corrective_maintenance()
    @pytest.mark.order(2_02)
    def test_add_corrective_ticket_btn(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_corrective_maintenance()
    @pytest.mark.order(2_03)
    def test_create_corrective_mandatory_fields(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.corrective_mandatory_fields()

    @pytest.mark.order(2_04)
    def test_add_corrective_maintenance(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.task_name("Test_ticket_corrective")
        self.corrective.priority(random.choice(["High", "Low","Normal"]))
        self.corrective.status("open")
        self.corrective.plant_name("Mobile_Plant")
        self.corrective.field_engineer("Mobile User")
        self.corrective.assigned_to("Mobile User")
        self.corrective.asset_category("Asset Category1")
        self.corrective.description("This is created for testing purpose")
        self.corrective.comment("This comment is for testing purpose")
        self.corrective.attachments()
        self.corrective.add_corrective()

    @pytest.mark.order(2_05)
    def test_corrective_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.corrective_ticket_listView("Test_ticket_corrective")

    @pytest.mark.order(2_06)
    def test_view_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_ticket("Test_ticket_corrective")

    @pytest.mark.order(2_07)
    def test_edit_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.ticketView_edit_button()

    @pytest.mark.order(2_08)
    def test_edit_fields(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.edit_ticket("Mobile_Sla", "8")

    # # #------------------Add Followup Task----------------------
    @pytest.mark.order(2_09)
    def test_add_followup_task_btn(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_addFollow_up_task()
    @pytest.mark.order(2_10)
    def test_create_followup_task_mandatory_fields(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.create_addfollowup_task_mandatory_fields()   
    @pytest.mark.order(2_11)
    def test_add_followUp_task(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.followup_task_name("_".join(["childtask",self.fake.name()]))
        self.corrective.followup_priority(random.choice(["High", "Low","Normal"]))
        self.corrective.followup_sla("Mobile_Sla")
        self.corrective.followup_status("open")
        self.corrective.plant_name("Mobile_Plant")
        self.corrective.followup_field_engineer("Mobile User")
        self.corrective.followup_assigned_to("Mobile User")
        self.corrective.followup_asset_category("Asset Category 51")
        self.corrective.followup_labour_hours("5")
        self.corrective.followup_description("This is created for testing purpose")
        self.corrective.followup_comment("This comment is for testing purpose")
        # self.corrective.followup_attachments()
        self.corrective.create_add_followup_task_button()

    @pytest.mark.order(2_12)
    def test_followup_task_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.followup_task_listview("Child_task_01")

    @pytest.mark.order(2_13)
    def test_edit_save_information(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.save_information_button()

    @pytest.mark.order(2_14)
    def test_followup_task_ticket_in_corrective_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.followup_ticket_visible_in_corrective_list_view("Child_task_01")

    @pytest.mark.order(2_15)
    def test_archive_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.archive_ticket("Test_ticket_corrective")

    @pytest.mark.order(2_16)
    def test_view_archive_ticket_list(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_archive_ticket_list()

    @pytest.mark.order(2_17)
    def test_archived_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.view_archived_ticket_in_list_view("Test_ticket_corrective")

    @pytest.mark.order(2_18)
    def test_unarchived_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.unarchived_ticket("Test_ticket_corrective")

    @pytest.mark.order(2_19)
    def test_unarchived_ticket_in_corrective_listView(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.unarchived_ticket_listView("Test_ticket_corrective")

    @pytest.mark.order(2_20)
    def test_number_of_tickets_count(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.ticket_listview_count()

    @pytest.mark.order(2_21)
    def test_search_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.search_corrective_ticket("Test_ticket_corrective")


    # def filter(self):
    #     self.corrective = corrective_maintenance(self.driver)
    #     self.corrective.status()
    #     time.sleep(3)
    #     self.corrective.assigned_engineer()
    #     time.sleep(3)
    #     self.corrective.plant_name()
    #     time.sleep(3)
    #     self.corrective.start_date()
    #     time.sleep(3) 
# suite_corrective_maintenance = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)
if __name__ == "__main__":
    unittest.TestLoader.sortTestMethodsUsing = None
    # unittest.TextTestRunner().run(suite_corrective_maintenance)
