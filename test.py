import requests

def run(*args):
    return requests.post(args[0]).text[0:int(args[1])]
