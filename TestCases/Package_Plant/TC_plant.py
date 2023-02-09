import unittest
import pytest
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup_class")
class Test_plant(unittest.TestCase):
    url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
