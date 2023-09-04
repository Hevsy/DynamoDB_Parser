from datetime import datetime
from tzlocal import get_localzone
import re


class Record:
    def __init__(self, site_id, path, comment, site_categories, invalid_entry, key):

        self.site_id = site_id
        self.path = path
        self.comment = comment
        self.site_categories = site_categories
        self.key = key
        self.is_invalid = invalid_entry

        # nested_structure = {"siteId": self.site_id}

        # current_level = nested_structure

        # for folder in self.path:
        #     current_level[key] = {folder: {}}
        #     current_level = current_level[key][folder]

        # current_level["comment"] = self.comment
        # current_level["categories"] = site_categories

        self.data = self.create_record()

    @classmethod
    def from_line(cls, line, delimeter=" ", key="site"):

        parts = line.strip().split(delimeter)

        # Two parts required for parsing: URL and site category.
        # If there are more or less parts in the line, it is considered malformed
        # and the function returns 'None' for all outputs and also returns True for invalid_entry
        if len(parts) != 2:
            return None  # Create an invalid Record
        url = parts[0]
        site_categories = [parts[1]]
        site_id, path = Record._parse_url(url)
        invalid_entry = False

        comment = "Imported " + timestamp()
        return cls(site_id, path, comment, site_categories, invalid_entry, key)

    def create_record(self):
        """
        Create a nested dictionary structure representing a DynamoDB record.

        Returns:
            dict: The nested dictionary structure.
        """
        nested_structure = {"siteId": self.site_id}

        current_level = nested_structure

        for folder in self.path:
            current_level[self.key] = {folder: {}}
            current_level = current_level[self.key][folder]

        current_level["comment"] = self.comment
        current_level["categories"] = self.site_categories

        return nested_structure

    @staticmethod
    def _url_strip(s):
        """
        Returns a string with the URL protocol ('http' or 'https') and 'www' prefix stripped.

        Args:
            s (str): The input URL string.

        Returns:
            str: The input URL with protocol and 'www' prefix removed.
        """
        pat = r"^(http(s)?:\/\/)?(www\.)?"
        return re.sub(pat, "", s)

    @staticmethod
    def _slash_strip(s) -> str:
        """
        Returns a string with the trailing '/' characters stripped.

        Args:
            s (str): The input string.

        Returns:
            str: The input string with trailing '/' characters removed.
        """
        return s.rstrip("/")

    @staticmethod
    def _parse_url(url):
        """
        Splits a URL into site ID and path components after stripping protocol and 'www'.

        Args:
            url (str): The input URL string.

        Returns:
            tuple: A tuple containing site ID and path components of the URL.
        """
        url = Record._url_strip(Record._slash_strip(url))
        site_id, *path = url.split("/")
        return site_id, path

    def __str__(self):
        # Override __str__ for debugging or logging

        return (
            f"Invalid record"
            if self.is_invalid
            else f"site_category: {self.site_categories}, site_id: {self.site_id}, path: {self.path}"
        )

    # def parse_line(self, line, delimiter=" "):
    #     """
    #     Parses a line of text containing a URL and site category.

    #     Args:
    #         line (str): The input line to parse.
    #         delimiter (str, optional): The delimiter used to split the line into parts. Defaults to space (' ').

    #     Returns:
    #         tuple: A tuple containing site category, site ID, and path components.
    #     """
    #     parts = line.strip().split(delimiter)

    #     # Two parts required for parsing: URL and site category.
    #     # If there are more or less parts in the line, it is considered malformed
    #     # and the function returns 'None' for all outputs, indicating it can be flagged as invalid.
    #     if len(parts) != 2:
    #         return None, None, None
    #     url = parts[0]
    #     site_category = parts[1]
    #     site_id, path = self._parse_url(url)
    #     return site_category, site_id, path

    # @staticmethod
    # def invalid_output(site_category, site_id) -> bool:
    #     """
    #     Checks if both required parts exist: site ID and site category.

    #     Args:
    #         site_category (str): The site category.
    #         site_id (str): The site ID.

    #     Returns:
    #         bool: True if either site ID or site category is missing, indicating an invalid output.
    #     """
    #     return not site_id or not site_category


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
