from func import log_error, parse_line, invalid_output


def main():
    with open("list1.txt", "r") as file:
        for line in file:
            site_category, site_id, path = None, None, None
            if not line:
                continue  # Skip empty lines
            line = line.strip()  # Remove leading/trailing whitespace

            site_category, site_id, path = parse_line(line)

            if invalid_output(site_category, site_id):
                log_error("Invalid line: " + line)
                print("Error - skipping")  # for debugging
                continue

            print(site_id, path, site_category, sep="\n")  # for debugging
            print("__________________")  # for debugging


if __name__ == "__main__":
    main()
