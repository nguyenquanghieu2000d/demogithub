import requests
import json

url = "http://api.cms.beetai.com/api/boxEngine/getById/5928"

headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDk4MTM3OTMsIm5iZiI6MTYwOTgxMzc5MywianRpIjp7ImVtYWlsIjoiYWRtaW5AYmVldHNvZnQuY29tLnZuIiwicnVsZSI6IjEiLCJ1c2VyX2lkIjoxfSwiZXhwIjoxNjEwNDE4NTkzLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.vmMRmJEjjj7HBlIjCtMnbmOxsFHfPtICvEBBGjp77eQ'}

res = requests.get(url, headers=headers)

res = json.loads(res.text)

print(res)