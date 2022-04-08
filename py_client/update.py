import json
import requests

endpoint = "http://localhost:8000/api/products/1/update/"

get_response = requests.put(endpoint,params={"abc":123 },json={"title":"Hello World my old friends","price":500})

print(get_response.json())