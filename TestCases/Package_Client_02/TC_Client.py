
import time
import pytest
import unittest
from pageObjects.client_Module import Client
from pageObjects.login_Module import login_Module
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup_class")
class Test_client(unittest.TestCase):
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_client(self):
        self.lp = login_Module(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        
    # def test_add_client(self):
        print("working1")
        self.client = Client(self.driver)
        print("working2")
        self.client.navigate_to_client_page()
        time.sleep(4)
        self.client.add_Client()
        self.client.name()
        time.sleep(5)
        self.client.phone_number()
        self.client.email()
        self.client.mobile_number()
        self.client.email_address()
        self.client.city()
        self.client.postal_code()
        self.client.website()

if __name__ =="__main__":
    unittest.main()
