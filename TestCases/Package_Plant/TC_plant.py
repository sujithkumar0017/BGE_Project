import time
import unittest
from page_objects.corrective_maintenance import corrective_maintenance
from page_objects.remedial_maintenance import remedial_maintenance
from page_objects.plant_module import Plant
import pytest
from page_objects.login_Module import login_Module
from utilities.readProperties import ReadConfig
import allure

@pytest.mark.usefixtures("init_driver")
class Test_plant(unittest.TestCase):
    # corrective = Test_Corrective()

    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # @pytest.mark.order(1)
    # def test_login(self):
    #     self.driver.get(self.url)
    #     self.login = login_Module(self.driver)
    #     self.login.email(self.useremail)
    #     self.login.password(self.password)
    #     self.login.login()
    @allure.description("Should navigate to PV-Plant Page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_01)
    def test_navigate_to_plant(self):
        self.plant = Plant(self.driver)
        self.plant.navigate_plant()
    
    @allure.description("Should navigate to Add PV-Plant Page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_02)
    def test_add_plant_btn(self):
        self.plant = Plant(self.driver)
        self.plant.add_plant()

    @allure.description("Should display the validation message on the mandatory field")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_03)
    def test_create_plant_mandatory_fields(self):
        self.plant = Plant(self.driver)
        self.plant.create_plant_mandatory_field()
   
    @allure.description("Should able to create PV-Plant Successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_04)
    def test_create_plant(self):
        self.plant = Plant(self.driver)
        self.plant.plant_name("Plant_Diamond_015")
        self.plant.size("9")
        self.plant.acronym("XWERTY556")
        self.plant.on_boarding_date()
        self.plant.client_name("client_user_03")
        self.plant.status("Active")
        self.plant.create_plant_btn()

    @allure.description("Should display the created PV-Plant in list view on Plant data table Successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_05)
    def test_created_plant_in_list_view(self):
        self.plant = Plant(self.driver)
        self.plant.plant_in_listView("Plant_Diamond_015")

    @allure.description("Should able to view  the created PV-Plant Successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_06)
    def test_view_created_plant(self):
        self.plant = Plant(self.driver)
        self.plant.view_plant("Plant_Diamond_015")

    @allure.description("Should navigate and display the Edit Pv-plant Page.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_07)
    def test_edit_btn_in_view_plant(self):
        self.plant = Plant(self.driver)
        self.plant.edit_button_view_plant()
    @allure.description("Should able to edit the plant")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_08)
    def test_edit_plant(self):
        self.plant = Plant(self.driver)
        self.plant.plant_manager("Admin user")
        self.plant.team_leader("Mobile User")
        self.plant.field_engineer("Mobile User")
        self.plant.postal_code("894432")
        self.plant.address("Chennai")
        
    @allure.description("Should able to save the edited plant.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_09)
    def test_edit_client_save_information_btn(self):
        self.plant = Plant(self.driver)
        self.plant.save_information()

    @allure.description("Should navigate to corrective maintenance Tab Successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_10)
    def test_corrective_tab(self):
        self.plant = Plant(self.driver)
        self.plant.corrective_maintenance_tab_in_view_plant()

    @allure.description("Should open the add corrective maintenance Popup window successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_11)
    def test_add_btn_in_corrective_ticket(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.add_corrective_maintenance()
    
    @allure.description("Should display the created plant name on the plant name which is non-editable field successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_12)
    def test_create_corrective_ticket_plant_name_were_displayed(self):
        self.plant = Plant(self.driver)
        self.plant.validate_plant_name_in_create_corrective_ticket("Plant_Diamond")

    @allure.description("Should able to add the Corrective ticket successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_13)
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

    @allure.description("Should display the corrective ticket in corrective ticket list view successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_14)
    def test_corrective_ticket_in_list_view(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.corrective_ticket_listView("task_corrective_ticket")
    @allure.description("Should navigate to remedial maintenance tab successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_15)
    def test_navigate_to_remedial_tab_in_view_plant(self):
        self.plant = Plant(self.driver)
        self.plant.remedial_maintenance_tab_in_view_plant()
    @allure.description("Should display the  add remedial ticket popup window successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_16)
    def test_add_btn_in_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.add_remedial_maintenance()
    @allure.description("Should display the created plant name on the plant name which is non-editable field successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_17)
    def test_create_remedial_ticket_plant_name_were_displayed(self):
        self.plant = Plant(self.driver)
        self.plant.validate_plant_name_in_create_remedial_ticket("Plant_Diamond_015")
    @allure.description("Should able to create the remedial ticket successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_18)
    def test_create_remedial_maintenance(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.task_name("ticket_issue_01")
        self.remedial.priority("Low")
        self.remedial.status("Open")
        self.remedial.field_engineer("Mobile User")
        self.remedial.assigned_to("Mobile User")
        self.remedial.asset_category("Asset Category 51")
        self.remedial.create_remedial_maintenance()
    @allure.description("Should display the remedial ticket in remedial tickets list view successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_19)
    def test_created_ticket_in_list_view(self):
        self.remedial = remedial_maintenance(self.driver)
        self.remedial.remedial_task_in_listView("ticket_issue_01")

    @allure.description("Should navigate to pv-plants page Successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_20)
    def test_back_functionality(self):
        self.plant = Plant(self.driver)
        self.plant.back_functionality()

    @allure.description("Should able to click on edit button in plant listview and navigate to edit plant page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_21)    
    def test_list_view_edit_plant(self):
        self.plant = Plant(self.driver)
        self.plant.edit_plant_dropdown("Plant_Diamond_015")
        self.plant.dno("Add_hospital")
        self.plant.hospital("data plant")
    
    @allure.description("Should able to save the edited data and navigate to plant page successfully")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_22)    
    def test_list_view_edit_save_information(self):
        self.plant = Plant(self.driver)
        self.plant.save_information()
    
    @allure.description("Should able to click on archive plant button in plant listview and able to archive the client")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_23)
    def test_archived_plant(self):
        self.plant = Plant(self.driver)
        self.plant.archive_user("Plant_Diamond_015")

    @allure.description("Should navigate archive page")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_24)
    def test_view_plant_archive_list_page(self):
        self.plant = Plant(self.driver)
        self.plant.view_archive_plant()  

    @allure.description("Should able to view the archived plant in list view")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_25)  
    def test_view_archived_list_view(self):
        self.plant = Plant(self.driver)
        self.plant.archived_plant_listview("Plant_Diamond_015") 

    @allure.description("Should able to click on unarchive plant button in plant listview and able to unarchive the plant")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_26) 
    def test_unarchived_plant(self):
        self.plant = Plant(self.driver)
        self.plant.unarchived_plant("Plant_Diamond_015")
    
    @allure.description("Should view the unarchived plant in plant list view.")
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.order(2_27)
    def test_unarchived_plant_in_list_view(self):
        self.plant = Plant(self.driver)
        self.plant.unarchived_plant_listView("Plant_Diamond_015")
    
    @allure.description("Should validate the plant count")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(2_28)
    def test_total_plant_count(self):
        self.plant = Plant(self.driver)
        self.plant.plants_listview_count()

    @allure.description("Should able to search the plant using search option")
    @allure.severity(severity_level="MEDIUM")
    @pytest.mark.order(2_29)
    def test_search_client_functionality(self):
        self.plant = Plant(self.driver)
        self.plant.search_client("Plant_Diamond_015")

