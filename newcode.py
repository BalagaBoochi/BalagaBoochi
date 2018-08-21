import requests

url = 'https://duckduckgo.com/html/'
payload = {'q':'python'}
response = requests.get(url, params=payload)

print(response.text)