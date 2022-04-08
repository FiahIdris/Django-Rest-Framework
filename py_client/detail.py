import json
import requests

endpoint = "http://localhost:8000/api/products/1/"

get_response = requests.get(endpoint,params={"abc":123 },json={"content_type":"Hello World"})
# print(get_response.te 
print(get_response.json())