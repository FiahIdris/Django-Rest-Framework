
import requests

endpoint = "http://localhost:8000/api/products/242344234534534543"

get_response = requests.get(endpoint)

print(get_response.json())