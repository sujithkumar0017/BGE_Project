import datetime
import os
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from selenium.common import exceptions  
class Client():
    menuitem_client_Xpath = "//a[@href='/clients']"
    # Page Contents
    text_Xpath = '//h3[@class="nk-block-title page-title"]'
    client_count = ""
    exportButton_Xpath = '//a[@id="client-export-btn"]'
    addClient_Id = "client-plus-btn"
    clientList_Xpath ='//div[@class="nk-block"]'
    pagination_Xpath = '//div[@class="card-inner"]'
    copyright =""
    tesark=""
    
    #Add Client Page 
    #Page_Contents
    title_Xpath = '//h5[@class="card-title"]'
    nameField_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[1]"
    phoneNumber_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[2]"
    addressField_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[3]"
    mobileAddress_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[4]"
    emailAddress_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[5]"
    city_isDisplayed_Xpath ="(//div[contains(@class,'form-group')])[6]"
    postalCode_isDisplayed_Xpath ="(//div[contains(@class,'form-group')])[7]"
    website_isDisplayed_Xpath ="(//div[contains(@class,'form-group')])[8]"
    taskVisibility_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[9]"
    plant_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[10]"
    plantOwned_with_addPlantButton_Xpath = "//h5[text()='Plants Owned'] |/div/button[@id='client-add-plant']"   #Need to take a look
    clientOwned_with_addUserButton_Xpath ="//h5[text()='Client Users'] |/span[text()=' Add User']"
    createClient_Xpath ='//button[@id="client-add-plant"]'

    # add client Functionality
    addClient_input_name_Xpath = '//input[@name="name"]'
    addClient_dd_select_phone_countryCode_Id = "client-phoneCode-input"
    addClient_input_phoneNumber_Id = 'client-phonenumber-input'
    addClient_input_address_Id = 'client-address-input'
    addClient_dd_select_mobile_countryCode_Id = "client-mobilecode-select"
    addClient_input_mobileNumber_Id = "client-mobilenumber-input"
    addClient_input_email_Xpath = '//input[@name="email"]'
    addClient_input_city_Xpath = '//input[@name="city"]'
    addClient_input_postalcode_Xpath = '//input[@name="postalCode"]'
    addClient_input_website_Xpath = '//input[@name="website"]'
    addClient_dd_TaskVisibility_Id= 'client-task-select'
    addClient_dd_TaskVisibility_Status_open_Id = 'react-select-12-option-0'
    addClient_dd_TaskVisibility_Status_inProgress_Id = 'react-select-12-option-1'
    addClient_dd_TaskVisibility_Status_readyForApproval_Id = 'react-select-12-option-2'
    addClient_dd_TaskVisibility_Status_completed_Id = 'react-select-12-option-3'
    addClient_dd_Plant_Id = 'client-plant-input'

    #Plant Owned 
    btn_addPlant_Xpath = '//button[@class="btn btn-primary btn-md" and @id="client-add-plant"]'

    # Plant Owned Page Contents
    plantOwned_title_Xpath = '//h5[text()="Plant Creation"]'
    plantOwned_plantName_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[11]"
    plantOwned_size_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[12]"
    plantOwned_acronym_isDisplayed_Xpath = "//label[@for='identifier']"
    plantOwned_onBoardingDate_isDisplayed_Xpath = "//label[normalize-space()='On-Boarding Date']"
    plantOwned_status_isDisplayed_Xpath = "//label[@for='status']"
    plantOwned_addPlant_isDisplayed_Xpath ='//button[text()="Add Plant"]'
    plantCreation_close_window_Xpath = "//em[@class='icon ni ni-cross']"

    #Plant Owned Functionality
    plantOwned_input_plantName_Id = "client-plant-name-input"
    plantOwned_input_size_Id = "client-size-input"
    plantOwned_input_acronym_Id = "client-acronym-input"
    plantOwned_input_onBoardingDate_Id = "client-onboardat"
    plantOwned_input_status_Id = "client-status-select"
    plantOwned_status_Id = "client-status-select"
    plantOwned_status_active_Id = "react-select-7-option-0"
    plantOwned_status_inactive_Id = "react-select-7-option-1"
    plantOwned_status_suspended_Id = "react-select-14-option-2"
    plantOwned_btn_addPlant_Xpath ='//button[text()="Add Plant"]'
    
    
    # -------------------------------------------------------------------------------------------------------------------------#
    
    #Add user 
    btn_addUser_Xpath = "//span[normalize-space()='Add User']"

    # User Creation Page Contents
    userCreation_firstName_isDisplayed_Xpath = "//label[normalize-space()='First Name']"
    userCreation_lastName_isDisplayed_Xpath = "//label[normalize-space()='Last Name']"
    userCreation_email_isDisplayed_Xpath  = "//label[normalize-space()='Email']"
    userCreation_password_isDisplayed_Xpath = "//label[normalize-space()='Password']"
    userCreation_addUserButton_isDisplayed_Xpath = "//button[@id='client-add-user']"
    userCraetion_close_window_xpath = "//em[@class='icon ni ni-cross']"

    #User Creation Functionality
    userCreation_input_addUser_firstName_Xpath= '//div//input[@id="firstName"]'
    userCreation_input_addUser_lastName_Xpath = '//input[@id="lastName"]'
    userCreation_input_addUser_Email_Xpath = "//input[@type='email']"
    userCreation_input_addUser_Password_Xpath = "//input[@name='password']"
    userCreation_btn_addUser_AddUser_Xpath = "//button[contains(text(),'Add User')]"

    #-----------------------------------------------------------------------------------------------------------------------#

    #Add Client 
    btn_createClient_Xpath = "//button[normalize-space()='Create Client']"
    #-------------------------------------------------------------------------------------------------------------------------#
    

    #View Client

    btn_back_id = "client-back-btn"  
    btn_delete_id = "client-del-btn"
    btn_edit_id = "client-edit-btn" 
    verify_client_name= '//span[normalize-space()="Client Name"]/following-sibling::span[@class="profile-ud-value"]'
    verify_phone_number = '//span[normalize-space()="Phone Number"]/following-sibling::span[@class="profile-ud-value"]'
    verify_address = '//span[normalize-space()="Address"]/following-sibling::span[@class="profile-ud-value"]'
    verify_email = '//span[normalize-space()=" Email"]/following-sibling::span[@class="profile-ud-value"]'
    verify_mobile_number = '//span[normalize-space()="Mobile Number"]/following-sibling::span[@class="profile-ud-value"]'
    verify_city = '//span[normalize-space()="City"]/following-sibling::span[@class="profile-ud-value"]'
    verify_postal_code = '//span[normalize-space()="Postal Code"]/following-sibling::span[@class="profile-ud-value"]'
    verify_website = '//span[normalize-space()="Website"]/following-sibling::span[@class="profile-ud-value"]'
    verify_createdAt = '//span[normalize-space()="Created At"]/following-sibling::span[@class="profile-ud-value"]'
    verify_updatedAt = '//span[normalize-space()="Updated At"]/following-sibling::span[@class="profile-ud-value"]'
    

    
    
    def __init__(self,driver):
        self.driver=driver
    def navigate_to_client_page(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.menuitem_client_Xpath).click()
        # wait =  WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.menuitem_client_Xpath)))
        # wait.click()
        #assert "https://bge.tkea.in/clients" in self.driver.current_url
    # def client_PageContents(self):
    #     self.driver.find_element(By.Xpath,self.text_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.exportButton_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.addClient_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.clientList_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.text_Xpath).is_displayed()
    def add_Client(self):
        self.driver.find_element(By.ID,self.addClient_Id).click()
        assert "https://bge.tkea.in/client/add" in self.driver.current_url
    def add_Client_Page_Contents(self):
         pass
    def client_mandatory_field(self):
        self.driver.find_element(By.XPATH,self.btn_createClient_Xpath).click()
        assert self.driver.find_element(By.XPATH,'//span[normalize-space()="Name is required"]').is_displayed()
    def name(self,name):
        self.driver.find_element(By.XPATH,self.addClient_input_name_Xpath).send_keys(name)
    def phone_number(self,country_code,phone_number):
        element = self.driver.find_element(By.ID,self.addClient_dd_select_phone_countryCode_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        # print("phone:",country_code)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.ID,self.addClient_input_phoneNumber_Id).send_keys(phone_number)
    def address(self,address):
        self.driver.find_element(By.ID,self.addClient_input_address_Id).send_keys(address)
    def mobile_number(self,country_code,mobile_number):
        element = self.driver.find_element(By.ID,self.addClient_dd_select_mobile_countryCode_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        # print("mobile:",country_code)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        #  print("mobile:",mobile_number)
        self.driver.find_element(By.ID,self.addClient_input_mobileNumber_Id).send_keys(mobile_number)  
    def email_address(self,email):
        self.driver.find_element(By.XPATH,self.addClient_input_email_Xpath).send_keys(email)
    def city(self,city):
        self.driver.find_element(By.XPATH,self.addClient_input_city_Xpath).send_keys(city)
    def postal_code(self,postal_code):
        self.driver.find_element(By.XPATH,self.addClient_input_postalcode_Xpath).send_keys(postal_code)
    def website(self,website):
        self.driver.find_element(By.XPATH,self.addClient_input_website_Xpath).send_keys(website)
    def task_visibility(self,status):
        for x in status:
            self.driver.find_element(By.ID,self.addClient_dd_TaskVisibility_Id).click()
            self.driver.find_element(By.XPATH, '//div[text()="'+x+'"]').click()
    def plant(self,plant_name):
        for y in plant_name:
            self.driver.find_element(By.ID,self.addClient_dd_Plant_Id).click()
            self.driver.find_element(By.XPATH, '//div[text()="'+y+'"]').click()

        #print("title of the window",self.driver.title)
        #assert "Plant Creation" == self.driver.find_element(By.XPATH,"//h5[normalize-space()='Plant Creation']").text
    def plant_name(self,name):
        self.driver.find_element(By.ID,self.plantOwned_input_plantName_Id).send_keys(name)
    def size(self,size):
        self.driver.find_element(By.ID,self.plantOwned_input_size_Id).send_keys(size)
    def acronym(self,acronym):
        self.driver.find_element(By.ID,self.plantOwned_input_acronym_Id).send_keys(acronym)
    def on_boardingDate(self):
        now = datetime.datetime.now()
        # tday = now.strftime("%d-%m-%Y")
        self.driver.find_element(By.ID,self.plantOwned_input_onBoardingDate_Id).send_keys(now.strftime("%Y-%m-%d")) 
    def status(self,status):
        element = self.driver.find_element(By.ID,self.plantOwned_input_status_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(status)
        actions.send_keys(Keys.ENTER).perform()
    def add_plant(self,value):
        self.driver.find_element(By.XPATH,self.plantOwned_btn_addPlant_Xpath).click()
        time.sleep(3)
        self.table = self.driver.find_elements(By.XPATH,'(//div[@class="nk-block border border-light"])[1]')
        element = self.driver.find_elements(By.XPATH,'(//div[@class="nk-block border border-light"])[1]//div[contains(@class,"nk-tb-item" )][position()>1]//div[@class="nk-tb-col"][1]')
        for x in element:
           if x.text == value:
            assert True
           else:
            assert False
    def plantCreation_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.plantOwned_btn_addPlant_Xpath).click()
        time.sleep(3)
        assert  "name is a required field" == self.driver.find_element(By.XPATH,'//span[text()="name is a required field"]').text
        assert "identifier is a required field" == self.driver.find_element(By.XPATH,"//span[normalize-space()='identifier is a required field']").text
        assert "Status is Required" == self.driver.find_element(By.XPATH,"//span[normalize-space()='Status is Required']").text
    

    #Add User
    def client_addUser(self):
        self.driver.find_element(By.XPATH,self.btn_addUser_Xpath).click()
    def user_firstName(self,name):
        self.driver.find_element(By.XPATH,self.userCreation_input_addUser_firstName_Xpath).send_keys(name)
    def user_lastName(self,name):
        self.driver.find_element(By.XPATH,self.userCreation_input_addUser_lastName_Xpath).send_keys(name)
    def user_email(self,email):
        self.driver.find_element(By.XPATH,self.userCreation_input_addUser_Email_Xpath).send_keys(email)
    def user_password(self,password):
        self.driver.find_element(By.XPATH,self.userCreation_input_addUser_Password_Xpath).send_keys(password)
        if len(password)<8:
            assert  "Password must be 8 characters long" == self.driver.find_element(By.XPATH,'//span[text()="Password must be 8 characters long"]').text

    def addUser(self,value):
        self.driver.find_element(By.XPATH,self.userCreation_btn_addUser_AddUser_Xpath).click()
        time.sleep(3)
        self.table = self.driver.find_elements(By.XPATH,'(//div[@class="nk-block border border-light"])[1]')
        element = self.driver.find_elements(By.XPATH,'(//div[@class="nk-block border border-light"])[2]//div[contains(@class,"nk-tb-item" )][position()>1]//div[@class="nk-tb-col"][1]')
        for x in element:
           if x.text == value:
            assert True
           else:
            assert False
    def userCreation_mandatory_fields(self):
        self.driver.find_element(By.XPATH,self.userCreation_btn_addUser_AddUser_Xpath).click()
        time.sleep(3)
        assert  "firstName is a required field" == self.driver.find_element(By.XPATH,'//span[text()="firstName is a required field"]').text
        assert "lastName is a required field" == self.driver.find_element(By.XPATH,"//span[normalize-space()='lastName is a required field']").text
        assert "email is a required field" == self.driver.find_element(By.XPATH,"//span[normalize-space()='email is a required field']").text
        assert "password is a requirevisibility_of_element_locatedd field" == self.driver.find_element(By.XPATH,"//span[normalize-space()='password is a required field']").text
    
    def createClient(self):
        self.driver.find_element(By.XPATH,self.btn_createClient_Xpath).click()
        time.sleep(3)
        self.msg=self.driver.find_element(By.XPATH,"(//div[contains(@class,'toastr-text')])[1]").text
        if "Client created successfully" in self.msg:
            assert True
        else:
            self.driver.save_screenshot("client.png")
            assert  False  
        # time.sleep(3)
        # self.table = self.driver.find_elements(By.XPATH,'//div[@class="nk-tb-list nk-tb-ulist is-compact"]//div[@class="user-card"]')
        # for y in self.table:
        #     if y.text == client_name:
        #      assert True
        #     else:
        #      assert Falsevisibility_of_element_located
    # def list_view(self,name):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]')))
    #     for x in element:
    #         # print(x)
    #         if x.text in name:
    #             # x.click()
    #             time.sleep(5)
    #             WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]')))
    #             time.sleep(3)
    #         else: edit_client
    #            assert False


    def search_client(self,name):
        self.driver.find_element(By.ID,'client-search')
        keyword = self.driver.find_element(By.ID,'client-search-input')
        keyword.send_keys(name)
        keyword.send_keys(Keys.ENTER)
        

    def client_view(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="user-card"]//span[@class="tb-lead"]')))
        for x in element:
            if x.text in name:
                # print("element",self.driver.execute_script('return document.getElementsByClassName("title")[0].innerText'))
                try:
                    x.click()
                    self.driver.implicitly_wait(10)
                    self.driver.set_page_load_timeout(30)
                    # time.sleep(5)
                    # self.driver.refresh()
                    time.sleep(3)
                    element2 = self.driver.execute_script('return document.getElementsByClassName("title")[0].innerText')
                    print(element2)
                    # print("name",name)
                    if name in element2:
                       assert True
                    else:
                        assert False
                    break
                except exceptions.StaleElementReferenceException as e:  # ignore this error
                    print("exception", e)          
    def validation(self):
        element = self.driver.find_elements(By.XPATH,'//div//span[@class="profile-ud-label"]').text
        for x in element:
            print(x)
   




#    --------------------------------------------Edit Client---------------------------------------------------------
    def view_edit_client_page(self):
        self.driver.find_element(By.XPATH,'//em[@class="icon ni ni-edit"]').click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Client | Edit":
            assert True
        else:
            self.driver.save_screenshot("edit_client.png")   
            assert False
    # def cancel_button(self):
    #     self.driver.find_element(By.XPATH,'//button[normalize-space()="Cancel"]').click()
    #     if self.driver.title == "Brighter App | Client | view":
    #         assert True
    #     else:
    #         self.driver.save_screenshot("editClient_cancel_button.png")
    #         assert False

    def mandatory_field(self):
        self.driver.find_element(By.XPATH,self.addClient_input_name_Xpath).clear()
        self.driver.find_element(By.XPATH,'//button[normalize-space()="Save Information"]').click()
        assert self.driver.find_element(By.XPATH,'//span[normalize-space()="Name is required"]').is_displayed()
    def edit_client(self,name):
        self.name(name)
        self.driver.find_element(By.XPATH,self.addClient_input_postalcode_Xpath).clear()
        self.driver.find_element(By.XPATH,self.addClient_input_city_Xpath).clear()
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_to_upload_path)
        self.driver.find_element(By.XPATH,'//button[normalize-space()="Save Information"]').click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p')))
        time.sleep(3)
        if "Client details updated successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("update_client.png")
            assert  False
    
    # ---------------------------------------------- List_View_three_dotted_icon-----------------------------------------------

    def edit_client_dropdown(self,client_name):
        self.driver.find_element(By.XPATH,'//div[normalize-space()="'+client_name+'"]/following::a[@id="client-menu-btn"]').click()
        element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//a[@id="client-edit-button"]')))
        element.click()
        self.view_edit_client_page()
        self.mandatory_field()
        self.edit_client()        
"""      
   

    Column:
    (//div[@class="nk-block border border-light"])[1]//div[@class="nk-tb-col"]

    rows:
    (//div[@class="nk-block border border-light"])[1]//div[@class="nk-tb-item"]

    rows:
    (//div[@class="nk-block border border-light"])[1]//div[contains(@class,"nk-tb-item" )][position()>1]

    Row - first column
    (//div[@class="nk-block border border-light"])[1]//div[contains(@class,"nk-tb-item" )][position()>1]//div[@class="nk-tb-col"][1]
    
"""
# //span[normalize-space()="Client Name"]/following::span[normalize-space()="Dr. Christopher Shaw"]