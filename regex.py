import re
import string


def url_strip (s):
    pat = r"^(http(s)?:\/\/)?(www.)?"
    return re.sub(pat, "", s)

def slash_strip(s):
    return s.rstrip('/')

with open('list1.txt', 'r') as file:
    for line in file:
        line = line.split()
        line [0] = slash_strip(url_strip(line[0]))
        print (line)

