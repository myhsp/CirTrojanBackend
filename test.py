import requests

def run(*args):
    return requests.post('http://bilibili.com').text
