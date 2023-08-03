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
    site_id, *path = url.split("/")
    return site_id, path


def parse_line(line):
    url, site_category = parse_entry(line)
    site_id, path = split_url(url)
    return site_category, site_id, path


def invalid_output(site_category, site_id):
    return not site_id or not site_category
