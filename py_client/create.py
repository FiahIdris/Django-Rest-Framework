import json
import requests

endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This cool thing happerns",
    "price":1111
}
get_response = requests.post(endpoint,json=data)

print(get_response.json())