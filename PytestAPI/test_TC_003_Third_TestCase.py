import pytest

# Test case code must be written inside a method in pytest
# Method name must be started test for pytest
@pytest.fixture(scope="module")  # It will execute at the module lavel i.e start of the module and end of the module
def setUp():
    print("This is our fixture code will execute before testcase")
    print("------------------------------------------------------")
    yield
    print("close DB connection after executing TestCases")
    print("------------------------------------------------------")
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_004_login_testing(setUp):
    print('This is our smoke test case code......')
    print("This is end of my smoke test cases")

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_005_logout_testing(setUp):
    print('This is our Sanity test case code......')
    print("This is end of 3rd sanity test cases")