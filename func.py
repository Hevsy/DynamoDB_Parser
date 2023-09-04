from datetime import datetime
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
