import re


def log_error(e):
    pass


def validation(s):
    pattern = r""
    pass


def url_strip(s):
    pattern = r"^(http(s)?:\/\/)?(www.)?"
    return re.sub(pattern, "", s)


def slash_strip(s):
    """Strips trailing slash"""
    return s.rstrip("/")


def url_strip(url):
    """Strips a string (presumably, URL) of http(s)://(www) and trailing slash"""
    try:
        s = str(url)
    except:
        log_error()
    result = url.strip("http")
    r"^(?:http|ftp)s?://(www.)"  # http:// or https://


with open("list1.txt", "r") as file:
    for line in file:
        line = line.split()
        if 2 > len(line) > 3 or validation(line[0]) == "invalid":
            log_error("Invalid line")
        if validation(line[0]) == "url":
            line[0] = slash_strip(url_strip(line[0]))
        print(line)
