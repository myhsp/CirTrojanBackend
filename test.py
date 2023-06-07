import requests

def run(*args):
    return requests.get(args[0]).text

