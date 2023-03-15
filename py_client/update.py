import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {
    "title":"Hello world my old friend",
    "price": 30
}

get_reponse = requests.put(endpoint,json=data) #http get request 
print(get_reponse.json())

