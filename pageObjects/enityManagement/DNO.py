import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class failure_reason:
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    dno_option = '//a[@href="/entity_management/dnos"]'
    add_dno_xpath = "//button[@class='btn btn-primary btn-icon']"
    
    #Add asset category popup
    input_dno_xpath = "//input[@name='name']"
    create_dno_xpath = '//button[@id="add-dno-btn"]'

    #List View
    created_dno_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'

    #edit category
    edit_dno_button_id = "edit-dno-btn"
    edit_failure_reason_xpath = "//input[@name='name']"
    save_information_button_xpath = "//button[normalize-space()='Save Information']"

    def __init__(self,driver) -> None:
        self.driver=driver
    def navigate_DNO(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.dno_option)))
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | DNO":
            assert True
        else:
            self.driver.save_screenshot("dno_Page.png")   
            assert False
    def add_DNO(self):
        self.driver.find_element(By.ID,self.add_dno_xpath).click()
        time.sleep(3)
        if self.driver.title == "Brighter App | DNO | Create":
            assert True
        else:
            self.driver.save_screenshot("create_dno_webtitle.png")   
            assert False
    #---------------------------------DNO Popup window -------------------------------------------------#
    def DNO_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.create_dno_xpath).click()
        time.sleep(2)
        if "name is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').text:
            assert True
        else:
            self.driver.save_screenshot("create_failure_reason_mandatory_fields.png")  
            assert False 
    def name(self,name):
        self.driver.find_element(By.ID,self.input_dno_xpath).send_keys(name)
    def create_DNO(self):
        self.driver.find_element(By.XPATH,self.create_dno_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_DNO_toast.png")
            assert False

    #------------------------------------------------- List View ---------------------------------------------------#
    
    def DNO_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_dno_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_DNO.png")
            assert False     
    def view_DNO(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_dno_in_listView_xpath)))
        for x in element:
            if x.text in name:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | DNO | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_DNO.png")   
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_DNO_notFound.png")
                assert False 
    
    #---------------------------------Edit DNO ------------------------------------------------#

    def edit_failure_reason_button(self):
        self.driver.find_element(By.ID,self.edit_dno_button_id).click()
        if self.driver.title == "Brighter App | DNO | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_DNO_webpage_title.png")   
                assert False
    def edit_failure_reason_mandatory_field(self):
        self.driver.find_element(By.ID,self. edit_failure_reason_xpath).clear()
        self.driver.find_element(By.XPATH,self.save_information_button_xpath).click()
        time.sleep(2)
        if "name is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').text:
            assert True
        else:
            self.driver.save_screenshot("DNO_edit_mandatory_fields.png")  
            assert False 

    def edit_name(self,name):
        self.driver.find_element(By.ID,self. edit_failure_reason_xpath).send_keys(name)
    def save_information_button(self):
        self.driver.find_element(By.ID,self.save_information_button_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_DNO_toast.png")
            assert False
    
    def list_view_edit_option(self,Model):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+Model+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if self.driver.title == "Brighter App | DNO | Edit":
                assert True
        else:
                self.driver.save_screenshot("Edit_Modal_page.png")   
                assert False
        self.save_information_button()
    def list_view_delete_option(self,Model):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+Model+'"]/following::em[@class="icon ni ni-trash"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by category"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.category_in_listView(search_term)