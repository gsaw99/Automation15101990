import requests
from requests.auth import HTTPBasicAuth

def test_authentication():
    base_url = "https://api.github.com/user"
    response = requests.get(base_url, auth=HTTPBasicAuth('testingworld', 1234567))
    print(response)


