#!/usr/bin/python3
import requests

url ="https://api.open-meteo.com//v1/forecast?latitude=41.4&logitude=2.12&current=temperature_2"

tem = requests.get(url)

tem_data = tem.json()

print(tem['latitude']+"\n"+tem['logitude'])

