import time
from page_objects.entity_Management.DNO import DNO
from utilities.readProperties import ReadConfig
from page_objects.login_Module import login_Module
import unittest
import pytest
import allure




@pytest.mark.usefixtures("init_driver")
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

   @allure.description("Should navigate to Dno page")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(2)
   def test_navigate_to_DNO_Page(self):
       self.dno = DNO(self.driver)
       self.dno.navigate_DNO()

   @allure.description("Should display the DNO popup window")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(3)
   def test_add_dno(self):
       self.dno = DNO(self.driver)
       self.dno.add_DNO()

   @allure.description("Should display the validation message on the mandatory field")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(4)
   def test_mandatory_fields(self):
       self.dno = DNO(self.driver)
       self.dno.DNO_mandatory_fields()
   @allure.description("Should able to create DNO")
   @allure.severity(severity_level="CRITICAL") 
   @pytest.mark.order(5)
   def test_create_dno(self):
       self.dno = DNO(self.driver)
       self.dno.name("Dno 5")
       self.dno.create_DNO()
   @allure.description("Should display the created DNO in list view")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(6)
   def test_created_dno_in_listView(self):
       self.dno = DNO(self.driver)
       self.dno.DNO_in_listView("Dno 5")

   @allure.description("Should view the created DNO")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(7)
   def test_view_created_dno(self):
       self.dno = DNO(self.driver)
       self.dno.view_DNO("Dno 5")
   
   @allure.description("Should display the edit DNO popup window ")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(8)
   def test_edit_button_in_view_dno(self):
       self.dno = DNO(self.driver)
       self.dno.edit_dno_button()

   @allure.description("Should display the validation message on mandatory fields")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(9)
   def test_edit_mandatory_fields(self):
       self.dno = DNO(self.driver)
       self.dno.edit_dno_mandatory_field()

   @allure.description("Should able to edit and save the DNO and navigate to DNO page")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(10)
   def test_edit_dno(self):
       self.dno = DNO(self.driver)
       self.dno.edit_name("Dno 51")
       self.dno.save_information_button()

   @allure.description("Should able to edit and save the DNO in DNO list view option")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(11)
   def test_edit_option_in_listView(self):
       self.dno = DNO(self.driver)
       self.dno.list_view_edit_option("Dno 51")
       self.dno.edit_name("Dno 512")
       self.dno.save_information_button()
    
   @allure.description("Should able to search DNO using search functionality")
   @allure.severity(severity_level="CRITICAL")
   @pytest.mark.order(12)
   def test_search_option_listView(self):
       self.dno = DNO(self.driver)
       self.dno.search_functionality("Dno 512")