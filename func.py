from datetime import datetime
from tzlocal import get_localzone
import re

def url_strip(s):
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

def split_url(url):
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

def parse_line(line, delimiter=" "):
    """
    Parses a line of text containing a URL and site category.

    Args:
        line (str): The input line to parse.
        delimiter (str, optional): The delimiter used to split the line into parts. Defaults to space (' ').

    Returns:
        tuple: A tuple containing site category, site ID, and path components.
    """
    parts = line.strip().split(delimiter)

    # Two parts required for parsing: URL and site category.
    # If there are more or less parts in the line, it is considered malformed
    # and the function returns 'None' for all outputs, indicating it can be flagged as invalid.
    if len(parts) != 2:
        return None, None, None
    url = parts[0]
    site_category = parts[1]
    site_id, path = split_url(url)
    return site_category, site_id, path

def invalid_output(site_category, site_id) -> bool:
    """
    Checks if both required parts exist: site ID and site category.

    Args:
        site_category (str): The site category.
        site_id (str): The site ID.

    Returns:
        bool: True if either site ID or site category is missing, indicating an invalid output.
    """
    return not site_id or not site_category

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

def list_to_nested_dict(key, lst):
    """
    Convert a list into a nested dictionary with the specified key.

    This function takes a list and recursively constructs a nested dictionary using the given key. Each element in the list
    becomes a key in the nested dictionary, and the corresponding value is either the next element in the list (if available)
    or the last item in the list.

    Parameters:
        key (str): The key to use for constructing the nested dictionary.
        lst (list): The list of elements to convert into a nested dictionary.

    Returns:
        dict: A nested dictionary constructed from the list using the specified key.
    """
    if len(lst) == 1:
        return {key: lst[0]}
    return {key: {lst[0]: list_to_nested_dict(key, lst[1:])}}