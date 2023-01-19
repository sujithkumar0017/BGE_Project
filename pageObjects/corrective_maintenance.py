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
    def startdate(self):
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
    def description(self,descripition):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.description_xpath)))
        element.send_keys(descripition)
    def comment(self,comment):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.comment_xpath)))
        element.send_keys(comment)
    def parent_task(self):
        pass
    def attachments(self):
        pass
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
    def 