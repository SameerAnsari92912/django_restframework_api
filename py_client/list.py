import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password")

auth_response  = requests.post(endpoint ,json={"username":username,'password':password}) #http get request 
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }


    endpoint = "http://localhost:8000/api/products/"

    get_reponse = requests.get(endpoint,headers=headers) #http get request 
    print(get_reponse.json())
