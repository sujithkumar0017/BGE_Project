import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType

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
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | SLA')):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="sla_Page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("sla_Page.png")   
            assert False
    def add_sla(self):
        self.driver.find_element(By.XPATH,self.add_sla_xpath).click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | SLA | Create')):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_sla_webpage_title",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_sla_webpage_title.png")   
            assert False
    def sla_mandatory_field(self):
        self.driver.find_element(By.XPATH,self.create_sla_xpath).click()
        validation_message = ["name is a required field","description is a required field"]
        for x in validation_message:
            print(x)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
            print(element.text)
            if element.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="create_Sla_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("create_manufacturer_mandatory_fields.png")  
                assert False
        # if (self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').is_displayed()) and (self.driver.find_element(By.XPATH,'//p[normalize-space()="description is a required field"]').is_displayed()):
        #     assert True
        # else:
        #     allure.attach(self.driver.get_screenshot_as_png(),name="create_sla_mandatory_fields",attachment_type=AttachmentType.PNG)
        #     # self.driver.save_screenshot("create_sla_mandatory_fields.png")  
        #     assert False 
    def level(self,level):
        self.driver.find_element(By.XPATH,self.input_level_xpath).send_keys(level)
    def description(self,description):
        self.driver.find_element(By.XPATH,self.input_description_xpath).send_keys(description)  
    def create_sla(self):
        self.driver.find_element(By.XPATH,self.create_sla_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_sla_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_sla_toast.png")
            assert False
    
    #---------------------------------------List View-------------------------------------------------------#
    def level_in_listView(self,level):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_level_in_listView_xpath)))
        for x in element:
            if x.text == level:
                assert True
            break
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="listView_level",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("listView_level.png")
            assert False     
    def view_level(self,level):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_level_in_listView_xpath)))
        for x in element:
            if x.text in level:
                x.click()
                if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | SLA | View')):
                    assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="view_level",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("view_level.png")   
                    assert False
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="listView_level_notFound",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("listView_level_notFound.png")
                assert False 
    
    #-------------------------------------------Edit asset----------------------------------------------------#
    def edit_sla_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,'//div[@class="modal-body"]//button//em',
                )
            )
        )
        edit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,'//div[@class="modal-body"]//button//em',
                )
            )
        )
        edit_button.click()
        # self.driver.find_element(By.XPATH,self.btn_edit_xpath).click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | SLA | Edit')):
                    assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_Sla_webpage_title",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_Sla_webpage_title.png")   
                assert False
        
    def edit_sla_mandatory_field(self):
        clear_mandatory_field = [
            self.input_level_xpath,
            self.input_description_xpath,
        ]  # need to be add : self.field_engineer_xpath,
        for validation in clear_mandatory_field:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, validation))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click(element)
            actions.key_down(Keys.CONTROL).send_keys("a").key_up(
                Keys.CONTROL
            ).send_keys(Keys.BACKSPACE)
            actions.perform()
        self.driver.find_element(By.XPATH, self.btn_save_information_xpath).click()
        validation_message = [
            "name is a required field",
            "description is a required field",
        ]  
        for y in validation_message:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="' + y + '"]')
                )
            )
            if element.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="edit_remedial_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("edit_remedial_mandatory_fields.png")
                assert False
    def edit_level(self,level):
        self.driver.find_element(By.XPATH,self.input_level_xpath).send_keys(level)
    def edit_description(self,description):
        self.driver.find_element(By.XPATH,self.input_description_xpath).send_keys(description)
    def save_information(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]')))
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_DNO_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_DNO_toast.png")
            assert False
    def list_view_edit_option(self,level):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+level+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | SLA | Edit')):
                    assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_SLA_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_SLA_page.png")   
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