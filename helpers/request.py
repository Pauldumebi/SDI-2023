import requests

baseUrl = ''

def make_request(url):
    req = requests.get(url)
    response = req.json()
    
    if req.status_code == 200:
        return response