import time
from pageObjects.enityManagement.DNO import DNO
from utilities.readProperties import ReadConfig
from pageObjects.login_Module import login_Module
import unittest
import pytest




@pytest.mark.usefixtures("setup_class")
class Test_DNO(unittest.TestCase):
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
   def test_navigate_entity_management(self):
       self.dno = DNO(self.driver)
       self.dno.navigate_DNO()


   @pytest.mark.order(3)
   def test_add_dno(self):
       self.dno = DNO(self.driver)
       self.dno.add_DNO()


   @pytest.mark.order(4)
   def test_mandatory_fields(self):
       self.dno = DNO(self.driver)
       self.dno.DNO_mandatory_fields()


   @pytest.mark.order(5)
   def test_create_dno(self):
       self.dno = DNO(self.driver)
       self.dno.name("Dno 5")
       self.dno.create_DNO()


   @pytest.mark.order(6)
   def test_created_dno_in_listView(self):
       self.dno = DNO(self.driver)
       self.dno.DNO_in_listView("Dno 5")


   @pytest.mark.order(7)
   def test_view_created_dno(self):
       self.dno = DNO(self.driver)
       self.dno.view_DNO("Dno 5")


   @pytest.mark.order(8)
   def test_edit_button_in_view_dno(self):
       self.dno = DNO(self.driver)
       self.dno.edit_dno_button()


   @pytest.mark.order(9)
   def test_edit_mandatory_fields(self):
       self.dno = DNO(self.driver)
       self.dno.edit_dno_mandatory_field()


   @pytest.mark.order(10)
   def test_edit_dno(self):
       self.dno = DNO(self.driver)
       self.dno.edit_name("Dno 51")
       self.dno.save_information_button()


   @pytest.mark.order(11)
   def test_edit_option_in_listView(self):
       self.dno = DNO(self.driver)
       self.dno.list_view_edit_option("Dno 51")
       self.dno.edit_name("Dno 512")
       self.dno.save_information_button()


   @pytest.mark.order(12)
   def test_search_option_listView(self):
       self.dno = DNO(self.driver)
       self.dno.search_functionality("Dno 512")