import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class failure_reason:
    entity_mamangement_xpath = '//span[normalize-space()="Entity Management"]'
    failure_reason_option = '//a[@href="/entity_management/failure-reasons"]'
    add_failure_reason_category_id = "add-faliure"
    
    #Add asset category popup
    input_name_id = "name-input"
    add_failure_reason_xpath = '//button[@id="aadd-faliure"]'

    #List View
    created_failure_reason_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'

    #edit category
    edit_failure_reason_button_id = "edit-faliure"
    edit_failure_reason_id = "name-input"
    save_information_button_id = "save-faliure"

    def __init__(self,driver) -> None:
        self.driver=driver
    def naviagate_failure_reason(self):
        self.driver.find_element(By.XPATH,self.entity_mamangement_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.failure_reason_option)))
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Failure Reason":
            assert True
        else:
            self.driver.save_screenshot("Failure_reason_Page.png")   
            assert False
    def add_failure_reason(self):
        self.driver.find_element(By.ID,self.add_failure_reason_category_id).click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Failure Reason | Create":
            assert True
        else:
            self.driver.save_screenshot("create_Failure Reason_webtitle.png")   
            assert False
    #---------------------------------Failure reason Popup window -------------------------------------------------#
    def failure_reason_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.add_failure_reason_xpath).click()
        time.sleep(2)
        if "name is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').text
            assert True
        else:
            self.driver.save_screenshot("create_failure_reason_mandatory_fields.png")  
            assert False 
    def name(self,name):
        self.driver.find_element(By.ID,self.input_name_id).send_keys(name)
    def create_failure_reason(self):
        self.driver.find_element(By.XPATH,self.add_failure_reason_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_failure_reason_toast.png")
            assert False

    #------------------------------------------------- List View ---------------------------------------------------#
    
    def failure_reason_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_failure_reason_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_failure_reason.png")
            assert False     
    def view_failure_reason(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_failure_reason_in_listView_xpath)))
        for x in element:
            if x.text in name:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | Failure Reason | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_failure_reason.png")   
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_failure_reason_notFound.png")
                assert False 
    
    #---------------------------------Edit Failure reason ------------------------------------------------#
    def edit_failure_reason_button(self):
        self.driver.find_element(By.ID,self.edit_failure_reason_button_id).click()
        if self.driver.title == "Brighter App | Failure Reason | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_Failure_reason_page.png")   
                assert False
    def edit_failure_reason_mandatory_field(self):
        self.driver.find_element(By.ID,self.edit_failure_reason_id).clear()
        self.driver.find_element(By.XPATH,self.save_information_button_id).click()
        time.sleep(2)
        if "name is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').text
            assert True
        else:
            self.driver.save_screenshot("edit_mandatory_fields.png")  
            assert False 

    def edit_name(self,name):
        self.driver.find_element(By.ID,self.edit_failure_reason_id).send_keys(name)
    def save_information_button(self):
        self.driver.find_element(By.ID,self.save_information_button_id).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_asset_category_toast.png")
            assert False
    
    def list_view_edit_option(self,category):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+category+'"]/following::button[@id="edit-faliure"])[1]').click()
        if self.driver.title == "Brighter App | Failure Reason | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_Failure_reason_page.png")   
                assert False
        self.edit_failure_reason_mandatory_field()
        self.edit_name(category)
        self.save_information_button()
    def list_view_delete_option(self,category):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+category+'"]/following::button[@id="delete-category"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by category"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.category_in_listView(search_term)