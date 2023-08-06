import logging
from func import parse_line, invalid_output, time_now, timestamp
from logging_config import setup_logging


def main():
    setup_logging()

    with open("list1.txt", "r") as file:
        for line in file:
            # Initialising data for each loop (otherwise lines with empty field getting values form the prvious line)
            site_category, site_id, path = None, None, None
            if not line:
                continue  # Skip empty lines

            site_category, site_id, path = parse_line(line)

            if invalid_output(site_category, site_id):
                logging.error(f"Error in line: {line}")
                print("Error - skipping")  # for debugging
                continue
            else:
                logging.info(f"Succesfully parsed line: {line}")

            print(site_id, path, site_category, sep="\n")  # for debugging
            print("__________________")


if __name__ == "__main__":
    main()
