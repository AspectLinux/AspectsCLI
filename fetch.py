from urllib.request import urlopen

def fetch(url):
    f = urlopen(url)
    myfile = f.read()
    return myfile

def fetchandsplit(url):
    f = fetch(url)
    myfile = f.split("\n")
    return myfile