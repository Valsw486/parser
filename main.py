import requests
import pprint

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.ok)

#print(response.text)
print(response.content)

response_json = response.json()


pprint.pprint(response_json)
