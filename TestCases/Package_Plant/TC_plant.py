import time
import unittest
from page_objects.corrective_maintenance import corrective_maintenance
from page_objects.remedial_maintenance import remedial_maintenance
from page_objects.plant_module import Plant
import pytest
from page_objects.login_Module import login_Module
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("init_driver")
class Test_plant(unittest.TestCase):
    # corrective = Test_Corrective()

    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.order(1)
    def test_login(self):
        self.driver.get(self.url)
        self.login = login_Module(self.driver)
        self.login.email(self.useremail)
        self.login.password(self.password)
        self.login.login()

    @pytest.mark.order(2)
    def test_navigate_to_plant(self):
        self.plant = Plant(self.driver)
        self.plant.navigate_plant()

    @pytest.mark.order(3)
    def test_add_plant_btn(self):
        self.plant = Plant(self.driver)
        self.plant.add_plant()

    @pytest.mark.order(4)
    def test_create_plant_mandatory_fields(self):
        self.plant = Plant(self.driver)
        self.plant.create_plant_mandatory_field()

    @pytest.mark.order(5)
    def test_create_plant(self):
        self.plant = Plant(self.driver)
        self.plant.plant_name("Plant_Diamond_015")
        self.plant.size("9")
        self.plant.acronym("XWERTY143")
        self.plant.on_boarding_date()
        self.plant.client_name("client_user_03")
        self.plant.status("Active")
        self.plant.create_plant_btn()

    @pytest.mark.order(6)
    def test_created_plant_in_list_view(self):
        self.plant = Plant(self.driver)
        self.plant.plant_in_listView("Plant_Diamond_015")

    @pytest.mark.order(7)
    def test_view_created_plant(self):
        self.plant = Plant(self.driver)
        self.plant.view_plant("Plant_Diamond_015")

    @pytest.mark.order(8)
    def test_edit_btn_in_view_plant(self):
        self.plant = Plant(self.driver)
        self.plant.edit_button_view_plant()

    @pytest.mark.order(9)
    def test_edit_plant(self):
        self.plant = Plant(self.driver)
        self.plant.plant_manager("Admin user")
        self.plant.team_leader("Mobile User")
        self.plant.field_engineer("Mobile User")
        self.plant.postal_code("894432")
        self.plant.address("Chennai")
        self.plant.save_information()

    @pytest.mark.order(10)
    def test_corrective_tab(self):
        self.plant = Plant(self.driver)
        self.plant.corrective_maintenance_tab_in_view_plant()

    @pytest.mark.order(11)
    def test_add_btn_in_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_corrective_maintenance()

    @pytest.mark.order(12)
    def test_create_corrective_ticket_plant_name_were_displayed(self):
        self.plant = Plant(self.driver)
        self.plant.validate_plant_name_in_create_corrective_ticket("Plant_Diamond")

    @pytest.mark.order(13)
    def test_create_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.task_name("task_corrective_ticket")
        self.corrective.priority("High")
        self.corrective.status("open")
        self.corrective.plant_name("Plant_Diamond_015")
        self.corrective.field_engineer("Mobile User")
        self.corrective.assigned_to("Mobile User")
        self.corrective.asset_category("Asset Category 51")
        self.corrective.description("This is created for testing purpose")
        self.corrective.comment("This comment is for testing purpose")
        self.corrective.add_corrective()

    @pytest.mark.order(14)
    def test_corrective_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.corrective_ticket_listView("task_corrective_ticket")

    @pytest.mark.order(15)
    def test_navigate_to_remedial_tab_in_view_plant(self):
        self.plant = Plant(self.driver)
        self.plant.remedial_maintenance_tab_in_view_plant()

    @pytest.mark.order(16)
    def test_add_btn_in_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.add_remedial_maintenance()

    @pytest.mark.order(17)
    def test_create_remedial_ticket_plant_name_were_displayed(self):
        self.plant = Plant(self.driver)
        self.plant.validate_plant_name_in_create_remedial_ticket("Plant_Diamond_015")

    @pytest.mark.order(18)
    def test_create_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("ticket_issue_01")
        self.remedial.priority("Low")
        self.remedial.status("Open")
        self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.asset_category("Asset Category 51")
        self.remedial.create_remedial_maintenance()

    @pytest.mark.order(19)
    def test_created_ticket_in_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("ticket_issue_01")
