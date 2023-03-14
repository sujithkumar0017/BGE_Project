# import unittest
# # from TestCases.Package_Plant.TC_plant import Test_plant
# # from TestCases.Package_entity_management.TC_asset_category import Test_Asset_Category
# # from TestCases.Package_Login_01.TC_Login import Test_login 
# # from TestCases.Package_Client_02.TC_Client import Test_client
# from TestCases.Package_Client_02.TC_Client import Test_client 
# # from TestCases.Package_maintenance.TC_corrective_maintenance import Test_Corrective
# # from TestCases.Package_Client_02.TC_Client import Test_client
# # from TestCases.Package_Plant.TC_plant import Test_plant

# # from TestCases.Package_entity_management.TC_SLA import Test_SLA
# # from TestCases.Package_entity_management.TC_asset import Test_Asset
# # from TestCases.Package_entity_management.TC_medical_centre import Test_Medical_Centre
# # from TestCases.Package_maintenance.TC_remedial_maintenance import Test_Remedial
# # from TestCases.Package_entity_management.TC_manufacturer import Test_Manufacturer

# # from TestCases.Package_entity_management.TC_asset_category import Test_Asset_Category
# # from TestCases.Package_entity_management.TC_failure_reason import Test_Failure_Reason
# # from TestCases.Package_Login_01.TC_Login_DDT import Test_002_DDT_login
# # from html_test_runner import HTMLTestRunner


# # To get all the test cases
# tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_client)
# # tc2 = unittest.TestLoader().loadTestsFromModule(Test_Corrective)
# # tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)
# # masterTestSuit = unittest.TestSuite([tc3])
# # tc4 = unittest.TestLoader().loadTestsFromTestCase(test_login)
# masterTestSuit = unittest.TestSuite([tc1])
# unittest.TextTestRunner(verbosity=2).run(masterTestSuit)
# runner = HTMLTestRunner(verbosity=2, title='Test report', report_name='report',
#                             open_in_browser=True, description="HTMLTestReport")
# outfile = open("Report.html", "w")
# runner = HTMLTestRunner(stream=outfile, title="Test Report")
# runner.run(masterTestSuit)

# (python3 -m pytest -v -s  ./Test_Suites/All_Test_Suites.py --browser chrome --html=Reports/report.html)

#allure reports
# python3 -m pytest -v -s  --alluredir="/home/sujith/codebase/BGE_Framework_Design/Reports" ./Test_Suites/All_Test_Suites.py --browser chrome

#allure system path reports 
#  export PATH=$PATH:~/Downloads/allure-2.21.0/bin

# import unittest
# from TestCases.Package_Client_02.TC_Client import Test_client 
# # # from TestCases.Package_Client_02.TC_Client import suite_client
# from TestCases.Package_maintenance.TC_corrective_maintenance import Test_Corrective
# # from TestCases.Package_maintenance.TC_corrective_maintenance import suite_corrective_maintenance

# all_suites = unittest.TestSuite()
# all_suites.addTest(unittest.makeSuite(Test_client))
# # all_suites.addTests(unittest.makeSuite(Test_Corrective))
# result1 = unittest.TestResult()
# all_suites.run(result1)

# if result1.wasSuccessful():
#         all_suites.addTest(unittest.makeSuite(Test_Correimport pytest
# import os
# print(os.getcwd())

# def run_test_cases_from_file(filename):
#     """Runs all the test cases in the specified file"""
#     pytest.main(["-q", filename])

# def run_all_test_cases():
#     """Runs all test cases in both files in sequence"""
#     run_test_cases_from_file("/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02/TC_Client.py")  # contains 30 test cases
#     # run_test_cases_from_file("TestCases/Package_maintenance/TC_corrective_maintenance.py")  # contains 20 test cases

# if __name__=='__main__':
#     run_all_test_cases()))

# if __name__ == '__main__':
#     unittest.TextTestRunner().run(all_suites)
    # client_suite = unittest.TestSuite()
    # client_suite.addTest(unittest.makeSuite(Test_Corrective))
    # unittest.TextTestRunner().run(client_suite)

# if __name__ == '__main__':
#     # Create a test suite for TestFile1 test cases
#     suite_file1 = unittest.TestLoader().loadTestsFromTestCase(Test_client)

#     # Run TestFile1 test cases
#     unittest.TextTestRunner(verbosity=2).run(suite_file1)

#     # Create a test suite for TestFile2 test cases
#     suite_file2 = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)

