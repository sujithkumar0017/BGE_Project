import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions  


class corrective_maintenance:
    maintenance = '//span[normalize-space()="Maintenance"]'
    menu_item_corrective_maintenance_xpath = '//span[normalize-space()="Corrective Maintenance"]'
    add_corrective_maintenance_xpath = '//button[@class="btn btn-primary btn-icon"]'
    
    #add Corrective Window
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
    
    #add_follow-up_task
    followup_task_name_xpath = "//div[@id='subtask-task-name-input']//input[@name='title']"
    followup_priority_xpath = "//div[@id='subtask-priority-select']//div[@class='form-control-select']"
    followup_Sla_xpath = "//div[@id='subtask-sla-select']//div[@class='form-control-select']"
    followup_status_xpath = "//div[@id='subtask-status-select']//div[@class='form-control-select']"
    followup_field_engineer_xpath = "//div[@id='subtask-field-engineer-select']//div//div[contains(@class,'form-control-select')]"
    followup_assigned_to_xpath = "//div[@id='subtask-assignto-select']//div[contains(@class,'form-control-select')]"
    followup_resolved_date_xpath = "//div[@id='subtask-resolve-select']//div[contains(@class,'form-control-wrap')]"
    followup_asset_category_xpath = "//div[@id='subtask-assetcategory-select']//div[contains(@class,'form-control-select')]"
    followup_labour_hours_xpath = "//div[@id='subtask-labour-input']//input[contains(@name,'labourHours')]"
    followup_description_xpath = "//div[@id='subtask-labour-input']//input[contains(@name,'labourHours')]"
    followup_comment_xpath = "//div[@id='subtask-comment-input']//textarea[contains(@name,'comment')]"
    followup_parent_task_xpath = "//div[@id='subtask-parenttask-select']//div[contains(@class,'form-control-select')]"



    
    def __init__(self,driver) -> None:
       self.driver = driver 
    def navigate_to_corrective_maintenance(self):
        self.driver.find_element(By.XPATH,self.maintenance).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.menu_item_corrective_maintenance_xpath)))
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Corrective Maintenance":
            assert True
        else:
            self.driver.save_screenshot("add_corrective_window.png")   
            assert False
    def add_corrective_maintenance(self):
        element = self.driver.find_element(By.XPATH,'//em[@class="icon ni ni-plus"]')
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Corrective | Create":
            assert True
        else:
            self.driver.save_screenshot("add_corrective_window.png")   
            assert False
    def task_name(self,name):
         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.task_name_xpath)))
         element.send_keys(name)
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
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("add_corrective.png")
            assert False
    def corrective_mandatory_fields(self):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()
        validation_message = [
            "Title is required",
            "Plant name is required",
            "Field Engineer is required",
            "Assigned To is required",
        ]
        for x in validation_message:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="' + x + '"]')
                )
            )
            if element.is_displayed():
                assert True
            else:
                self.driver.save_screenshot("create_corrective_mandatory_fields.png")
                assert False

    #-----------------------List View---------------------------------------------#
    def corrective_ticket_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-name"]//span[@class="tb-lead"]')))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_ticket_view.png")
            assert False     
    def search_corrective_ticket(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by Ticket Name, status and Plant Name.enter to search"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.corrective_ticket_listView(search_term)
    #------------------------ Ticket View --------------------------------#
    def view_ticket(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-name"]//span[@class="tb-lead"]')))
        for x in element:
            if x.text in name:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | Corrective | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_corrective_ticket.png")   
                    assert False
                break
        else:
            self.driver.save_screenshot("select_corrective_ticket.png")
            assert False 
    #---------------------------View-Edit Ticket-------------------------------#           
    def ticketView_edit_button(self):
        self.driver.find_element(By.XPATH,'//span[normalize-space()="Edit"]').click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Corrective | Edit":
            assert True
        else:
            self.driver.save_screenshot("Edit_corrective_ticket_page.png")   
            assert False
    def edit_ticket(self,sla,labour_hours):
        self.sla(sla)
        self.labour_hours(labour_hours)
    
#-----------------------------------Add Follow-up Task-----------------------------------------#
    
    def add_addFollow_up_task(self):
        self.driver.execute_script("window.scrollBy(0, -500);")
        self.driver.find_element(By.XPATH,'//span[normalize-space()="Add Follow-up Task"]').click() 
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
    def create_addfollowup_task_mandatory_fields(self):
        self.driver.find_element(By.XPATH,'//button[normalize-space()="Add"]').click()     
        validation_message = [
            "Title is required",
            "Field Engineer is required",
            "Assigned To is required",
        ]
        for x in validation_message:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="' + x + '"]')
                )
            )
            if element.is_displayed():
                assert True
            else:
                self.driver.save_screenshot("create_followup_task_fields.png")
                assert False
    def followup_task_name(self,name):
         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_task_name_xpath)))
         element.send_keys(name)
    def followup_priority(self,priority):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_priority_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(priority)
        actions.send_keys(Keys.ENTER).perform()
    def followup_sla(self,sla):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_Sla_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(sla)
        actions.send_keys(Keys.ENTER).perform()
    def followup_status(self,status):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_status_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(status)
        actions.send_keys(Keys.ENTER).perform()
    def followup_plant_name(self,plant_name):
       element= self.driver.find_element(By.XPATH,"(//div[contains(@class,'react-select__control react-select__control--is-disabled css-1fhf3k1-control')])[1]")
       actions = ActionChains(self.driver)
       actions.double_click(element)
       actions.key_down(Keys.CONTROL).send_keys("a").key_up(
                Keys.CONTROL
            ).perform()
       if element.text == plant_name:
           assert True
       else:
           self.driver.save_screenshot("Plant_name_in_create_remedial.png")
           assert False
    def followup_field_engineer(self,field_engineer):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_field_engineer_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(field_engineer)
        actions.send_keys(Keys.ENTER).perform()
    def followup_start_date(self):
        pass
    def followup_assigned_to(self,assigned_to):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_assigned_to_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(assigned_to)
        actions.send_keys(Keys.ENTER).perform()
    def followup_resolved_date(self):
        pass
    def followup_asset_category(self,asset_category):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_asset_category_xpath)))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(asset_category)
        actions.send_keys(Keys.ENTER).perform()
    def followup_labour_hours(self,labour_hours):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_labour_hours_xpath)))
        element.send_keys(labour_hours)
    def followup_description(self,description):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_description_xpath)))
        element.send_keys(description)
    def followup_comment(self,comment):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.followup_comment_xpath)))
        element.send_keys(comment)
    def followup_parent_task(self,plant_name):
        element= self.driver.find_element(By.XPATH,"(//div[contains(@class,'react-select__control react-select__control--is-disabled css-1fhf3k1-control')])[2]")
        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(
                Keys.CONTROL
            ).perform()
        if element.text in plant_name:
           assert True
        else:
           self.driver.save_screenshot("Plant_name_in_create_remedial.png")
           assert False
    def followup_attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        button=self.driver.find_element(By.XPATH,'//div[@id="subtask-parenttask-select"]/following::div//span[@class="dz-message-text"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[text()="File uploaded successfully"')))
        if "File uploaded successfully" in self.msg.text:
            assert True
        else:   
            self.driver.save_screenshot("add_followup_task.png")
            assert False
        
    def create_add_followup_task_button(self):
        button = self.driver.find_element(By.XPATH,'//button[normalize-space()="Add"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[text()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("add_followup_task.png")
            assert False
    
    def followup_task_listview(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-card dropdown-toggle"]')))
        for x in element:
            if x.text in name:
                assert True
            break
        else:
                self.driver.save_screenshot("followup_ticket_view.png")
                assert False 
    def followup_ticket_visible_in_corrective_list_view(self,name):
        # self.driver.find_element(By.XPATH,'//button[@class="close"]').click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-name"]//span[@class="tb-lead"]')))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_ticket_view.png")
            assert False
    def save_information_button(self):
        self.driver.find_element(By.XPATH,'//button[@id="save-correctiveForm"]').click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[text()="Successfully Updated"]')))
        time.sleep(3)
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_corrective_ticket.png")
            assert False
    
    

    # ----------------------Archive and Unarchive ticket -----------------------------#
    def archive_ticket(self,corrective_ticket):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+corrective_ticket+'"]/following::div[@class="dropdown"])[1]').click() 
        element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//span[normalize-space()="Archive Task"]')))
        element.click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Corrective Task Archived successfully"]')))
        if "Corrective Task Archived successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("archive_corrective_ticket.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()
    def view_archive_ticket_list(self):
            self.driver.find_element(By.XPATH,'//em[@class="icon ni ni-filter-alt"]').click()
            element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[@for="isArchived"]'))
        )
            element.click()
            self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
    def view_archived_ticket_in_list_view(self,corrective_ticket):
        element = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]') 
        for x in element:
            if x.text == corrective_ticket:
                assert True
                break
            else:
                self.driver.save_screenshot("archive_corrective_ticket_list.png")
                assert False   
    def unarchived_ticket(self,client_name):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+client_name+'"]/following::div[@class="dropdown"])[1]').click() 
        element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'(//ul[@class="link-list-opt no-bdr"]//span[normalize-space()="UnArchive Task"])[1]')))
        element.click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[text()="Corrective Task UnArchived successfully"]')))
        if "Corrective Task UnArchived successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("unarchive_corrective_ticket.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()
    def unarchived_ticket_listView(self,corrective_ticket):
        self.driver.find_element(By.XPATH,'//em[@class="icon ni ni-filter-alt"]').click()
        reset_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Reset Filter']")
            )
        )
        reset_btn.click()
        element = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]') 
        for x in element:
            if x.text == corrective_ticket:
                assert True
                break
            else:
                self.driver.save_screenshot("unarchive_corrective_ticket_listView.png")
                assert False 

    def ticket_listview_count(self):
        count =0
        isNextDisabled = False
        while not isNextDisabled:
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]')
            for x in validate_status:
                count+=1
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')  
            if "page-item disabled" in next_class:
                isNextDisabled = True
                break
            else:
                self.driver.find_element(By.XPATH,"//div[@class='card-inner']//li[last()-2]").click()
        self.driver.find_element(By.XPATH,"(//div[@class='card-inner']//li)[2]").click()
        element = self.driver.find_element(By.XPATH,'//p[contains(text(),"You have a total")]').text
        if element[20:22] == str(count):
            assert True
        else:
            self.driver.save_screenshot("Number_of_client_count.png")
            assert False






















    
    
    
    
    #-----------------------Filter Functionality-----------------------------------#
    def filter_option(self):
        self.driver.find_element(By.XPATH,'//div[@tag="a"]').click()
    def apply_button(self):
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn-secondary").click()  
    def reset_filter_button(self):
        self.driver.find_element(By.XPATH,'//button[text()="Reset Filter"]').click()
    def filter_status(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="react-select__input"]//input[@type="text"])[1]')))
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("open")
        actions.send_keys(Keys.ENTER).perform()
        self.apply_button()
        isNextDisabled = False
        while not isNextDisabled:
            validate_status = self.driver.find_elements(By.XPATH,'//div[@class="user-name"]/following::span[@class="text-capitalize badge badge-danger badge-pill"]')
            for x in validate_status:
                
                if x.text != "Open":
                    self.driver.save_screenshot("corrective_open_status.png")
                    break
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')  
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
                if x.text != "Admin Test":
                    self.driver.save_screenshot("corrective_filter_assigned_to.png")
                    assert False
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')  
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
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class') 
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
            
            nxt_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='card-inner']//li[last()-2]")))
            next_class = nxt_btn.get_attribute('class')
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