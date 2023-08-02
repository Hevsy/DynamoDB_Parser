import re

def log_error(message):
    with open("error.log", "a") as log_file:
        log_file.write(message + "\n")

def parse_entry(entry):
    parts = entry.split()
    if len(parts) != 2:
        return None, None
    return parts

def url_strip(s):
    pat = r"^(http(s)?:\/\/)?(www\.)?"
    return re.sub(pat, "", s)

def slash_strip(s):
    return s.rstrip("/")

def split_url(url):
    url = url_strip(slash_strip(url))
    site_id, *path = url.split('/')
    return site_id,path