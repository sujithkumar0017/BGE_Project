import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType







class manufacturer():
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    manufacturer_option = '//a[@href="/entity_management/manufacturers"]'
    add_manufacturer_xpath = '//button[@id="add-manufacture"]'

    #Add Manufacturer Popup
    input_name_xpath = '//input[@id="name-input"]'
    input_address_xpath = '//input[@id="register-input"]'
    input_country_code_xpath = '//div[@id="phone-select"]'
    input_phone_number_xpath = '//input[@id="phoneNumber-input"]'
    input_email_xpath = '//input[@id="email-input"]'
    input_website_xpath = '//input[@id="text-input"]'
    btn_create_manufacturer_xpath = '//button[@id="ads-manufacture"]'


    #List View
    created_manufacturer_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'

    #Edit Manufacturer 
    btn_edit_manufacturer_xpath = '//button[@id="edit-manufacture"]'
    btn_save_information_xpath = '//button[@id="save-manufacture"]'


    def __init__(self,driver) -> None:
        self.driver=driver
    def navigate_manufacturer(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.manufacturer_option)))
        element.click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Manufacturer')):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Manufacturer_Page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("Manufacturer_Page.png")   
            assert False
    def add_manufacturer(self):
        self.driver.find_element(By.XPATH,self.add_manufacturer_xpath).click()
       
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Manufacturer | Create')):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_manufacturer_webtitle",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_manufacturer_webtitle.png")   
            assert False
    def manufacturer_mandatory_field(self):
        self.driver.find_element(By.XPATH,self.btn_create_manufacturer_xpath).click()
        validation_message = ["name is a required field","address is a required field","Please enter a valid number","email is a required field"]
        for x in validation_message:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
            if element.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="create_manufacturer_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("create_manufacturer_mandatory_fields.png")  
                assert False
    def corporate_brand_name(self,name):
        self.driver.find_element(By.XPATH,self.input_name_xpath).send_keys(name)
    def address(self,address):
        self.driver.find_element(By.XPATH,self.input_address_xpath).send_keys(address)
    def phone_number(self,country_code,phone_number):
        element = self.driver.find_element(By.XPATH,self.input_country_code_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH,self.input_phone_number_xpath).send_keys(phone_number)  
    def email(self,email):
        self.driver.find_element(By.XPATH,self.input_email_xpath).send_keys(email)
    def create_manufacturer(self):
        self.driver.find_element(By.XPATH,self.btn_create_manufacturer_xpath).click()
        self.msg=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="create_DNO_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_DNO_toast.png")
            assert False 
        self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Created"]/following::button[@aria-label="close"]').click()
    
    #------------------------------------List View---------------------------------------------------------#
    def manufacturer_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_manufacturer_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="listView_manufacturer",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("listView_manufacturer.png")
            assert False     
    def view_manufacturer(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.created_manufacturer_in_listView_xpath)))
        for x in element:
            if x.text in name:
                x.click()
                if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Manufacturer | View')):
                        assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="view_manufacturer",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("view_manufacturer.png")   
                    assert False
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="listView_manufacturer_notFound",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("listView_manufacturer_notFound.png")
                assert False 
    
    #----------------------------Edit Manufacturer---------------------------------------------#
    def edit_manufacturer_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,'//div[@class="modal-body"]',
                )
            )
        )
        edit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,'//div[@class="modal-body"]//button',
                )
            )
        )
        edit_button.click()
        # self.driver.find_element(By.XPATH,self.btn_edit_manufacturer_xpath).click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Manufacturer | Edit')):
                assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_Manufacturer_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_Manufacturer_page.png")   
                assert False
    def edit_manufacturer_mandatory_field(self):
           phone_number = self.driver.find_element(By.XPATH,self.input_phone_number_xpath)
           email =self.driver.find_element(By.XPATH,self.input_email_xpath)
           actions = ActionChains(self.driver)
           actions.click(phone_number)
           actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.click(email).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
           actions.perform()
           self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
           validation_message = ["Please enter a valid number","email is a required field"]
           for x in validation_message:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//span[normalize-space()="'+x+'"]')))
                if element.is_displayed():
                    assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="edit_manufacturer_mandatory_fields",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("edit_manufacturer_mandatory_fields.png")  
                    assert False
    def edit_manufacturer(self):
        self.driver.find_element(By.XPATH,self.btn_save_information_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]')))
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_manufacturer_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_manufacturer_toast.png")
            assert False
        self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Updated"]/following::button[@aria-label="close"]').click()
    def list_view_edit_option(self,manufacturer):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+manufacturer+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Manufacturer | Edit')):
                assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_Modal_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_Modal_page.png")   
                assert False
    def website(self,website):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,'self.input_website_xpath')))
        element = self.driver.find_element(By.XPATH,self.input_website_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(website).perform()
    
    def list_view_delete_option(self,manufacturer):
        self.driver.find_element(By.XPATH,'(//span[normalize-space()="'+manufacturer+'"]/following::em[@class="icon ni ni-edit"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by corporation brand name"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.manufacturer_in_listView(search_term)
    