import requests
import json
import jsonpath

base_url = "https://reqres.in/api/users"

# Read input Json File_File handling Concept

file = open('C:\\Users\API\\CreateUser.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

response = requests.post(base_url, request_json)
print(response)

assert response.status_code==201

print(response.headers.get('Content-Length'))

# Parse response to Json Format
response_json = json.loads(response.text)

# pick id from Jasonpath
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])




