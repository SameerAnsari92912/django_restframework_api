import requests

product_id = input("What is the product id you want to use \n")

try:
    product_id = int(product_id)
except:
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = "http://localhost:8000/api/products/{product_id}/delete/"

    get_reponse = requests.delete(endpoint) #http get request 
    print(get_reponse.status_code,get_reponse.status_code==204)

