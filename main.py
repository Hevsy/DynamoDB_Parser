import re

def log_error():
    pass

def url_strip(url):
    """ Strips a string (presumably, URL) of http(s)://(www) and trailing slash"""
    try: s=str(url)
    except: log_error() 
    result = url.strip("http")
    r'^(?:http|ftp)s?://(www.)' # http:// or https://
