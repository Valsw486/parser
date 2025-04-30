import requests
import pprint

params = {
    'q': 'html'
}
response = requests.get( url='https://api.github.com/search/repositories',
params = params)

print(response.status_code)
print(response.ok)
response_json = response.json()
pprint.pprint(response_json)
