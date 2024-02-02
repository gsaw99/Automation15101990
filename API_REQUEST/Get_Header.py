import requests

base_url = "https://httpbin.org/get"

headerdata = {'T1': 'First _Header', 'T2':'Second_Header'}  # Customized headers
response = requests.get(base_url, headers=headerdata)
print(response.text)
