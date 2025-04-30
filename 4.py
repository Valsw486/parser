import requests
import pprint

params = {
    'q': 'html'
}
response = requests.get( url='https://api.github.com/search/repositories',
params = params)
response_json = response.json()
print(response.status_code)
print(response.ok)

print(f"html: {response_json['total_count']}")