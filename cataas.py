#!/usr/bin/python3
import requests

url ="http://cat-fcat.herokuapp.com"

cataas= requests.get(url)

cat_data = cataas.json()

for fact in cat_data:
    print(fact['text']+"\n")
