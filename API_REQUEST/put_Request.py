import requests
import json
import jsonpath

base_url = "https://reqres.in/api/users/2"

# Read input Json File_File handling Concept

file = open('C:\\Users\API\\CreateUser.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(base_url, request_json)

# validation Response Code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_id = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_id[0])


