import requests

url = 'SOME URL'

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

response = requests.get(url, headers=headers)
content = response.content