#     # Run TestFile2 test cases if TestFile1 test cases are successful
#     if not suite_file1.failures and not suite_file1.errors:
#         unittest.TextTestRunner(verbosity=2).run(suite_file2)


# if __name__ == '__main__':
#     # Create a test suite with both TestFile1 and TestFile2 test cases
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(Test_client))
#     # suite.addTest(unittest.makeSuite(Test_Corrective))

#     # Run the test suite with both TestFile1 and TestFile2 test cases
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
# import unittest
# from TestCases.Package_Client_02.test_client import suite_client
# from TestCases.Package_maintenance.test_corrective_maintenance import suite_corrective_maintenance

# suite = unittest.TestSuite()
# suite.addTest(suite_client)
# suite.addTest(suite_corrective_maintenance)
# print(type(suite_client))

# print(type(suite_corrective_maintenance))
# print(suite_client.countTestCases())
# print(suite_corrective_maintenance.countTestCases())

# if __name__ == '__main__':
#     unittest.TextTestRunner().run(suite)
#     unittest.TextTestRunner().run(suite_corrective_maintenance)
# from TestCases.Package_Client_02.TC_Client import Test_client 
# import unittest

# status = False
# if status == True:
#     from TestCases.Package_maintenance.TC_corrective_maintenance import Test_Corrective

# def test_client_suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(Test_client))
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
#     status = True
#     print(status)

#     # status = True
#     return True

# test_client_suite()

# if __name__ == '__main__':
#     if status == True:
#         print("SSSSSSSSSSSSSSSSSS")
    #  suite = unittest.TestSuite()
    #  suite.addTest(unittest.makeSuite(Test_Corrective))
    #  runner = unittest.TextTestRunner(verbosity=2)
    #  runner.run(suite)

    # Create a test suite with both TestFile1 and TestFile2 test cases
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(Test_client))



# import pytest

# def run_test_cases_from_file(filename):
#import unittest
# from TestCases.Package_Client_02.TC_Client import Test_client 
# print(type(Test_client))     """Runs all the test cases in the specified file"""
#     pytest.main(["-q", filename])

# def run_all_test_cases():
#     """Runs all test cases in both files in sequence"""
#     run_test_cases_from_file("TestCases/Package_Client_02/TC_Client.py")  # contains 30 test cases
#     # run_test_cases_from_file("TestCases/Package_maintenance/TC_corrective_maintenance.py")  # contains 20 test cases

# if __name__=='__main__':
#     run_all_test_cases()
# import unittest
# from TestCases.Package_Client_02.TC_Client import Test_client 
# print(type(Test_client))
# from TestCases.Package_maintenance.TC_corrective_maintenance import Test_Corrective
# # To get all the test cases
# tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_client)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)
# # tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Corrective)
# # masterTestSuit = unittest.TestSuite([tc3])
# # tc4 = unittest.TestLoader().loadTestsFromTestCase(test_login)
# masterTestSuit = unittest.TestSuite([tc1])
# unittest.TextTestRunner(verbosity=2).run(masterTestSuit)

# import pytest
# import os
# print(os.getcwd())

# def run_test_cases_from_file(filename):
#     """Runs all the test cases in the specified file"""
#     pytest.main(["-q", filename])

# def run_all_test_cases():
#     """Runs all test cases in both files in sequence"""
#     run_test_cases_from_file("/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02/test_client.py")  # contains 30 test cases
#     # run_test_cases_from_file("TestCases/Package_maintenance/TC_corrective_maintenance.py")  # contains 20 test cases

# if __name__=='__main__':
#     run_all_test_cases()
import unittest
from TestCases.Package_Login_01.TC_Login import Test_login
from TestCases.Package_Client_02.test_client import Test_client 
# from TestCases.Package_Plant.TC_plant import Test_plant
# from TestCases.Package_maintenance.test_corrective_maintenance import Test_Corrective
# from TestCases.Package_maintenance.TC_remedial_maintenance import Test_Remedial
# from TestCases.Package_entity_management.TC_asset_category import Test_Asset_Category
# from TestCases.Package_entity_management.TC_asset import Test_Asset
# from TestCases.Package_entity_management.TC_DNO import Test_DNO
# from TestCases.Package_entity_management.TC_failure_reason import Test_Failure_Reason
# from TestCases.Package_entity_management.TC_manufacturer import Test_Manufacturer
# from TestCases.Package_entity_management.TC_SLA import Test_SLA

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(Test_client))
#     suite.addTest(unittest.makeSuite(Test_Corrective))

#     runner = unittest.TextTestRunner()
#     runner.run(suite)