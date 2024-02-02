import requests

base_url = "https://reqres.in/api/users/2"

response = requests.delete(base_url)

# Fetch Response code

print(response.status_code)

assert response.status_code == 204