from urllib.parse import urlparse
from func import log_error, slash_strip, url_strip, valid_entry


with open("list1.txt", "r") as file:
    for line in file:
        try:
            line = line.split()
            url = line[0]
            site_category = line[1]
        except:
            log_error("Invalid line")
            print ("Error - skipping")
            continue

        if len(line) != 2 or not valid_entry(url):
            log_error("Invalid line")
            print ("Error - skipping")
            continue

        if valid_entry(url):
            parse_object = urlparse(url)
            site_id = url_strip(parse_object.netloc)
            path = slash_strip(parse_object.path)
        print(site_id, path, site_category, sep="\n")
        print("__________________")
