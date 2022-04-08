import json
import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,params={"abc":123 },json={"content_type":"Hello World"})
# print(get_response.te 
print(get_response.json())