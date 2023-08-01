def log_error(e):
    # TODO: logging errors
    pass


def valid_entry(s):
    # TODO: entry validation
    pattern = r""
    return True


def url_strip(s) -> str:
    """Strips a string (presumably, URL) of http(s)://(www.)"""
    pat = r"^(http(s)?:\/\/)?(www.)?"
    return re.sub(pat, "", s)

def slash_strip(s) -> str:
    """Strips trailing slash"""
    return s.rstrip("/")