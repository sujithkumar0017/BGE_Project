import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType



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
    input_description_xpath = "//textarea[@id='description-input-assetForm']"
    create_asset_xpath = "//button[@id='add-assetForm']"

    #List View
    created_asset_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'
    
    #Edit_Asset
    btn_edit_xpath = '(//em[@class="icon ni ni-edit"])[last()]'
    btn_save_information_xpath ="//button[@id='save-assetForm']"

    def __init__(self,driver) -> None:
        self.driver = driver    
    def navigate_asset(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.asset_option)))
        element.click()

        if self.driver.title == "Brighter App | Asset":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="asset_Page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("asset_Page.png")   
            assert False
    def add_asset(self):
        self.driver.find_element(By.ID,self.add_asset_id).click()
        if self.driver.title == "Brighter App | Asset | Create":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_Asset_webpage_title",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_Asset_webpage_title.png")   
            assert False
    def asset_mandatory_fields(self):
        # button  = self.driver.find_element(By.XPATH,self.create_asset_xpath)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.create_asset_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        time.sleep(2)
        element.click()
        # .click()
        validation_message = ["model is a required field","assetCategory is required","manufacturer is required"]
        for x in validation_message:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
            if element.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="create_asset_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("create_asset_mandatory_fields.png")  
                assert False
    def modal(self,modal):
        self.driver.find_element(By.XPATH,self.input_modal_xpath).send_keys(modal)
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
        self.driver.find_element(By.XPATH,self.create_asset_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_asset_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_asset_toast.png")
            assert False
    #---------------------------------------List View-------------------------------------------------------#
    def asset_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_asset_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="listView_asset",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("listView_asset.png")
            assert False     
    def view_asset(self,modal):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_asset_in_listView_xpath)))
        for x in element:
            if x.text in modal:
                x.click()
                if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Asset | View')):
                    assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="view_asset",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("view_asset.png")   
                    assert False
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="listView_asset_notFound",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("listView_asset_notFound.png")
                assert False 

    #---------------------------------- Edit asset -----------------------------------------------------------#
    def edit_asset_button(self):
        self.driver.find_element(By.XPATH,self.btn_edit_xpath).click()
        if self.driver.title == "Brighter App | Asset | Edit":
                assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_asset_webpage_title",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_asset_webpage_title.png")   
                assert False
    def edit_asset_mandatory_field(self):
           modal = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,self.input_modal_xpath)))
        #    modal = self.driver.find_element(By.XPATH,self.input_modal_xpath)
           actions = ActionChains(self.driver)
           actions.click(modal).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.perform()
           save_information_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.btn_save_information_xpath)))
           self.driver.execute_script("arguments[0].scrollIntoView();",save_information_btn)
           time.sleep(2)
           save_information_btn.click()
        #    self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
           element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="model is a required field"]')))
           if element.is_displayed():
            assert True
           else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_asset_mandatory_fields",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_asset_mandatory_fields.png")  
            assert False
    def weblink(self,weblink):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,self.input_weblink_xpath)))
        # element = self.driver.find_element(By.XPATH,self.input_weblink_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(weblink)
        actions.perform()
    def description(self,description):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,self.input_description_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(description)
        actions.perform()
        # self.driver.find_element(By.XPATH,self.input_description_xpath).send_keys(description)
    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
        self.msg=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="File uploaded successfully"')))
        if "File uploaded successfully" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="add_followup_task",attachment_type=AttachmentType.PNG)   
            # self.driver.save_screenshot("add_followup_task.png")
            assert False
    def save_information(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]')))
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_asset_toast",attachment_type=AttachmentType.PNG) 
            # self.driver.save_screenshot("edit_asset_toast.png")
            assert False
        self.driver.find_element(By.XPATH,'//button[@aria-label="close"]').click()
#---------------------------------------List View Edit and delete option----------------------------------------------#
    def list_view_edit_option(self,modal):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+modal+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if self.driver.title == "Brighter App | Asset | Edit":
                assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_Asset_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_Asset_page.png")   
                assert False
    def list_view_delete_option(self,model):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+model+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.implicitly_wait(10)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'(//a[@id="search-asset"])[1]')))
        element.click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by model"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.asset_in_listView(search_term)    