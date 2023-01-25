
import unittest
from TestCases.Package_Client_02.TC_Client import Test_client
# from TestCases.Package_corrective_maintenance.TC_corrective_maintenance import Test_Corrective
#from TestCases.Package_Login_01.TC_Login_DDT import Test_002_DDT_login
from html_test_runner import HTMLTestRunner


    #To get all the test cases
#tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_002_DDT_login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_client)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)
masterTestSuit = unittest.TestSuite([tc2])

    #unittest.TextTestRunner(verbosity=2).run(masterTestSuit)
    # runner = HTMLTestRunner(verbosity=2, title='Test report', report_name='report',
    #                             open_in_browser=True, description="HTMLTestReport")
outfile = open("Report.html", "w")
runner = HTMLTestRunner(stream=outfile, title='Test Report')
runner.run(masterTestSuit)

#(python3 -m pytest -v -s  ./Test_Suites/All_Test_Suites.py --browser chrome --html=Reports/report.html)