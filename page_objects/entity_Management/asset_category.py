import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType



class asset_category:
    entity_management_xpath = '//span[normalize-space()="Entity Management"]'
    asset_category_option = '//a[@href="/entity_management/asset-categories"]'
    add_asset_category_id = "add-category"
    
    #Add asset category popup
    input_category_id = "name-input"
    add_category_xpath = '(//button[@id="add-category"])[2]'

    #List View
    added_category_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'

    #edit category
    edit_category_button_xpath = '(//button[@id="edit-category"])[last()]'
    edit_category_id = "name-input"
    save_information_button_id = "save-category"

    def __init__(self,driver) -> None:
        self.driver=driver
    @allure.severity(allure.severity_level.NORMAL)
    def navigate_assetCategory(self):
        self.driver.find_element(By.XPATH,self.entity_management_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.asset_category_option)))
        element.click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | AssetCategory')):
                    assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="assetCategory_Page",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("assetCategory_Page.png")   
            assert False
    def add_assetCategory(self):
        self.driver.find_element(By.ID,self.add_asset_category_id).click()
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Asset Category | Create')):
                    assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="add_assetCategory_webtitle",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("add_assetCategory_webtitle.png")   
            assert False
    #---------------------------------Asset Category Popup window -------------------------------------------------#
    def assetCategory_mandatory_fields(self):
        element =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.add_category_xpath)))
        element.click()
        validation_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="name is a required field"]')
                )
            )
        if "name is a required field"== validation_message.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="asset_category_mandatory_fields",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("asset_category_mandatory_fields.png")  
            assert False 
    def Category(self,category):
        self.driver.find_element(By.ID,self.input_category_id).send_keys(category)
    def create_category(self):
        self.driver.find_element(By.XPATH,self.add_category_xpath).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
        if "Successfully Created" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="add_asset_category_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("add_asset_category_toast.png")
            assert False    
        self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Created"]/following::button[@aria-label="close"]').click()

    #------------------------------------------------- List View ---------------------------------------------------#
    
    def category_in_listView(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.added_category_in_listView_xpath)))
        for x in element:
            if x.text == name:
                assert True
            break
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="listView_category.png",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("listView_category.png")
            assert False     
    def view_category(self,name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.added_category_in_listView_xpath)))
        for x in element:
            if x.text in name:
                x.click()
                if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Asset Category | View')):
                    assert True
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name="view_category",attachment_type=AttachmentType.PNG)
                    # self.driver.save_screenshot("view_category.png")   
                    assert False
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="listView_category_notFound",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("listView_category_notFound.png")
                assert False 
    
    #---------------------------------Edit Category ------------------------------------------------#
    # def modal(self):
    #      modal_container_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]')))
    def edit_category_button(self):
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
        if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | Asset Category | Edit')):
            assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_category_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_category_page.png")   
                assert False
    def edit_category_mandatory_field(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,'//input[@id="name-input"]',
                )
            )
        )
        # element = self.driver.find_element(By.XPATH,'//input[@id="name-input"]')
        element.click()
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        element =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,self.save_information_button_id)))
        element.click()
        if "name is a required field"== self.driver.find_element(By.XPATH,'//span[normalize-space()="name is a required field"]').text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_mandatory_fields",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_mandatory_fields.png")  
            assert False 

    def edit_category(self,name):
        self.driver.find_element(By.ID,self.edit_category_id).send_keys(name)
    def save_information_button(self):
        self.driver.find_element(By.ID,self.save_information_button_id).click()
        self.msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]')))
        if "Successfully Updated" in self.msg.text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="edit_asset_category_toast",attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot("edit_asset_category_toast.png")
            assert False
        self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Updated"]/following::button[@aria-label="close"]').click()
    
    def list_view_edit_option(self,category):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+category+'"]/following::button[@id="edit-category"])[1]').click()
        if self.driver.title == "Brighter App | Asset Category | Edit":
                assert True
        else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Edit_category_page",attachment_type=AttachmentType.PNG)
                # self.driver.save_screenshot("Edit_category_page.png")   
                assert False
    def list_view_delete_option(self,category):
        self.driver.find_element(By.XPATH,'(//div[normalize-space()="'+category+'"]/following::button[@id="delete-category"])[1]').click()
        pass
    def search_functionality(self,search_term):
        self.driver.find_element(By.XPATH,'//a[@href="#search"]').click()
        keyword = self.driver.find_element(By.XPATH,'//input[@placeholder="Search by category"]')
        keyword.send_keys(search_term)
        keyword.send_keys(Keys.ENTER)
        self.category_in_listView(search_term)
