
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType



class DNO:
   entity_management_xpath = '//span[normalize-space()="Entity Management"]'
   dno_option = '//a[@href="/entity_management/dnos"]'
   add_dno_xpath = '//em[@class="icon ni ni-plus"]'


   # Add asset category popup
   input_dno_xpath = "//input[@name='name']"
   create_dno_xpath = '//button[@id="add-dno-btn"]'


   # List View
   created_dno_in_listView_xpath = '//div[@class="user-name"]//span[@class="tb-lead"]'


   # edit category
   edit_dno_button_xpath = '(//em[@class="icon ni ni-edit"])[last()]'
   edit_dno_xpath = "//input[@name='name']"
   save_information_button_xpath = "//button[normalize-space()='Save Information']"


   def __init__(self, driver) -> None:
       self.driver = driver


   def navigate_DNO(self):
       self.driver.find_element(By.XPATH, self.entity_management_xpath).click()
       element = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, self.dno_option))
       )
       element.click()
       if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | DNO')):
            assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="dno_Page",attachment_type=AttachmentType.PNG) 
        #    self.driver.save_screenshot("dno_Page.png")
           assert False


   def add_DNO(self):
       self.driver.find_element(By.XPATH, self.add_dno_xpath).click()
       if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | DNO | Create')):
            assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="create_dno_webtitle",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("create_dno_webtitle.png")
           assert False


   # ---------------------------------DNO Popup window -------------------------------------------------#
   def DNO_mandatory_fields(self):
       self.driver.find_element(By.XPATH, self.create_dno_xpath).click()
       validation_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="name is a required field"]')
                )
            )
       if "name is a required field"== validation_message.text:
            assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="create_failure_reason_mandatory_fields",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("create_failure_reason_mandatory_fields.png")
           assert False


   def name(self, dno):
       self.driver.find_element(By.XPATH, self.input_dno_xpath).send_keys(dno)


   def create_DNO(self):
       self.driver.find_element(By.XPATH, self.create_dno_xpath).click()
       self.msg = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//div[@class="toastr-text"]//p[normalize-space()="Successfully Created"]'))
       )
       if "Successfully Created" in self.msg.text:
           assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="create_DNO_toast",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("create_DNO_toast.png")
           assert False
       self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Created"]/following::button[@aria-label="close"]').click()


   # ------------------------------------------------- List View ---------------------------------------------------#


   def DNO_in_listView(self, dno):
       element = WebDriverWait(self.driver, 10).until(
           EC.presence_of_all_elements_located(
               (By.XPATH, self.created_dno_in_listView_xpath)
           )
       )
       for x in element:
           if x.text == dno:
               assert True
           break
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="listView_DNO",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("listView_DNO.png")
           assert False


   def view_DNO(self, dno):
       element = WebDriverWait(self.driver, 10).until(
           EC.presence_of_all_elements_located(
               (By.XPATH, self.created_dno_in_listView_xpath)
           )
       )
       for x in element:
           if x.text in dno:
               x.click()
               if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | DNO | View')):
                    assert True
               else:
                   allure.attach(self.driver.get_screenshot_as_png(),name="view_DNO",attachment_type=AttachmentType.PNG)
                #    self.driver.save_screenshot("view_DNO.png")
                   assert False
               break
           else:
               allure.attach(self.driver.get_screenshot_as_png(),name="listView_DNO_notFound",attachment_type=AttachmentType.PNG)
            #    self.driver.save_screenshot("listView_DNO_notFound.png")
               assert False


   # ---------------------------------Edit DNO ------------------------------------------------#


   def edit_dno_button(self):
       element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,'//div[@class="modal-body"]//button//em',
                )
            )
        )
       edit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,'//div[@class="modal-body"]//button//em',
                )
            )
        )
       edit_button.click()
       if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | DNO | Edit')):
                    assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="Edit_DNO_webpage_title",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("Edit_DNO_webpage_title.png")
           assert False


   def edit_dno_mandatory_field(self):
       element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,'//input[@name="name"]',
                )
            )
        )
    #    element = self.driver.find_element(By.XPATH, '//input[@name="name"]')
       actions = ActionChains(self.driver)
       actions.click(element)
       actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
       element = WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located(
               (By.XPATH, self.save_information_button_xpath)
           )
       )
       element.click()
       validation_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[normalize-space()="name is a required field"]')
                )
            )
       if "name is a required field"== validation_message.text:
            assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="DNO_edit_mandatory_fields",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("DNO_edit_mandatory_fields.png")
           assert False


   def edit_name(self, dno):
       self.driver.find_element(By.XPATH, self.edit_dno_xpath).send_keys(dno)


   def save_information_button(self):
       self.driver.find_element(By.XPATH, self.save_information_button_xpath).click()
       self.msg = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//div[@class="toastr-text"]//p[normalize-space()="Successfully Updated"]'))
       )
       if "Successfully Updated" in self.msg.text:
           assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="edit_DNO_toast",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("edit_DNO_toast.png")
           assert False
       self.driver.find_element(By.XPATH, '//p[normalize-space()="Successfully Updated"]/following::button[@aria-label="close"]').click()

   def list_view_edit_option(self, Model):
       self.driver.find_element(
           By.XPATH,
           '(//span[normalize-space()="'
           + Model
           + '"]/following::em[@class="icon ni ni-edit"])[1]',
       ).click()
       if WebDriverWait(self.driver, 50).until(
                    EC.title_contains('Brighter App | DNO | Edit')):
            assert True
       else:
           allure.attach(self.driver.get_screenshot_as_png(),name="Edit_Modal_page",attachment_type=AttachmentType.PNG)
        #    self.driver.save_screenshot("Edit_Modal_page.png")
           assert False
       self.edit_dno_mandatory_field()


   def list_view_delete_option(self, Model):
       self.driver.find_element(
           By.XPATH,
           '(//span[normalize-space()="'
           + Model
           + '"]/following::em[@class="icon ni ni-trash"])[1]',
       ).click()
       pass


   def search_functionality(self, search_term):
       self.driver.find_element(By.XPATH, '//a[@href="#search"]').click()
       keyword = self.driver.find_element(
           By.XPATH, '//input[@placeholder="Search by Dno"]'
       )
       keyword.send_keys(search_term)
       keyword.send_keys(Keys.ENTER)
       self.DNO_in_listView(search_term)