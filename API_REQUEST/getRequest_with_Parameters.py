import requests

base_url = "https://httpbin.org/get"
param = {'name':'Gopal', 'email':'gopalsaw90@gmail.com', 'mobile':'7676437323'}
response = requests.get(base_url, params=param)


print(response.text)