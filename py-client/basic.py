import json
import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,params={"abc":123 },json={"query":"Hello World"})
# print(get_response.te 
print(get_response.json())