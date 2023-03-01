import datetime
import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Plant:
    menuitem_plant_xpath = '//a[@href="/pv-plants"]'

    # Add Plant
    add_plant_xpath = '//button[@id="add-pvplant-btn"]'

    # Create Plant
    plant_name_xpath = '//div[@id="plant-name-input"]//div[@class="form-control-wrap"]'
    size_xpath = '//div[@id="plant-size-input"]//div[@class="form-control-wrap"]'
    acronym_xpath = (
        '//div[@id="plant-identifier-input"]//div[@class="form-control-wrap"]'
    )
    on_boarding_date_xpath = (
        '//div[@id="plant-onBoardDate-input"]//div[@class="form-control-wrap"]'
    )
    client_name_xpath = (
        '//div[@id="plant-clientName-select"]//div[@class="form-control-wrap"]'
    )
    plant_manager_xpath = (
        '//div[@id="plant-manager-select"]//div[@class="form-control-wrap"]'
    )
    team_leader_xpath = (
        '//div[@id="plant-team-select"]//div[@class="form-control-wrap"]'
    )
    field_engineer_xpath = (
        '//div[@id="plant-engineer-select"]//div[@class="form-control-wrap"]'
    )
    status_xpath = '//div[@id="plant-status-select"]//div[@class="form-control-select"]'
    postal_code_xpath = (
        '//div[@id="plant-postal-input"]//div[@class="form-control-wrap"]'
    )
    address_xpath = '//div[@id="plant-address-input"]//div[@class="form-control-wrap"]'
    google_map_link_xpath = (
        '//div[@id="plant-map-input"]//div[@class="form-control-wrap"]'
    )
    what3word_link_xpath = (
        '//div[@id="plant-what3word-input"]//div[@class="form-control-wrap"]'
    )
    dno_xpath = '//div[@id="plant-dno-select"]//div[@class="form-control-wrap "]'
    hospital_xpath = (
        '//div[@id="plant-hospital-select"]//div[@class="form-control-wrap"]'
    )
    btn_cancel_xpath = '//button[@id="cancel-plant"]'
    btn_create_plant_xpath = '//button[@id="create-plant-form"]'

    # list view
    created_plant_in_listView_xpath = (
        '//div[@class="user-name"]//span[@class="tb-lead"]'
    )

    def __init__(self, driver) -> None:
        self.driver = driver

    def navigate_plant(self):
        self.driver.find_element(By.XPATH, self.menuitem_plant_xpath).click()
        time.sleep(2)
        if self.driver.title == "Brighter App | PV-Plant":
            assert True
        else:
            self.driver.save_screenshot("Pv_plant_Page.png")
            assert False

    def add_plant(self):
        self.driver.find_element(By.XPATH, self.add_plant_xpath).click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Pv-Plant | Create":
            assert True
        else:
            self.driver.save_screenshot("add_plant_popup.png")
            assert False

    def create_plant_mandatory_field(self):
        self.driver.find_element(By.XPATH, self.btn_create_plant_xpath).click()
        validation_message = [
            "Name is required",
            "Identifier is required",
            "Client is required",
            "status is a required field",
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
                self.driver.save_screenshot("create_plant_mandatory_fields.png")
                assert False

    def plant_name(self, name):
        self.driver.find_element(By.XPATH, self.plant_name_xpath).send_keys(name)

    def size(self, size):
        self.driver.find_element(By.XPATH, self.size_xpath).send_keys(size)

    def acronym(self, acronym):
        self.driver.find_element(By.XPATH, self.acronym_xpath).send_keys(acronym)

    def on_boarding_date(self):
        now = datetime.datetime.now()
        element = self.driver.find_element(By.XPATH, self.on_boarding_date_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(now.strftime("%Y-%m-%d"))
        actions.send_keys(Keys.ENTER).perform()

    def client_name(self, client):
        element = self.driver.find_element(By.XPATH, self.client_name_xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(client)

    def plant_manager(self, manager):
        self.driver.find_element(By.XPATH, self.plant_manager_xpath).send_keys(manager)

    def team_leader(self, leader):
        self.driver.find_element(By.XPATH, self.team_leader_xpath).send_keys(leader)

    def field_engineer(self, engineer):
        self.driver.find_element(By.XPATH, self.team_leader_xpath).send_keys(engineer)

    def status(self, status):
        self.driver.find_element(By.XPATH, self.status_xpath).send_keys(status)

    def postal_code(self, code):
        self.driver.find_element(By.XPATH, self.postal_code_xpath).send_keys(code)

    def address(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def google_map_link(self, link):
        self.driver.find_element(By.XPATH, self.google_map_link_xpath).send_keys(link)

    def what3word_link(self, link):
        self.driver.find_element(By.XPATH, self.what3word_link_xpath).send_keys(link)

    def dno(self, dno):
        self.driver.find_element(By.XPATH, self.dno_xpath).send_keys(dno)

    def hospital(self, hospital):
        self.driver.find_element(By.XPATH, self.hospital_xpath).send_keys(hospital)

    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(
            file_to_upload_path
        )

    def create_plant_btn(self):
        self.driver.find_element(By.XPATH, self.btn_create_plant_xpath).click()
        self.msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]',
                )
            )
        )
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("create_plant_toast.png")
            assert False

    def cancel_btn(self):
        self.driver.find_element(By.XPATH, self.btn_cancel_xpath).click()
        time.sleep(2)
        if self.driver.title == "Brighter App | PV-Plant":
            assert True
        else:
            self.driver.save_screenshot("cancel_plant_creation.png")

    # ------------------------------------List View---------------------------------------------------------#
    def plant_in_listView(self, plant):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_plant_in_listView_xpath)
            )
        )
        for x in element:
            if x.text == plant:
                assert True
            break
        else:
            self.driver.save_screenshot("listView_plant.png")
            assert False

    def view_plant(self, plant):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_plant_in_listView_xpath)
            )
        )
        for x in element:
            if x.text == plant:
                x.click()
                time.sleep(3)
                if self.driver.title == "Brighter App | Pv-Plant | View":
                    assert True
                else:
                    self.driver.save_screenshot("view_plant.png")
                    assert False
                break
        else:
            self.driver.save_screenshot("listView_plant_notFound.png")
            assert False

    # ------------------------------------------------Edit Plant-------------------------------------------#
    def edit_button_view_plant(self):
        self.driver.find_element(By.XPATH, '//a[@id="edit-Plants-btn"]').click()
        time.sleep(2)
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Pv-Plant | Edit":
            assert True
        else:
            self.driver.save_screenshot("edit_plant_page.png")
            assert False

    def save_information(self):
        self.driver.find_element(By.XPATH, self.btn_save_information_xpath).click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]',
                )
            )
        )
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            self.driver.save_screenshot("edit_plant_toast.png")
            assert False

    # --------------------------------------------------------Corrective Ticket--------------------------------------------------------#
    def corrective_maintenance_tab_in_view_plant(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[@id="corrective-Plants-btn"]')
            )
        )
        element.click()

    def validate_plant_name_in_create_corrective_ticket(self, plant_name):
        element = self.driver.find_element(
            By.XPATH,
            "(//div[contains(@class,'react-select__control react-select__control--is-disabled css-1fhf3k1-control')])[4]",
        )
        #    value = element.get_attribute("value")

        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        if element.text == plant_name:
            assert True
        else:
            self.driver.save_screenshot("Plant_name_in_create_remedial.png")
            assert False

    # --------------------------------------------------------Remedial Ticket--------------------------------------------------------#
    def remedial_maintenance_tab_in_view_plant(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[@id="remedial-Plants-btn"]')
            )
        )
        element.click()

    def validation_message(self):
        pass

    def validate_plant_name_in_create_remedial_ticket(self, plant_name):
        element = self.driver.find_element(
            By.XPATH,
            "(//div[contains(@class,'react-select__control react-select__control--is-disabled css-1fhf3k1-control')])[4]",
        )
        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        if element.text == plant_name:
            assert True
        else:
            self.driver.save_screenshot("Plant_name_in_create_remedial.png")
            assert False
