import requests
import json
resp = requests.get('http://192.168.2.201:8096/bitable?option=5&timeout=6')

print(resp.json()['code'])