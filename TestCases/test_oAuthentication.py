import json
import requests
import jsonpath


def test_oauth_api():
    token_url='http://thetestingworldapi.com/Token'
    data={'grant_type':'password', 'username':'admin', 'password':12345}
    response = requests.post(token_url, data)
    token_value=jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authentication':'Bearer'+token_value[0]}
    API_URL = 'http://thetestingworldapi.com/api/StDetails/1104'
    requests.get(API_URL, headers=auth)
    print(response.text)

