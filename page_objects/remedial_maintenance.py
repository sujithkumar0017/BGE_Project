import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType

class remedial_maintenance:
    maintenance = '//span[normalize-space()="Maintenance"]'
    menu_item_remedial_maintenance_xpath = (
        '//span[normalize-space()="Remedial Maintenance"]'
    )
    add_remedial_maintenance_xpath = '//button[@id="add-remedial"]'

    # add Client Window
    task_name_xpath = '//input[@id="title-input-remedial"]'
    priority_xpath = '//div[@id="priority-remedial-select"]'
    status_xpath = '//div[@id="status-remedial-select"]'
    plant_name_xpath = '//div[@id="plant-remedial-select"]'
    field_engineer_xpath = '//div[@id="engineer-remedial-select"]'
    assigned_to_xpath = '//div[@id="assignedto-remedial-select"]'
    asset_category_xpath = '//div[@id="assertcategory-remedial-select"]'
    resolve_date_xpath = '//input[@id="resolved--remedial-select"]'
    description_xpath = '//textarea[@name="description"]'
    comment_xpath = '//textarea[@name="comment"]'
    parent_task_xpath = '//div[@id="parendid-remedial-select"]'
    add_button_xpath = '(//button[@id="add-remedial"])[2]'

    # List View
    created_remedial_task_in_listView_xpath = (
        '//div[@class="user-name"]//span[@class="tb-lead"]'
    )

    # Save Information Button
    btn_save_information_xpath = '//button[@id="save-remedial"]'

    def __init__(self, driver) -> None:
        self.driver = driver

    def navigate_to_remedial_maintenance(self):
        self.driver.find_element(By.XPATH, self.maintenance).click()
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.menu_item_remedial_maintenance_xpath)
            )
        )
        element.click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Remedial Maintenance":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="remedial_page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("remedial_page.png")
            assert False

    def add_remedial_maintenance(self):
        element = self.driver.find_element(
            By.XPATH, self.add_remedial_maintenance_xpath
        )
        element.click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Remedial | Create":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="add_remedial_popup",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("add_remedial_popup.png")
            assert False

    def task_name(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.task_name_xpath))
        )
        element.send_keys(name)

    def priority(self, priority):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.priority_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(priority)
        actions.send_keys(Keys.ENTER).perform()

    def status(self, status):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.status_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(status)
        actions.send_keys(Keys.ENTER).perform()

    def plant_name(self, plant_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.plant_name_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(plant_name)
        actions.send_keys(Keys.ENTER).perform()

    def field_engineer(self, field_engineer):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.field_engineer_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(field_engineer)
        actions.send_keys(Keys.ENTER).perform()

    def start_date(self):
        pass

    def assigned_to(self, assigned_to):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.assigned_to_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(assigned_to)
        actions.send_keys(Keys.ENTER).perform()

    def resolved_date(self):
        pass

    def asset_category(self, asset_category):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.asset_category_xpath))
        )
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(asset_category)
        actions.send_keys(Keys.ENTER).perform()

    def description(self, description):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.description_xpath))
        )
        element.send_keys(description)

    def comment(self, comment):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.comment_xpath))
        )
        element.send_keys(comment)

    def parent_task(self):
        pass

    def attachments(self):
        file_to_upload_path = os.getcwd() + "/Files/file.png"
        self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(
            file_to_upload_path
        )
        self.msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[text()="File uploaded successfully"',
                )
            )
        )
        if "File uploaded successfully" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="add_followup_task",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("add_followup_task.png")
            assert False

    def create_remedial_maintenance(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.add_button_xpath))
        )
        element.click()
        self.msg = WebDriverWait(self.driver, 10).until(
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
            allure.attach(self.driver.get_screenshot_as_png(),name="create_remedial",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("create_remedial.png")
            assert False

    def remedial_mandatory_fields(self):
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
                allure.attach(self.driver.get_screenshot_as_png(),name="create_remedial_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("create_remedial_mandatory_fields.png")
                assert False

    # ------------------------------------List View---------------------------------------------------------#
    def remedial_task_in_listView(self, plant):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_remedial_task_in_listView_xpath)
            )
        )
        for x in element:
            if x.text == plant:
                assert True
            break
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="listView_plant",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("listView_plant.png")
            assert False

    def view_remedial_task(self, plant):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.created_remedial_task_in_listView_xpath)
            )
        )
        for x in element:
            if x.text in plant:
                x.click()
                time.sleep(3)
                title = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.TAG_NAME, "title"))
                )
                if title.get_attribute("innerHTML") == "Brighter App | Remedial | View":
                    assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="view_plant",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("view_plant.png")
                    assert False
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="listView_plant_notFound",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("listView_plant_notFound.png")
                assert False

    def ticketView_edit_button(self):
        self.driver.find_element(By.XPATH, '//span[normalize-space()="Edit"]').click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Remedial | Edit":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Edit_remedial_ticket_page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("Edit_remedial_ticket_page.png")
            assert False

    def edit_mandatory_field(self):
        clear_mandatory_field = [
            self.task_name_xpath,
            self.assigned_to_xpath,
        ]  # need to be add : self.field_engineer_xpath,
        for validation in clear_mandatory_field:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, validation))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click(element)
            actions.key_down(Keys.CONTROL).send_keys("a").key_up(
                Keys.CONTROL
            ).send_keys(Keys.BACKSPACE)
            actions.perform()
        self.driver.find_element(By.XPATH, self.btn_save_information_xpath).click()
        validation_message = [
            "Title is required",
            "Assigned To is required",
        ]  # need to add :  "Field Engineer is required"
        for y in validation_message:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="' + y + '"]')
                )
            )
            if element.is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="edit_remedial_mandatory_fields",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("edit_remedial_mandatory_fields.png")
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
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_remedial_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_remedial_toast.png")
            assert False

    # ---------------------------------------------- List_View_three_dotted_icon-----------------------------------------------

    def edit_plant_dropdown(self, ticket):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + ticket
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//a[@id="edit-remedial"]',
                )
            )
        )
        element.click()
        title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        if title.get_attribute("innerHTML") == "Brighter App | Remedial | Edit":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_ticket",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_ticket.png")
            assert False

    def archive_ticket(self, ticket):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + ticket
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@class="dropdown show"]//ul[@class="link-list-opt no-bdr"]//a[@id="archive-remedial"]',
                )
            )
        )
        element.click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Remedial Task Archived successfully"]',
                )
            )
        )
        if "Remedial Task Archived successfully" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="archive_ticket",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("archive_ticket.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()

    def view_archive_list(self):
        self.driver.find_element(By.ID, "filter-remedial").click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[@for="isArchived"]'))
        )
        element.click()
        self.driver.find_element(
            By.XPATH, "//button[normalize-space()='Apply']"
        ).click()

    def archived_ticket_listview(self, ticket):
        element = self.driver.find_elements(By.XPATH, '//div[@class="user-name"]')
        for x in element:
            if x.text == ticket:
                assert True
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="archive_ticket_list",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("archive_ticket_list.png")
                assert False

    def unarchived_ticket(self, ticket):
        self.driver.find_element(
            By.XPATH,
            '(//div[normalize-space()="'
            + ticket
            + '"]/following::div[@class="dropdown"])[1]',
        ).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//ul[@class="link-list-opt no-bdr"]//a[@id="unarchive-remedial"]',
                )
            )
        )
        element.click()
        self.msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="toastr-text"]//p[normalize-space()="Remedial Task UnArchived successfully"]',
                )
            )
        )
        if "Remedial Task UnArchived successfully" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="unarchive_ticket",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("unarchive_ticket.png")
            assert False
        self.driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()

    def unarchived_ticket_listView(self, ticket):
        self.driver.find_element(By.ID, "filter-remedial").click()
        reset_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Reset Filter']")
            )
        )
        reset_btn.click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="user-name"]'))
        )
        for x in element:
            if x.text == ticket:
                assert True
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="unarchive_client_listView",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("unarchive_client_listView.png")
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
            allure.attach(self.driver.get_screenshot_as_png(),name="Number_of_ticket_count",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("Number_of_ticket_count.png")
            assert False

    def search_remedial_ticket(self, search_term):
        self.driver.find_element(By.XPATH, '//a[@href="#search"]').click()
        keyword = self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="Search by Ticket Name, status and Plant Name.enter to search"]',
        )
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.remedial_task_in_listView(search_term)
