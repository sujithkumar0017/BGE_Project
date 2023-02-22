import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class sla:
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    sla_option = '//a[@href="/entity_management/slas"]'
    add_sla_xpath = '//em[@class="icon ni ni-plus"]'

    #Add SLA Popup
    input_level_xpath = '//input[@name="name"]'
    input_description_xpath = '//textarea[@name="description"]'
    create_sla_xpath = '//button[normalize-space()="Add"]'

    #List View
    created_level_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'

    #Edit SLA
    btn_edit_xpath = '(//em[@class="icon ni ni-edit"])[last()]'
    btn_save_information_xpath ='//button[normalize-space()="Save Information"]'




    def __init__(self,driver) -> None:
        self.driver = driver
    def navigate_sla(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.sla_option)))
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | SLA":
            assert True
        else:
            self.driver.save_screenshot("sla_Page.png")   
            assert False
    def add_sla(self):
        self.driver.find_element(By.XPATH,self.add_sla_xpath).click()
        time.sleep(3)
        if self.driver.title == "Brighter App | SLA | Create":
            assert True
        else:
            self.driver.save_screenshot("create_sla_webpage_title.png")   
            assert False
    def sla_mandatory_field(self):
        self.driver.find_element(By.XPATH,self.create_sla_xpath).click()
        if (self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').is_displayed()) and (self.driver.find_element(By.XPATH,'//p[normalize-space()="description is a required field"]').is_displayed()):
            assert True
        else:
            self.driver.save_screenshot("create_sla_mandatory_fields.png")  
            assert False 
    def level(self,level):
        self.driver.find_element(By.XPATH,self.input_level_xpath).send_keys(level)
    def description(self,description):
        self.driver.find_element(By.XPATH,self.input_description_xpath).send_keys(description)  
    def create_sla(self):
        self.driver.find_element(By.XPATH,self.create_sla_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_sla_toast.png")
            assert False
    
    #---------------------------------------List View-------------------------------------------------------#
    def level_in_listView(self,level):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_level_in_listView_xpath)))
        for x in element:
            if x.text == level:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_level.png")
            assert False     
    def view_level(self,level):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_level_in_listView_xpath)))
        for x in element:
            if x.text in level:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | SLA | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_level.png")   
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_level_notFound.png")
                assert False 
    
    #-------------------------------------------Edit asset----------------------------------------------------#
    def edit_sla_button(self):
        self.driver.find_element(By.XPATH,self.btn_edit_xpath).click()
        time.sleep(2)
        if self.driver.title == "Brighter App | SLA | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_Sla_webpage_title.png")   
                assert False
    def edit_sla_mandatory_field(self):
        element = self.driver.find_element(By.XPATH,self.input_level_xpath)
        time.sleep(2)
        element.clear() 
        time.sleep(2)
        element2 = self.driver.find_element(By.XPATH,self.input_description_xpath)
        # element2.clear()
        actions = ActionChains(self.driver)

        # Click the text box to select it
        actions.click(element2)

        # Send the Control+A keys to select all text, followed by the Delete key to clear the text box
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()


        # Perform the actions to clear the text box
        actions.perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').is_displayed() and self.driver.find_element(By.XPATH,'//p[normalize-space()="description is a required field"]').is_displayed():
            assert True
        else:
            self.driver.save_screenshot("create_sla_mandatory_fields.png")  
            assert False 
    def edit_level(self,level):
        self.driver.find_element(By.XPATH,self.input_level_xpath).send_keys(level)
    def edit_description(self,description):
        self.driver.find_element(By.XPATH,self.input_description_xpath).send_keys(description)
    def save_information(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_DNO_toast.png")
            assert False
    def list_view_edit_option(self,level):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+level+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if self.driver.title == "Brighter App | SLA | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_SLA_page.png")   
                assert False
        self.save_information()
    def list_view_delete_option(self,Model):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+Model+'"]/following::em[@class="icon ni ni-trash"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by level"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.level_in_listView(search_term)