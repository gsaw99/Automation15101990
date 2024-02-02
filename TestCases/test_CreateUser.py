import requests
import json
import jsonpath
import pytest


#a = 10
#@pytest.mark.skip("This is not valid for current build")
#@pytest.mark.skipif(a>10, reason="conition is not satisfied")

@pytest.fixture()
def setUp():
    global file
    file = open('C:\\Users\API\\CreateUser.json', 'r')
    yield
    print("i will execute at last")
@pytest.mark.Smoke
def test_create_new_user(setUp):
    base_url = "https://reqres.in/api/users"
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(base_url, request_json)
    print(response)
    assert response.status_code == 201
@pytest.mark.Sanity
def test_create_other_user(setUp):
    base_url = "https://reqres.in/api/users"
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(base_url, request_json)
    print(response)
    assert response.status_code == 201
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])