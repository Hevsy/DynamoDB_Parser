from unicodedata import category
from urllib.parse import urlparse
from posixpath import basename, dirname, normpath

with open("list1.txt", "r") as file:
    for line in file:
        line = line.split()

        url = line[0]
        site_category = line[1]
        parse_object = urlparse(url)

        site_id = parse_object.netloc
        path = dirname(parse_object.path)

        #print(site_id, path, site_category, sep="\n", end="\n__________________\n")

        print(parse_object.netloc)
        print(parse_object.path)
        print (basename(parse_object.path))
        print (dirname(parse_object.path))
        print (normpath(parse_object.path))
        print ('__________________')
        
        
        
