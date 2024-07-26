import requests

def visitGet(url, params):
    response = requests.get(url, params=params)
    return response

def visitPost(url, params):
    response = requests.post(url, params=params)
    return response