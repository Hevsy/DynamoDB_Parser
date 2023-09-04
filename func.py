from datetime import datetime
import re
from tzlocal import get_localzone


def time_now(fmt) -> str:
    """
    Returns the current time in a specified format.

    Args:
        fmt (str): The desired time format.

    Returns:
        str: The current time formatted according to the provided format.
    """
    return datetime.now(tz=get_localzone()).strftime(fmt)


def timestamp() -> str:
    """
    Returns the current time in 'YYYYMMDD HH:MM TMZ' format.

    Returns:
        str: The current time formatted as 'YYYYMMDD HH:MM TMZ'.
    """
    fmt = "%Y%m%d %H:%M %Z"
    return time_now(fmt)


def create_nested_structure(key, site_id, path, categories, comment):
    """
    Create a nested dictionary structure representing a DynamoDB record.

    Args:
        key (str): The key used for nesting levels.
        site_id (str): The site ID.
        path (list): List of path elements for nesting.
        categories (list): List of strings representing categories.
        comment (str): The comment for the record.

    Returns:
        dict: The nested dictionary structure.
    """
    nested_structure = {"siteId": site_id}

    current_level = nested_structure

    for folder in path:
        current_level[key] = {folder: {}}
        current_level = current_level[key][folder]

    current_level["comment"] = comment
    current_level["categories"] = categories

    return nested_structure


def url_strip(s) -> str:
    """
    Returns a string with the URL protocol ('http' or 'https') and 'www' prefix stripped.

    Args:
        s (str): The input URL string.

    Returns:
        str: The input URL with protocol and 'www' prefix removed.
    """
    pat = r"^(http(s)?:\/\/)?(www\.)?"
    return re.sub(pat, "", s)


def slash_strip(s) -> str:
    """
    Returns a string with the trailing '/' characters stripped.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with trailing '/' characters removed.
    """
    return s.rstrip("/")


def parse_url(url) -> str:
    """
    Splits a URL into site ID and path components after stripping protocol and 'www'.

    Args:
        url (str): The input URL string.

    Returns:
        tuple: A tuple containing site ID and path components of the URL.
    """
    url = url_strip(slash_strip(url))
    site_id, *path = url.split("/")
    return site_id, path
