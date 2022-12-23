
import unittest
from TestCases.Package_Client_02.TC_Client import Test_client
#from TestCases.Package_Login_01.TC_Login_DDT import Test_002_DDT_login
from html_test_runner import HTMLTestRunner


    #To get all the test cases
#tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_002_DDT_login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_client)
masterTestSuit = unittest.TestSuite([tc2])

    #unittest.TextTestRunner(verbosity=2).run(masterTestSuit)
    # runner = HTMLTestRunner(verbosity=2, title='Test report', report_name='report',
    #                             open_in_browser=True, description="HTMLTestReport")
outfile = open("Report.html", "w")
runner = HTMLTestRunner(stream=outfile, title='Test Report')
runner.run(masterTestSuit)

#(python3 -m pytest ./Test_Suites/All_Test_Suites.py)