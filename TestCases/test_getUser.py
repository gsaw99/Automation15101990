import requests
import json
import jsonpath
import pytest


@pytest.mark.Smoke
def test_fetch_user_details():
    base_url = "https://reqres.in/api/users?page=2"
    response = requests.get(base_url)
    print(response.status_code)
    assert response.status_code == 200
    print(response.content)
    print(response.headers)
    print(response.headers.get('Date'))
    print(response.headers.get('Server'))
    print(response.cookies)
    print(response.encoding)
    print(response.elapsed)
    json_response = json.loads(response.text)
    print(json_response)
   #print(json_response)
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])
    first_name = jsonpath.jsonpath(json_response, 'data[3].first_name')
    print(first_name[0])
    assert pages[0] == 2
    for i in range(0, 4):  # Last value will be ignored
        first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print(first_name[0])
