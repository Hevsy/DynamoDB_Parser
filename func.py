from datetime import datetime
from tzlocal import get_localzone

import re


def url_strip(s):
    """Returns string with the url protocol and 'www' prefix stripped"""
    pat = r"^(http(s)?:\/\/)?(www\.)?"
    return re.sub(pat, "", s)


def slash_strip(s) -> str:
    """Returns string with the trailing '/' stripped"""
    return s.rstrip("/")


def split_url(url):
    url = url_strip(slash_strip(url))
    site_id, *path = url.split("/")
    return site_id, path


def parse_line(line, delimiter=" "):
    parts = line.strip().split(delimiter)

    # Two parts required for parsing: url and site_category.
    # If there are more or less parts in the line - it is considered malfored
    # and function returns 'None' for all outputs, so if can later be flagged as invalid
    if len(parts) != 2:
        return None, None, None
    url = parts[0]
    site_category = parts[1]
    site_id, path = split_url(url)
    return site_category, site_id, path


def invalid_output(site_category, site_id) -> bool:
    """Checks if both required parts exist: site_id and site_category.
    If either one is missing, the output deemed invalid and function return 'True'"""
    return not site_id or not site_category


def time_now(fmt) -> str:
    """Returns current time in a specified format"""
    return datetime.now(tz=get_localzone()).strftime(fmt)


def timestamp() -> str:
    """Returns current time in 'YYYYMMDD HH:MM TMZ' format"""
    fmt = "%Y%m%d %H:%M %Z"
    return time_now(fmt)
