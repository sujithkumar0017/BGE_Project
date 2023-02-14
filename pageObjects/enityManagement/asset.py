import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




class asset:
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    asset_option = '//a[@href="/entity_management/assets"]'
    add_asset_id = "add-asset"

    #Add asset popup
    input_modal_xpath = '//input[@name="model"]'
    input_rating_id = 'rating-input-assetForm'
    input_factory_barcode_id = 'factroy-input-assetForm'
    dd_category_id = 'category-select-assetForm'
    dd_manufacturer_id ='manufacture-select-assetForm'
    input_weblink_xpath = '//input[@name="weblink"]'
    input_description_id = 'description-input-assetForm'
    create_asset_id = 'add-assetForm'

    #List View
    created_asset_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'
    
    #Edit_Asset
    btn_edit_xpath = '(//em[@class="icon ni ni-edit"])[last()]'
    btn_save_information_id ='save-assetForm'

    def __init__(self,driver) -> None:
        self.driver = driver    
    def navigate_asset(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.asset_option)))
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Asset":
            assert True
        else:
            self.driver.save_screenshot("asset_Page.png")   
            assert False
    def add_asset(self):
        self.driver.find_element(By.ID,self.add_asset_id).click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Asset | Create":
            assert True
        else:
            self.driver.save_screenshot("create_Asset_webpage_title.png")   
            assert False
    def asset_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.create_asset_id).click()
        time.sleep(2)
        if "model is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="model is a required field"]').text and "assetCategory is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="assetCategory is required"]').text and  "manufacturer is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="manufacturer is required"]').text:
            assert True
        else:
            self.driver.save_screenshot("create_asset_mandatory_fields.png")  
            assert False 
    def modal(self,modal):
        self.driver.find_element(By.ID,self.input_modal_xpath).send_keys(modal)
    def rating(self,rating):
        self.driver.find_element(By.ID,self.input_rating_id).send_keys(rating)
    def factory_barcode(self,barcode):
        self.driver.find_element(By.ID,self.input_factory_barcode_id).send_keys(barcode)
    def category(self,category):
        element = self.driver.find_element(By.ID,self.dd_category_id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(category)
        actions.send_keys(Keys.ENTER).perform()
    def Manufacturer(self,manufacturer):
        element = self.driver.find_element(By.ID,self.dd_manufacturer_id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(manufacturer)
        actions.send_keys(Keys.ENTER).perform()
    def create_asset(self):
        self.driver.find_element(By.ID,self.create_asset_id).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_asset_toast.png")
            assert False
    #---------------------------------------List View-------------------------------------------------------#
    def asset_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_asset_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_asset.png")
            assert False     
    def view_asset(self,modal):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_asset_in_listView_xpath)))
        for x in element:
            if x.text in modal:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | Asset | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_asset.png")   
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_asset_notFound.png")
                assert False 

    #---------------------------------- Edit asset -----------------------------------------------------------#
    def edit_asset_button(self):
        self.driver.find_element(By.ID,self.btn_edit_xpath).click()
        if self.driver.title == "Brighter App | Asset | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_asset_webpage_title.png")   
                assert False
    def weblink(self,weblink):
        self.driver.find_element(By.XPATH,self.input_weblink_xpath).send_keys(weblink)
    def description(self,description):
        self.driver.find_element(By.ID,self.input_description_id).send_keys(description)
    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
    def save_information(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_id).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_asset_toast.png")
            assert False
