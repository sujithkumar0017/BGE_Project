import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class corrective_maintenance:
    maintenance = '//span[normalize-space()="Maintenance"]'
    menu_item_corrective_maintenance_xpath = '//span[normalize-space()="Corrective Maintenance"]'
    add_corrective_maintenance_xpath = '//button[@class="btn btn-primary btn-icon"]'
    
    #add Client Window
    task_name_xpath = '//div[@class="form-control-wrap"]//input[@name="title"]'
    priority_xpath='(//label[@class="form-label"]/following::div[@class="form-control-select"])[1]'
    sla_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[2]'
    status_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[3]'
    plant_name_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[4]'
    field_engineer_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[5]'
    assigned_to_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[6]'
    asset_category_xpath= '(//label[@class="form-label"]/following::div[@class="form-control-select"])[7]'
    resolve_date_xpath = '//input[@class="form-control date-picker react-datepicker-ignore-onclickoutside"]'
    labour_hours_xpath = '//input[@name="labourHours"]'
    description_xpath = '//textarea[@name="description"]'
    comment_xpath = '//textarea[@name="comment"]'
    parent_task_xpath = '(//label[@class="form-label"]/following::div[@class="form-control-select"])[8]'
    attachments = ""
    add_button_xpath = '//div[@class="d-flex justify-content-end col-xl-12"]/button'
    



    
    def __init__(self,driver) -> None:
       self.driver = driver 
    def navigate_to_corrective_maintenance(self):
        self.driver.find_element(By.XPATH,self.maintenance).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.menu_item_corrective_maintenance_xpath)))
        element.click()
    def add_corrective_maintenance(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.add_corrective_maintenance_xpath)))
        element.click()
    def task_name(self):
         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.task_name_xpath)))
         element.send_keys("corrective")
    def priority(self,priority):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.priority_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(priority)
        actions.send_keys(Keys.ENTER).perform()
    def sla(self,sla):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.sla_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(sla)
        actions.send_keys(Keys.ENTER).perform()
    def status(self,status):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.status_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(status)
        actions.send_keys(Keys.ENTER).perform()
    def plant_name(self,plant_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.plant_name_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(plant_name)
        actions.send_keys(Keys.ENTER).perform()
    def field_engineer(self,field_engineer):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.field_engineer_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(field_engineer)
        actions.send_keys(Keys.ENTER).perform()
    def start_date(self):
        pass
    def assigned_to(self,assigned_to):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.assigned_to_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(assigned_to)
        actions.send_keys(Keys.ENTER).perform()
    def resolved_date(self):
        pass
    def asset_category(self,asset_category):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.asset_category_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(asset_category)
        actions.send_keys(Keys.ENTER).perform()
    def labour_hours(self,labour_hours):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.labour_hours_xpath)))
        element.send_keys(labour_hours)
    def description(self,description):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.description_xpath)))
        element.send_keys(description)
    def comment(self,comment):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.comment_xpath)))
        element.send_keys(comment)
    def parent_task(self):
        pass
    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
    def add_corrective(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.add_button_xpath)))    
        element.click()
    def corrective_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.add_button_xpath).click()
        time.sleep(2)
        assert "Title is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="Title is required"]').text
        assert "Plant name is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="Plant name is required"]').text
        assert "Field Engineer is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="Field Engineer is required"]').text
        assert "Assigned To is required"== self.driver.find_element(By.XPATH,'//span[normalize-space()="Assigned To is required"]').text




    #Filter Functionality
    def filter_option(self):
        self.driver.find_element(By.XPATH,'//div[@tag="a"]').click()
    def apply_button(self):
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn-secondary").click()  
    def reset_filter_button(self):
        self.driver.find_element(By.XPATH,'//button[text()="Reset Filter"]').click()
    def filter_status(self):
        self.filter_option()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="react-select__input"]//input[@type="text"])[1]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("open")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()
        
        # sleep = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.ID,"client-next-btn")))
        isNextDisabled = False
        while not isNextDisabled:
            # element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            #   (By.XPATH, '//div[@class="user-name"]/following::span[@class="text-capitalize badge badge-danger badge-pill"]')))
            # table = element.find_element(By.XPATH, '//div[@class="user-name"]/following::span[@class="text-capitalize badge badge-danger badge-pill"]')
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]/following::span[@class="text-capitalize badge badge-danger badge-pill"]')
            for x in validate_status:
                # print(x.text)
                if x.text != "Open":
                    self.driver.save_screenshot("corrective_open_status.png")
                    break
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')  
            # print(next_class)
            if "page-item disabled" in next_class:
                isNextDisabled = True
            else:
                self.driver.find_element(By.XPATH,"//div[@class='card-inner']//li[last()-2]").click()
        self.driver.find_element(By.XPATH,"(//div[@class='card-inner']//li)[2]").click()
    def filter_assigned_engineer(self):
        self.filter_option()
        self.reset_filter_button()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="react-select__input"]//input[@type="text"])[2]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("Admin Test")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()
        isNextDisabled = False
        while not isNextDisabled:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                          (By.XPATH, '//div[@class="user-name"]/following::div[@id="corrective-assignedto"]')))
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]/following::div[@id="corrective-assignedto"]')
            for x in validate_status:
                # print(x.text)
                if x.text != "Admin Test":
                    self.driver.save_screenshot("corrective_filter_assigned_to.png")
                    assert False
                # print(x.text)
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')
            # print(next_class)  
            if "page-item disabled" in next_class:
                isNextDisabled = True
                break
            else:
                self.driver.find_element(By.XPATH,"//div[@class='card-inner']//li[last()-2]").click()
        self.driver.find_element(By.XPATH,"(//div[@class='card-inner']//li)[2]").click()
    def filter_plant_name(self):
        self.filter_option()
        self.reset_filter_button()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="react-select__input"]//input[@type="text"])[3]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("Plant_003")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()
        isNextDisabled = False
        while not isNextDisabled:
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]/following::div[@id="corrective-plant-name"]')
            for x in validate_status:
                if x.text != "Plant_003":
                    self.driver.save_screenshot("corrective_filter_plant_name.png")
                    assert False
                # print(x.text)
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')
            # print(next_class)  
            if "page-item disabled" in next_class:
                isNextDisabled = True
                break
            else:
                self.driver.find_element(By.XPATH,"//div[@class='card-inner']//li[last()-2]").click()
        self.driver.find_element(By.XPATH,"(//div[@class='card-inner']//li)[2]").click()

    def filter_start_date(self):
        self.filter_option()
        self.reset_filter_button()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//label[normalize-space()="Start Date"]/following-sibling::div[@class="react-datepicker-wrapper"]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("23/01/2023")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()
        isNextDisabled = False
        while not isNextDisabled:
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]/following::div[@id="corrective-startat"]')
            for x in validate_status:
                if x.text != "23/01/2023":
                    self.driver.save_screenshot("corrective_filter_plant_name.png")
                    assert False
                # print(x.text)
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')
            # print(next_class)  
            if "page-item disabled" in next_class:
                isNextDisabled = True
                break
            else:
                self.driver.find_element(By.XPATH,"//div[@class='card-inner']//li[last()-2]").click()
        self.driver.find_element(By.XPATH,"(//div[@class='card-inner']//li)[2]").click()


    def filter_resolved_date(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="react-datepicker-wrapper"])[2]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("09/01/2023")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()






"""
    ticket name = //div[@class="user-name"]
    status = //div[@class="user-name"]/following::span[@class="text-capitalize badge badge-danger badge-pill"]
"""