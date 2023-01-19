import time
from pageObjects.corrective_maintenance import corrective_maintenance
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest


@pytest.mark.usefixtures("setup_class")
class Test_Corrective(unittest.TestCase):
    # url = ReadConfig.getApplicationUrl()
    # useremail = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()

    def test_login(self):
        self.driver.get("https://bge.tkea.in/")
        self.lp = login_Module(self.driver)
        self.lp.email("bge02@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
    def test_zdd_corrective_maintenance(self):
        self.corrective = corrective_maintenance(self.driver)
        self.corrective.navigate_to_corrective_maintenance()
        time.sleep(3)
        self.corrective.add_corrective_maintenance()
        self.corrective.corrective_mandatory_fields()
        self.corrective.task_name()
        self.corrective.priority("high")
        self.corrective.sla("TestName4")
        self.corrective.status("open")
        self.corrective.plant_name("Watch Plant")
        self.corrective.field_engineer("Admin Test")
        self.corrective.assigned_to("test 10")
        self.corrective.asset_category("CCTV")
        self.corrective.labour_hours("5")
        self.corrective.description("This is created for testing purpose")
        self.corrective.comment("This comment is for testing purpose")
        