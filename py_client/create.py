import requests

endpoint = "http://localhost:8000/api/products/"
data = {"title":"This field is done",
        "price": 32.99
}
get_reponse = requests.post(endpoint,json=data) #http get request 
print(get_reponse.json())
