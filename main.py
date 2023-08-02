from func import log_error, slash_strip, url_strip, valid_entry


with open("list1.txt", "r") as file:
    for line in file:
        line = line.split()
        if len(line) != 2 or not valid_entry(line[0]):
            log_error("Invalid line")
        if valid_entry(line[0]):
            line[0] = slash_strip(url_strip(line[0]))
        print(line)
