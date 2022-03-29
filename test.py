# import requests
# import json
# url = "https://google-news.p.rapidapi.com/v1/search"
# query = "dragon ball"
# querystring = {"q":query,"country":"US","lang":"en"}

# headers = {
#     'x-rapidapi-key': "d91e691f2cmsh042308c88546e6ep1128ccjsn2fedb6de25b2",
#     'x-rapidapi-host': "google-news.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# import the module
import requests
from pprint import pprint

pprint(r.json())
print(r.json())