import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Client:
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
    btn_addPlant_Id = 'client-add-plant'

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
    plantOwned_input_plantName_Xpath = "(//div[contains(@class,'form-group')])[11]"
    plantOwned_input_size_Xpath = "(//div[contains(@class,'form-group')])[12]"
    plantOwned_input_acronym_id = "client-acronym-input"
    plantOwned_input_onBoardingDate_id = "client-onboardat"
    plantOwned_input_status_id = "client-status-select"
    plantOwned_status_id = "client-status-select"
    plantOwned_status_active_id = "react-select-7-option-0"
    plantOwned_status_inactive_id = "react-select-7-option-1"
    plantOwned_status_suspended_id = "react-select-14-option-2"
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
    userCreation_input_addUser_firstName_Xpath= "//input[@name='firstName']"
    userCreation_input_addUser_lastName_Xpath = "//input[@name='lastName']"
    userCreation_input_addUser_Email_Xpath = "//input[@type='email']"
    userCreation_input_addUser_Password_Xpath = "//input[@name='password']"
    userCreation_btn_addUser_AddUser_Xpath = "//button[contains(text(),'Add User')]"

    #-----------------------------------------------------------------------------------------------------------------------#

    #Add Client 
    btn_createClient_Xpath = "//button[normalize-space()='Create Client']"
    
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
    def name(self):
        self.driver.find_element(By.XPATH,self.addClient_input_name_Xpath).send_keys("TestUser_001")
    def phone_number(self):
        element = self.driver.find_element(By.ID,self.addClient_dd_select_phone_countryCode_Id)
        element2 = self.driver.find_element(By.ID,self.addClient_dd_select_phone_countryCode_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("+91")
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
        self.driver.find_element(By.ID,self.addClient_input_phoneNumber_Id).send_keys("8234747484")
    def email(self):
        self.driver.find_element(By.ID,self.addClient_input_address_Id).send_keys("Mumbai")
    def mobile_number(self):
        # self.driver.find_element(By.ID,self.addClient_dd_select_mobile_countryCode_Id).send_keys("+91")
        element = self.driver.find_element(By.ID,self.addClient_dd_select_mobile_countryCode_Id)
        element2 = self.driver.find_element(By.ID,self.addClient_dd_select_mobile_countryCode_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys("+91")
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
        self.driver.find_element(By.ID,self.addClient_input_mobileNumber_Id).send_keys("992735371")  
    def email_address(self):
        self.driver.find_element(By.XPATH,self.addClient_input_email_Xpath).send_keys("bgeclient099@yopmail.com")
    def city(self):
        self.driver.find_element(By.XPATH,self.addClient_input_city_Xpath).send_keys("Chennai")
    def postal_code(self):
        self.driver.find_element(By.XPATH,self.addClient_input_postalcode_Xpath).send_keys("098933")
    def website(self):
        self.driver.find_element(By.XPATH,self.addClient_input_website_Xpath).send_keys("www.google.com")
