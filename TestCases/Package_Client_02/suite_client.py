import pytest
import os
print(os.getcwd())

def run_test_cases_from_file(filename):
    """Runs all the test cases in the specified file"""
    pytest.main(["-q", filename])

def run_all_test_cases():
    """Runs all test cases in both files in sequence"""
    run_test_cases_from_file("/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02/TC_Client.py")  # contains 30 test cases
    # run_test_cases_from_file("TestCases/Package_maintenance/TC_corrective_maintenance.py")  # contains 20 test cases

if __name__=='__main__':
    run_all_test_cases()