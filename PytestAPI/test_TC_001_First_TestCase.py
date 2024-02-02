import pytest

# Test case code must be written inside a method in pytest
# Method name must be started test for pytest\

actual_result = "Hello"

@pytest.mark.TopPriority
def test_tc_001_login_testing():
    print('This is our test case code......')
    print("This is end of my test cases")
    assert actual_result == "Hello1"


@pytest.mark.TopPriority
def test_tc_003_logout_testing():
    print('This is our 3rd smoke test case code......')
    print("This is end of 3rd my sanity test cases")