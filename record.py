import re

from func import timestamp


class Record:
    def __init__(self, site_id, path, comment, site_categories, key):

        self.site_id = site_id
        self.path = path
        self.comment = comment
        self.site_categories = site_categories
        self.key = key
        self.is_invalid = True if not site_id or not site_categories else False

        self.data = self._create_record()

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

        comment = "Imported " + timestamp()
        return cls(site_id, path, comment, site_categories, key)

    def _create_record(self):
        """
        Create a nested dictionary structure representing a DynamoDB record.

        Returns:
            dict: The nested dictionary structure.
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
