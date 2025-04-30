import requests
import pprint

params = {
    'q': 'python'
}

response = requests.get( url='https://api.github.com/search/repositories',
params = params)

response_json = response.json()

print(response.status_code)
print(response.ok)
pprint.pprint(response_json)
