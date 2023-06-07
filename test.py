import requests

def run(*args):
    return('a'*2048)
    return requests.get(args[0]).text[0:int(args[1])]
