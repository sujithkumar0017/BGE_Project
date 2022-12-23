import time
from selenium.webdriver.common.by import By


class login_Module:
    #Page Contents
    Logo_Xpath="//img[@alt='logo-dark']"
    Login_card_Xpath = "//div[@class='card-preview card-bordered card']"
    Card_Header_Xpath = "//h4[normalize-space()='Login']"
    input_email_Xpath = '//input[@name="email"]'
    input_password_Xpath = '//input[@name="password"]'
    link_Forget_Password = '//a[@href="/auth-forgot-password"]'
    btn_Login_Xpath = '//button[contains(text(),"Login")]'
    link_TermsConditions_Xpath = "//a[contains(text(),'Terms & Condition')]"
    link_PrivacyPolicy_Xpath = "//a[normalize-space()='Privacy Policy']"
    link_Help_Xpath = "//a[contains(text(),'Help')]"
    copyright_Xpath ="//p[contains(text(),' © Brighter Green Engineering ')]"
    
    def __init__(self, driver):
        self.driver = driver
    def Page_Contents(self):
        self.driver.find_element(By.XPATH,self.Logo_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.Login_card_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.Card_Header_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.input_email_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.input_password_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.link_Forget_Password).is_displayed() 
        self.driver.find_element(By.XPATH,self.btn_Login_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.link_TermsConditions_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.link_PrivacyPolicy_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.link_Help_Xpath).is_displayed() 
        self.driver.find_element(By.XPATH,self.copyright_Xpath).is_displayed() 

    def email(self, email):
        self.driver.find_element(By.XPATH, self.input_email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_Xpath).send_keys(email)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_Xpath).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.btn_Login_Xpath).click()
   
    def signOut(self):
        self.driver.find_element(By.XPATH,"//div[@class='user-name dropdown-indicator']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Sign Out']").click()
    
    def termsConditions_Link(self):
            self.driver.refresh()
            parent_handle=self.driver.current_window_handle 
            self.driver.find_element(By.XPATH,self.link_TermsConditions_Xpath).click()
            child_handle=self.driver.window_handles
            for child in child_handle:
                if parent_handle!= child:
                    self.driver.switch_to.window(child)
                    if self.driver.current_url == "https://brightergreenengineering.com/wp-content/uploads/2019/08/Terms-and-Conditions-1.pdf":
                       assert True
                       time.sleep(3)
                       self.driver.close()
                       self.driver.switch_to.window(parent_handle)
                    else:
                        assert False

    def privacyPolicy_Link(self):
        parent_handle=self.driver.current_window_handle 
        self.driver.find_element(By.XPATH,self.link_PrivacyPolicy_Xpath).click()
        child_handle=self.driver.window_handles
        for child in child_handle:
                if parent_handle!= child:
                    self.driver.switch_to.window(child)
                    if self.driver.current_url == "https://brightergreenengineering.com/wp-content/uploads/2019/08/Privacy-Policy.pdf":
                       assert True
                       time.sleep(3)
                       self.driver.close()
                       self.driver.switch_to.window(parent_handle)
                    else:
                        assert False
    def help_Link(self):
        parent_handle=self.driver.current_window_handle 
        self.driver.find_element(By.XPATH,self.link_Help_Xpath).click()
        child_handle=self.driver.window_handles
        for child in child_handle:
                if parent_handle!= child:
                    self.driver.switch_to.window(child)
                    if self.driver.current_url == "https://brightergreenengineering.com/CONTACT/":
                       assert True
                       time.sleep(3)
                       self.driver.close()
                       self.driver.switch_to.window(parent_handle)
                    else:
                        assert False