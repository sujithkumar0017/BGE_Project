import time
import unittest
from TestCases.Package_maintenance.TC_corrective_maintenance import Test_Corrective
from pageObjects.corrective_maintenance import corrective_maintenance
from pageObjects.plant_module import Plant
import pytest
from pageObjects.login_Module import login_Module
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup_class")
class Test_plant(unittest.TestCase):
    # corrective = Test_Corrective()

    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    def __init__(self, driver):
        self.driver = driver
    
    @pytest.mark.order(1)
    def test_login(self):
            self.driver.get(self.url)
            self.login= login_Module(self.driver)
            self.login.email(self.useremail)
            self.login.password(self.password)
            self.login.login()

    @pytest.mark.order(2)
    def test_navigate_to_plant(self):
        self.plant = Plant(self.driver)
        self.plant.navigate_plant()

    # @pytest.mark.order(3)
    # def test_add_plant_btn(self):
    #     self.plant = Plant(self.driver)
    #     self.plant.add_plant()

    # @pytest.mark.order(4)
    # def test_create_client_mandatory_fields(self):
    #     self.plant = Plant(self.driver)
    #     self.plant.create_plant_mandatory_field()
    # @pytest.mark.order(5)
    # def test_create_client(self):
    #     self.plant = Plant(self.driver) 
    #     self.plant.plant_name("Plant_Diamond")
    #     self.plant.size("9")
    #     self.plant.acronym("XWERTY")
    #     self.plant.on_boarding_date()
    #     self.plant.client_name("client_user_03")
    #     self.plant.status("Active")
    #     self.plant.create_plant_btn()
    @pytest.mark.order(3)
    def test_created_plant_in_list_view(self):
         self.plant = Plant(self.driver)
         self.plant.plant_in_listView("test")
    @pytest.mark.order(4)
    def test_view_created_client(self):
         self.plant = Plant(self.driver)
         self.plant.view_plant("test")
    
    @pytest.mark.order(5)
    def test_corrective_tab(self):
        self.plant = Plant(self.driver)
        self.plant.corrective_maintenance_tab_in_view_plant()
        self.corrective = Test_Corrective(self.driver)
        self.corrective.test_add_corrective_maintenance() 
        time.sleep(3)
        

    