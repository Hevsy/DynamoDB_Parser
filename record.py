import re

from func import parse_url, timestamp


class Record:
    """
    Represents a record to be stored in DynamoDB.

    Args:
        site_id (str): The site ID.
        site_categories (list): List of site categories.
        key (str): The key for nesting levels.

    Attributes:
        site_id (str): The site ID.
        site_categories (list): List of site categories.
        key (str): The key for nesting levels.
        is_invalid (bool): Indicates whether the record is invalid.
        _data (dict or None): The nested dictionary structure representing the DynamoDB record.
    """

    def __init__(self, site_id, path, comment, site_categories, key):
        self.site_id = site_id
        self.path = path
        self.comment = comment
        self.site_categories = site_categories
        self.key = key
        self.is_invalid = not (self.site_id and self.site_categories)

        self.data = self._create_record()

    @classmethod
    def from_line(cls, line, delimiter=" ", key="site"):
        """
        Create a Record instance from a line of text.

        Args:
            line (str): The input line to parse.
            delimiter (str, optional): The delimiter used to split the line into parts. Defaults to space (' ').
            key (str, optional): The key for nesting levels. Defaults to "site".

        Returns:
            Record: A Record instance created from the input line.
        """
        parts = line.strip().split(delimiter)

        # Two parts required for parsing: URL and site category.
        # If there are more or less parts in the line, it is considered malformed
        # and the function returns 'None' for all outputs and also returns True for invalid_entry
        if len(parts) != 2:
            return None  # Create an invalid Record
        url = parts[0]
        site_categories = [parts[1]]
        site_id, path = parse_url(url)

        comment = "Imported " + timestamp()
        return cls(site_id, path, comment, site_categories, key)

    def _create_record(self):
        """
        Create the nested dictionary structure representing a DynamoDB record.

        Returns:
            dict or None: The nested dictionary structure if valid, otherwise None.
        """
        if self.is_invalid:
            return None
        else:
            nested_structure = {"siteId": self.site_id}

            current_level = nested_structure

            for folder in self.path:
                current_level[self.key] = {folder: {}}
                current_level = current_level[self.key][folder]

            current_level["comment"] = self.comment
            current_level["categories"] = self.site_categories

        return nested_structure

    def __str__(self):
        """
        Get a string representation of the record.

        Returns:
            str: A string representation of the record.
        """

        return (
            f"Invalid record"
            if self.is_invalid
            else f"site_category: {self.site_categories}, site_id: {self.site_id}, path: {self.path}"
        )
