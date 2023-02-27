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


class Client:
    menuitem_client_Xpath = "//a[@href='/clients']"
    # Page Contents
    text_Xpath = '//h3[@class="nk-block-title page-title"]'
    client_count = ""
    exportButton_Xpath = '//a[@id="client-export-btn"]'
    addClient_Id = "client-plus-btn"
    clientList_Xpath = '//div[@class="nk-block"]'
    pagination_Xpath = '//div[@class="card-inner"]'
    copyright = ""
    tesark = ""

    # Add Client Page
    # Page_Contents
    title_Xpath = '//h5[@class="card-title"]'
    nameField_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[1]"
    phoneNumber_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[2]"
    addressField_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[3]"
    mobileAddress_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[4]"
    emailAddress_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[5]"
    city_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[6]"
    postalCode_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[7]"
    website_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[8]"
    taskVisibility_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[9]"
    plant_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[10]"
    plantOwned_with_addPlantButton_Xpath = "//h5[text()='Plants Owned'] |/div/button[@id='client-add-plant']"  # Need to take a look
    clientOwned_with_addUserButton_Xpath = (
        "//h5[text()='Client Users'] |/span[text()=' Add User']"
    )
    createClient_Xpath = '//button[@id="client-add-plant"]'

    # add client Functionality
    addClient_input_name_Xpath = '//input[@name="name"]'
    addClient_dd_select_phone_countryCode_Id = "client-phoneCode-input"
    addClient_input_phoneNumber_Id = "client-phonenumber-input"
    addClient_input_address_Id = "client-address-input"
    addClient_dd_select_mobile_countryCode_Id = "client-mobilecode-select"
    addClient_input_mobileNumber_Id = "client-mobilenumber-input"
    addClient_input_email_Xpath = '//input[@name="email"]'
    addClient_input_city_Xpath = '//input[@name="city"]'
    addClient_input_postalcode_Xpath = '//input[@name="postalCode"]'
    addClient_input_website_Xpath = '//input[@name="website"]'
    addClient_dd_TaskVisibility_Id = "client-task-select"
    addClient_dd_TaskVisibility_Status_open_Id = "react-select-12-option-0"
    addClient_dd_TaskVisibility_Status_inProgress_Id = "react-select-12-option-1"
    addClient_dd_TaskVisibility_Status_readyForApproval_Id = "react-select-12-option-2"
    addClient_dd_TaskVisibility_Status_completed_Id = "react-select-12-option-3"
    addClient_dd_Plant_Id = "client-plant-input"

    # Plant Owned
    btn_addPlant_Xpath = (
        '//button[@class="btn btn-primary btn-md" and @id="client-add-plant"]'
    )

    # Plant Owned Page Contents
    plantOwned_title_Xpath = '//h5[text()="Plant Creation"]'
    plantOwned_plantName_isDisplayed_Xpath = (
        "(//div[contains(@class,'form-group')])[11]"
    )
    plantOwned_size_isDisplayed_Xpath = "(//div[contains(@class,'form-group')])[12]"
    plantOwned_acronym_isDisplayed_Xpath = "//label[@for='identifier']"
    plantOwned_onBoardingDate_isDisplayed_Xpath = (
        "//label[normalize-space()='On-Boarding Date']"
    )
    plantOwned_status_isDisplayed_Xpath = "//label[@for='status']"
    plantOwned_addPlant_isDisplayed_Xpath = '//button[text()="Add Plant"]'
    plantCreation_close_window_Xpath = "//em[@class='icon ni ni-cross']"

    # Plant Owned Functionality
    plantOwned_input_plantName_Id = "client-plant-name-input"
    plantOwned_input_size_Id = "client-size-input"
    plantOwned_input_acronym_Id = "client-acronym-input"
    plantOwned_input_onBoardingDate_Id = "client-onboardat"
    plantOwned_input_status_Id = "client-status-select"
    plantOwned_status_Id = "client-status-select"
    plantOwned_status_active_Id = "react-select-7-option-0"
    plantOwned_status_inactive_Id = "react-select-7-option-1"
    plantOwned_status_suspended_Id = "react-select-14-option-2"
    plantOwned_btn_addPlant_Xpath = '//button[text()="Add Plant"]'

    # -------------------------------------------------------------------------------------------------------------------------#

    # Add user
    btn_addUser_Xpath = "//span[normalize-space()='Add User']"

    # User Creation Page Contents
    userCreation_firstName_isDisplayed_Xpath = "//label[normalize-space()='First Name']"
    userCreation_lastName_isDisplayed_Xpath = "//label[normalize-space()='Last Name']"
    userCreation_email_isDisplayed_Xpath = "//label[normalize-space()='Email']"
    userCreation_password_isDisplayed_Xpath = "//label[normalize-space()='Password']"
    userCreation_addUserButton_isDisplayed_Xpath = "//button[@id='client-add-user']"
    userCraetion_close_window_xpath = "//em[@class='icon ni ni-cross']"

    # User Creation Functionality
    userCreation_input_addUser_firstName_Xpath = '//div//input[@id="firstName"]'
    userCreation_input_addUser_lastName_Xpath = '//input[@id="lastName"]'
    userCreation_input_addUser_Email_Xpath = "//input[@type='email']"
    userCreation_input_addUser_Password_Xpath = "//input[@name='password']"
    userCreation_btn_addUser_AddUser_Xpath = "//button[contains(text(),'Add User')]"

    # -----------------------------------------------------------------------------------------------------------------------#

    # Add Client
    btn_createClient_Xpath = "//button[normalize-space()='Create Client']"
    # -------------------------------------------------------------------------------------------------------------------------#

    # List View
    created_client_in_listView_xpath = (
        '//div[@class="user-name"]//span[@class="tb-lead"]'
    )

    # View Client

    btn_back_id = "client-back-btn"
    btn_delete_id = "client-del-btn"
    btn_edit_id = "client-edit-btn"
    verify_client_name = '//span[normalize-space()="Client Name"]/following-sibling::span[@class="profile-ud-value"]'
    verify_phone_number = '//span[normalize-space()="Phone Number"]/following-sibling::span[@class="profile-ud-value"]'
    verify_address = '//span[normalize-space()="Address"]/following-sibling::span[@class="profile-ud-value"]'
    verify_email = '//span[normalize-space()=" Email"]/following-sibling::span[@class="profile-ud-value"]'
    verify_mobile_number = '//span[normalize-space()="Mobile Number"]/following-sibling::span[@class="profile-ud-value"]'
    verify_city = '//span[normalize-space()="City"]/following-sibling::span[@class="profile-ud-value"]'
    verify_postal_code = '//span[normalize-space()="Postal Code"]/following-sibling::span[@class="profile-ud-value"]'
    verify_website = '//span[normalize-space()="Website"]/following-sibling::span[@class="profile-ud-value"]'
    verify_createdAt = '//span[normalize-space()="Created At"]/following-sibling::span[@class="profile-ud-value"]'
    verify_updatedAt = '//span[normalize-space()="Updated At"]/following-sibling::span[@class="profile-ud-value"]'

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_client_page(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.menuitem_client_Xpath).click()
        # wait =  WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.menuitem_client_Xpath)))
        # wait.click()
        # assert "https://bge.tkea.in/clients" in self.driver.current_url

    # def client_PageContents(self):
    #     self.driver.find_element(By.Xpath,self.text_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.exportButton_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.addClient_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.clientList_Xpath).is_displayed()
    #     self.driver.find_element(By.Xpath,self.text_Xpath).is_displayed()
    def add_Client(self):
        self.driver.find_element(By.ID, self.addClient_Id).click()
        assert "https://bge.tkea.in/client/add" in self.driver.current_url

    def add_Client_Page_Contents(self):
        pass

    def client_mandatory_field(self):
        self.driver.find_element(By.XPATH, self.btn_createClient_Xpath).click()
        assert self.driver.find_element(
            By.XPATH, '//span[normalize-space()="Name is required"]'
        ).is_displayed()

    def name(self, name):
        self.driver.find_element(By.XPATH, self.addClient_input_name_Xpath).send_keys(
            name
        )

    def phone_number(self, country_code, phone_number):
        element = self.driver.find_element(
            By.ID, self.addClient_dd_select_phone_countryCode_Id
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        # print("phone:",country_code)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.ID, self.addClient_input_phoneNumber_Id).send_keys(
            phone_number
        )

    def address(self, address):
        self.driver.find_element(By.ID, self.addClient_input_address_Id).send_keys(
            address
        )

    def mobile_number(self, country_code, mobile_number):
        element = self.driver.find_element(
            By.ID, self.addClient_dd_select_mobile_countryCode_Id
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(country_code)
        actions.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.ID, self.addClient_input_mobileNumber_Id).send_keys(
            mobile_number
        )

    def email_address(self, email):
        self.driver.find_element(By.XPATH, self.addClient_input_email_Xpath).send_keys(
            email
        )

    def city(self, city):
        self.driver.find_element(By.XPATH, self.addClient_input_city_Xpath).send_keys(
            city
        )

    def postal_code(self, postal_code):
        self.driver.find_element(
            By.XPATH, self.addClient_input_postalcode_Xpath
        ).send_keys(postal_code)

    def website(self, website):
        self.driver.find_element(
            By.XPATH, self.addClient_input_website_Xpath
        ).send_keys(website)

    def task_visibility(self, status):
        for x in status:
            self.driver.find_element(By.ID, self.addClient_dd_TaskVisibility_Id).click()
            self.driver.find_element(By.XPATH, '//div[text()="' + x + '"]').click()

    def plant(self, plant_name):
        for y in plant_name:
            self.driver.find_element(By.ID, self.addClient_dd_Plant_Id).click()
            self.driver.find_element(By.XPATH, '//div[text()="' + y + '"]').click()

        # print("title of the window",self.driver.title)
        # assert "Plant Creation" == self.driver.find_element(By.XPATH,"//h5[normalize-space()='Plant Creation']").text

    # Add Plant
    def add_plant_in_client_page(self):
        self.driver.find_element(By.XPATH, '//button[@id="client-add-plant"]').click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Plant | Create":
            assert True
        else:
            self.driver.save_screenshot("add_plant_popup.png")
            assert False

    def plant_name(self, name):
        self.driver.find_element(By.ID, self.plantOwned_input_plantName_Id).send_keys(
            name
        )

    def size(self, size):
        self.driver.find_element(By.ID, self.plantOwned_input_size_Id).send_keys(size)

    def acronym(self, acronym):
        self.driver.find_element(By.ID, self.plantOwned_input_acronym_Id).send_keys(
            acronym
        )

    def on_boardingDate(self):
        now = datetime.datetime.now()
        # tday = now.strftime("%d-%m-%Y")
        self.driver.find_element(
            By.ID, self.plantOwned_input_onBoardingDate_Id
        ).send_keys(now.strftime("%Y-%m-%d"))

    def status(self, status):
        element = self.driver.find_element(By.ID, self.plantOwned_input_status_Id)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(status)
        actions.send_keys(Keys.ENTER).perform()

    def add_plant(self):
        self.driver.find_element(By.XPATH, self.plantOwned_btn_addPlant_Xpath).click()

    def created_plant_in_list_view(self, plant_name):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '(//div[@class="nk-block border border-light"])[1]//div[contains(@class,"nk-tb-item" )][position()>1]//div[@class="nk-tb-col"][1]',
                )
            )
        )
        for x in element:
            if x.text == plant_name:
                assert True
            else:
                assert False

    def plantCreation_mandatory_fields(self):
        self.driver.find_element(By.XPATH, self.plantOwned_btn_addPlant_Xpath).click()
        validation_message = [
            "name is a required field",
            "identifier is a required field",
            "Status is Required",
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
                self.driver.save_screenshot("create_remedial_mandatory_fields.png")
                assert False

    # Add User
    def client_page_addUser(self):
        self.driver.find_element(By.XPATH, self.btn_addUser_Xpath).click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | User | Create":
            assert True
        else:
            self.driver.save_screenshot("add_user_popup.png")
            assert False

    def user_firstName(self, name):
        self.driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(name)

    def user_lastName(self, name):
        self.driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(name)

    def user_email(self, email):
        self.driver.find_element(
            By.XPATH, '(//input[@id="client-email-input"])[2]'
        ).send_keys(email)

    def user_password(self, password):
        self.driver.find_element(
            By.XPATH, '//input[@id="client-password-input"]'
        ).send_keys(password)
        if len(password) < 8:
            assert (
                "Password must be 8 characters long"
                == self.driver.find_element(
                    By.XPATH, '//span[text()="Password must be 8 characters long"]'
                ).text
            )

    def addUser(self):
        self.driver.find_element(By.XPATH, '//button[@id="client-add-user"]').click()

    def created_user_in_list_view(self, user):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '(//div[@class="nk-block border border-light"])[2]//div[contains(@class,"nk-tb-item" )][position()>1]//div[@class="nk-tb-col"][1]',
                )
            )
        )
        for x in element:
            if x.text == user:
                assert True
            else:
                self.driver.save_screenshot("created_user_listview.png")
                assert False

    def userCreation_mandatory_fields(
        self,
    ):  # need to add password as a required field.
        self.driver.find_element(
            By.XPATH, self.userCreation_btn_addUser_AddUser_Xpath
        ).click()
        validation_message = [
            "firstName is a required field",
            "lastName is a required field",
            "email is a required field",
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
                self.driver.save_screenshot("create_remedial_mandatory_fields.png")
                assert False

    def createClient(self):
        self.driver.find_element(By.XPATH, self.btn_createClient_Xpath).click()
        self.msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Client created successfully"]',
                )
            )
        )
        if "Client created successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("client.png")
            assert False

    def client_view(self, client):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_client_in_listView_xpath)
            )
        )
        for x in element:
            print(x.text)
            if x.text in client:
                x.click()
                time.sleep(2)
                title = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.TAG_NAME, "title"))
                )
                if title.get_attribute("innerHTML") == "Brighter App | Client | View":
                    assert True
                else:
                    self.driver.save_screenshot("client_view_page.png")
                    assert False
                break
            else:
                self.driver.save_screenshot("listView_client_notFound.png")
                assert False

    def created_client_in_listView(self, client):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_client_in_listView_xpath)
            )
        )
        for x in element:
            if x.text == client:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_plant.png")
            assert False

    def validation(self):
        element = self.driver.find_elements(
            By.XPATH, '//div//span[@class="profile-ud-label"]'
        ).text
        for x in element:
            print(x)

    #    --------------------------------------------Edit Client---------------------------------------------------------
    def view_edit_client_page(self):
        self.driver.find_element(By.XPATH, '//em[@class="icon ni ni-edit"]').click()
        time.sleep(2)
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Client | Edit":
            assert True
        else:
            self.driver.save_screenshot("edit_client_page.png")
            assert False

    # def cancel_button(self):
    #     self.driver.find_element(By.XPATH,'//button[normalize-space()="Cancel"]').click()
    #     if self.driver.title == "Brighter App | Client | view":
    #         assert True
    #     else:
    #         self.driver.save_screenshot("editClient_cancel_button.png")
    #         assert False

    def edit_client_mandatory_field(self):
        self.driver.find_element(By.XPATH, self.addClient_input_name_Xpath).clear()
        self.driver.find_element(
            By.XPATH, '//button[normalize-space()="Save Information"]'
        ).click()
        assert self.driver.find_element(
            By.XPATH, '//span[normalize-space()="Name is required"]'
        ).is_displayed()

    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(
            file_to_upload_path
        )

    def save_information_btn(self):
        self.driver.find_element(
            By.XPATH, '//button[normalize-space()="Save Information"]'
        ).click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Client details updated successfully"]',
                )
            )
        )
        if "Client details updated successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("update_client.png")
            assert False

    # ---------------------------------------------- List_View_three_dotted_icon-----------------------------------------------

    def edit_client_dropdown(self, client_name):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + client_name
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//a[@id="client-edit-button"]',
                )
            )
        )
        element.click()
        time.sleep(3)
        if self.driver.title == "Brighter App | Client | Edit":
            assert True
        else:
            self.driver.save_screenshot("edit_client.png")
            assert False

    def archive_user(self, client_name):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + client_name
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//a[@id="client-archive-btn"]',
                )
            )
        )
        element.click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@class="toastr-text"]//p')
            )
        )
        if "Client Archived successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("archive_client.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()

    def view_archive_client_list(self):
        self.driver.find_element(By.ID, "client-filter-btn").click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[@for="isArchived"]'))
        )
        element.click()
        self.driver.find_element(
            By.XPATH, "//button[normalize-space()='Apply']"
        ).click()

    def archived_client_listview(self, client_name):
        element = self.driver.find_elements(By.XPATH, '//div[@class="user-name"]')
        for x in element:
            if x.text == client_name:
                assert True
                break
            else:
                self.driver.save_screenshot("archive_client_list.png")
                assert False

    def unarchived_client(self, client_name):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + client_name
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//ul[@class="link-list-opt no-bdr"]//a[@id="client-unarchive-btn"]',
                )
            )
        )
        element.click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Client Unarchived successfully"]',
                )
            )
        )
        if "Client Unarchived successfully" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("unarchive_client.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()

    def unarchived_client_listView(self, client_name):
        self.driver.find_element(By.ID, "client-filter-btn").click()
        reset_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Reset Filter']")
            )
        )
        reset_btn.click()
        element = self.driver.find_elements(By.XPATH, '//div[@class="user-name"]')
        for x in element:
            if x.text == client_name:
                assert True
                break
            else:
                self.driver.save_screenshot("unarchive_client_listView.png")
                assert False

    def ticket_listview_count(self):
        count = 0
        isNextDisabled = False
        while not isNextDisabled:
            validate_status = self.driver.find_elements(
                By.XPATH, '//div[@class="user-name"]'
            )
            for x in validate_status:
                count += 1
            nxt_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='card-inner']//li[last()-2]")
                )
            )
            next_class = nxt_btn.get_attribute("class")
            if "page-item disabled" in next_class:
                isNextDisabled = True
                break
            else:
                self.driver.find_element(
                    By.XPATH, "//div[@class='card-inner']//li[last()-2]"
                ).click()
        self.driver.find_element(
            By.XPATH, "(//div[@class='card-inner']//li)[2]"
        ).click()
        element = self.driver.find_element(
            By.XPATH, '//p[contains(text(),"You have a total")]'
        ).text
        if element[20:22] == str(count):
            assert True
        else:
            self.driver.save_screenshot("Number_of_client_count.png")
            assert False

    def search_client(self, search_term):
        self.driver.find_element(By.XPATH, '//a[@href="#search"]').click()
        keyword = self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="Search by user, email and status.enter to search"]',
        )
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.created_client_in_listView(search_term)

    def create_client_with_existing_emailid(self):
        self.driver.find_element(By.XPATH, self.btn_createClient_Xpath).click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Error Client emailId already exits"]',
                )
            )
        )
        if "Error Client emailId already exits" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_client_with_existing_email.png")
            assert False
