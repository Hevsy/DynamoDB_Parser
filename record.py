import re

from func import parse_url, timestamp


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
    def from_line(cls, line, delimiter=" ", key="site"):
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

    def __str__(self):
        # Override __str__ for debugging or logging

        return (
            f"Invalid record"
            if self.is_invalid
            else f"site_category: {self.site_categories}, site_id: {self.site_id}, path: {self.path}"
        )
