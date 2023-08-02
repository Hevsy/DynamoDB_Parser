from func import log_error, split_url, url_strip, slash_strip, parse_entry

def main():
    with open("list1.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:
                continue  # Skip empty lines
            
            url, site_category = parse_entry(line)
            
            if not url or not site_category:
                log_error("Invalid line")
                print("Error - skipping")
                continue
            
            site_id, path = split_url(url)
            
            print(site_id, path, site_category, sep="\n")
            print("__________________")



if __name__ == "__main__":
    main()
