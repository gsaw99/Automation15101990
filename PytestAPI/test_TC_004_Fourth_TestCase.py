import pytest

# Test case code must be written inside a method in pytest
# Method name must be started test for pytest

@pytest.mark.Smoke
def test_tc_006_login_testing():
    print('This is our smoke  test case code......')
    print("This is end of my test cases")

@pytest.mark.Sanity
def test_tc_007_logout_testing():
    print('This is our 3rd test sanity case code......')
    print("This is end of 3rd my sanity test cases")