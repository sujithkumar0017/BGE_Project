import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By








class medical_centre:
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    medical_reason_option_xpath = 'href="/entity_management/medical-centres"'
    add_medical_centre_xpath = '//button[@id="plus-health-btn"]'


    #Add Medical Reason
    input_hospital_xpath = '//input[@id="name-input"]'
    input_country_code_xpath = '//div[@id="phonecode-select"]'
    input_phone_number_xpath = '//input[@id="phoneNumber-input"]'
    input_address_xpath = '//input[@id="address-input"]'
    btn_add_medical_centre_xpath = '//button[@id="add-medical"]'


    # List View
    created_medical_centre_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'


    # edit category
    edit_medical_centre_button_xpath = '(//em[@class="icon ni ni-edit"])[last()]'
    btn_save_information_xpath = "//button[normalize-space()='Save Information']"


    def __init__(self, driver) -> None:
        self.driver = driver


    def navigate_medical_centre(self):
        self.driver.find_element(By.XPATH, self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.medical_reason_option_xpath))
        )
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Medical Centre":
            assert True
        else:
            self.driver.save_screenshot("medical_reason_Page.png")
            assert False
    def add_medical_centre(self):
        self.driver.find_element(By.XPATH, self.add_medical_centre_xpath).click()
        if self.driver.title == "Brighter App | MedicalCentre | Create":
            assert True
        else:
            self.driver.save_screenshot("medical_reason_webtitle.png")
            assert False
    
    # ---------------------------------DNO Popup window -------------------------------------------------#
    def create_medical_reason_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.btn_add_medical_centre_xpath).click()
        validation_message = ["name is a required field","address is a required field","Please enter a valid number"]
        for x in validation_message:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
            if element.is_displayed():
                assert True
            else:
                self.driver.save_screenshot("create_medical_centre_mandatory_fields.png") 
                assert False


    def hospital(self, hospital):
        self.driver.find_element(By.XPATH, self.input_hospital_xpath).send_keys(hospital)
    def phone_number(self,country_code,phone_number):
        element = self.driver.find_element(By.XPATH,self.input_country_code_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH,self.input_phone_number_xpath).send_keys(phone_number) 
    def addresss(self, address):
        self.driver.find_element(By.XPATH, self.input_address_xpath).send_keys(address)
    def create_medical_centre(self):
        self.driver.find_element(By.XPATH,self.btn_add_medical_centre_xpath).click()
        self.msg=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_medical_centre_toast.png")
            assert False


        #------------------------------------List View---------------------------------------------------------#
    def medical_centre_in_listView(self,hospital):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_medical_centre_in_listView_xpath)))
        for x in element:
            if x.text == hospital:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_medical_centre.png")
            assert False    
    def view_medical_centre(self,hospital):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_medical_centre_in_listView_xpath)))
        for x in element:
            if x.text in hospital:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | Medical Centre | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_medical_centre.png")  
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_medical_centre_notFound.png")
                assert False
    #----------------------------Edit Medical Reason---------------------------------------------#
    def edit_medical_center_button(self):  
        self.driver.find_element(By.XPATH,self.edit_medical_centre_button_xpath).click()
        if self.driver.title == "Brighter App | Medical Centre | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_Manufacturer_page.png")   
                assert False 
    def edit_medical_centre_mandatory_field(self):
           phone_number = self.driver.find_element(By.XPATH,self.input_phone_number_xpath)
           hospital = self.driver.find_element(By.XPATH, self.input_hospital_xpath)
           address = self.driver.find_element(By.XPATH, self.input_address_xpath)
           actions = ActionChains(self.driver)
           actions.click(phone_number)
           actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.click(hospital).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.click(address).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.perform()
           self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
           validation_message = ["name is a required field","Please enter a valid number","email is a required field"]
           for x in validation_message:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
                if element.is_displayed():
                    assert True
                else:
                    self.driver.save_screenshot("edit_medical_centre_mandatory_fields.png")  
                    assert False
    def edit_medical_reason(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]')))
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_medical_centre_toast.png")
            assert False

    #---------------------------------------List View Edit and delete option----------------------------------------------#
    def list_view_edit_option(self,hospital):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+hospital+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if self.driver.title == "Brighter App | Medical Centre | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_medical_centre_page.png")   
                assert False
    def list_view_delete_option(self,manufacturer):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+manufacturer+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by hospital"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.manufacturer_in_listView(search_term)