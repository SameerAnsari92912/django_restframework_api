import requests


#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_reponse = requests.post(endpoint,params={"abc":123}, json={"content":"hello world"}) #http get request 
#print(get_reponse.json()['message'])   # print the raw text response

#print(get_reponse.json) //for json respon 
#print(get_reponse.status_code)

"""
HTTP Request -> HTML
REST API HTTP Request-> JSON

"""


print(get_reponse.json())



"""
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.28.2",
    "X-Amzn-Trace-Id": "Root=1-63f638be-2098defa1d8c619852f16d78"
  },
  "json": null,
  "method": "GET",
  "origin": "111.92.134.19",
  "url": "https://httpbin.org/anything"
}



"""