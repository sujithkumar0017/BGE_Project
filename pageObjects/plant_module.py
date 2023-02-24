import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




class Plant:
   menuitem_plant_xpath = '//a[@href="/pv-plants"]'




   #Add Plant
   add_plant_xpath = '//button[@id="add-pvplant-btn"]'


   #Create Plant
   plant_name_xpath = '//input[@name="name"]'
   size_xpath = '//input[@name="size"]'
   acronym_xpath = '//input[@name="identifier"]'
   on_boarding_date = '//input[@class="form-control date-picker"]'
   client_name_xpath = '//input[@name="clientId"]'
   plant_manager_xpath = '//input[@name="plantManagerId"]'
   team_leader_xpath = '//input[@name="teamLeaderId"]'
   field_engineer_xpath = '//input[@id="react-select-9-input"]'
   status_xpath = '//input[@id="react-select-10-input"]'
   postal_code_xpath = '//input[@name="postalCode"]'
   address_xpath = '//input[@name="address"]'
   google_map_link_xpath = '//input[@name="googleMapLink"]'
   what3word_link_xpath = '//input[@name="what3WordLink"]'
   dno_xpath = '//input[@id="react-select-11-input"]'
   hospital_xpath = '//input[@id="react-select-12-input"]'
   btn_cancel_xpath = '//button[normalize-space()="Cancel"]'
   btn_create_plant_xpath = '//button[normalize-space()="Create Plant"]'
  


   def __init__(self, driver) -> None:
       self.driver = driver




   def navigate_plant(self):
       self.driver.find_element(By.XPATH, self.menuitem_plant_xpath).click()
       time.sleep(2)
       if self.driver.title == "Brighter App | PV-Plant":
           assert True
       else:
           self.driver.save_screenshot("Pv_plant_Page.png")
           assert False
   def add_plant(self):
       self.driver.find_element(By.XPATH,self.add_plant_xpath).click()
       time.sleep(2)
       if self.driver.title == "Brighter App | PV-Plant | Create":
           assert True
       else:
           self.driver.save_screenshot("Pv_plant_Page.png")
           assert False
   def create_plant_mandatory_field(self):
       self.driver.find_element(By.XPATH,self.btn_create_plant_xpath).click()
       validation_message = ["name is a required field","Identifier is required","Client is required","status is a required field"]
       for x in validation_message:
           element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
           if element.is_displayed():
               assert True
           else:
               self.driver.save_screenshot("create_plant_mandatory_fields.png")
               assert False
   def plant_name(self,name):
       self.driver.find_element(By.XPATH,self.plant_name_xpath).send_keys(name)
   def size(self,size):
       self.driver.find_element(By.XPATH,self.size_xpath).send_keys(size)
   def acronym(self,acronym):
       self.driver.find_element(By.XPATH,self.acronym_xpath).send_keys(acronym)
   def on_boarding_date(self,date):
       pass
   def client_name(self,client):
       self.driver.find_element(By.XPATH,self.client_name_xpath).send_keys(client)
   def plant_manager(self,manager):
       self.driver.find_element(By.XPATH,self.plant_manager_xpath).send_keys(manager)
   def team_leader(self,leader):
       self.driver.find_element(By.XPATH,self.team_leader_xpath).send_keys(leader)
   def field_engineer(self,engineer):
       self.driver.find_element(By.XPATH,self.team_leader_xpath).send_keys(engineer)
   def status(self,status):
       self.driver.find_element(By.XPATH,self.status_xpath).send_keys(status)
   def postal_code(self,code):
       self.driver.find_element(By.XPATH,self.postal_code_xpath).send_keys(code)
   def address(self,address):
       self.driver.find_element(By.XPATH,self.address_xpath).send_keys(address)
   def google_map_link(self,link):
       self.driver.find_element(By.XPATH,self.google_map_link_xpath).send_keys(link)
   def what3word_link(self,link):
       self.driver.find_element(By.XPATH,self.what3word_link_xpath).send_keys(link)
   def dno(self,dno):
       self.driver.find_element(By.XPATH,self.dno_xpath).send_keys(dno)
   def hospital(self,hospital):
       self.driver.find_element(By.XPATH,self.hospital_xpath).send_keys(hospital)
   def attachments(self):
       file_to_upload_path = os.getcwd() + "/Files/file.png"
       self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
   def create_plant_btn(self):
       self.driver.find_element(By.XPATH,self.btn_create_plant_xpath).click()
       self.msg=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
       if "Successfully Created" in self.msg.text:
           assert True
       else:
           self.driver.save_screenshot("create_plant_toast.png")
           assert False
   def cancel_btn(self):
       self.driver.find_element(By.XPATH,self.btn_cancel_xpath).click()
       time.sleep(2)
       if self.driver.title == "Brighter App | PV-Plant":
           assert True
       else:
           self.driver.save_screenshot("cancel_plant_creation.png")


#------------------------------------List View---------------------------------------------------------#
   def plant_in_listView(self,plant):
       element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_plant_in_listView_xpath)))
       for x in element:
           if x.text == plant:
               assert True
           break
       else:
           self.driver.save_screenshot("listView_plant.png")
           assert False   
   def view_plant(self,plant):
       element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_plant_in_listView_xpath)))
       for x in element:
           if x.text in plant:
               x.click()
               time.sleep(3)
               if self.driver.title == "Brighter App | Pv-Plant | View":
                   assert True
               else:
                   self.driver.save_screenshot("view_plant.png") 
                   assert False
               break
           else:
               self.driver.save_screenshot("listView_plant_notFound.png")
               assert False
