import json
import requests


headers_data = {
    'Authorization': 'Bearer 9acdbea1e7232a692228b226b18959581e63cd2b'
}
endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This cool thing happerns",
    "price":1111
}
get_response = requests.post(endpoint,json=data,headers = headers_data )

print(get_response.json())