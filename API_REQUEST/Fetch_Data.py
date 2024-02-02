import requests
import json
import jsonpath
import string

base_url = "https://reqres.in/api/users?page=2"
response = requests.get(base_url)
print(response.status_code)
assert response.status_code == 200
print(response.content)
print(response.headers)
# Fetch individual headers
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)
# Fetch Encoding
print(response.encoding)
# Fetch Elapsed Time
print(response.elapsed)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

#print(json_response)

# Fetching any individual value of response(it is giving list of value) using jason path

pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
first_name = jsonpath.jsonpath(json_response, 'data[3].first_name')
print(first_name[0])
assert pages[0] == 2

# How to fetch multiple all first_name
for i in range(0, 4):  # Last value will be ignored
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])