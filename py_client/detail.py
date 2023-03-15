import requests

endpoint = "http://localhost:8000/api/products/5/"

get_reponse = requests.get(endpoint) #http get request 
print(get_reponse.json())

