import json
import requests


headers = {
    'Authorization': 'Bearerd3d5a8b3fa96444bbdba1631c456cc2931803fbf'
}
endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This cool thing happerns",
    "price":1111
}
get_response = requests.post(endpoint,json=data,headers = headers )

print(get_response.json())