import requests
from pprint import pprint

response = requests.get('http://localhost:5000/login', params={'email':'jd@myinsuranceapp.com','password':'passwordjd'})

print(response.json())
