import requests

def visitGet(url, params):
    response = requests.get(url, params=params)
    print (response)
    return response

def visitPost(url, params):
    response = requests.post(url, params=params)
    return response