import logging
from func import parse_line, invalid_output, time_now, timestamp


def main():
    logging.basicConfig(
        filename=f"import-error.{time_now('%Y%m%d')}.{time_now('%H%M%S')}.{time_now('%Z')}.log",
        filemode="a",
        format="%(message)s",
    )

    with open("list1.txt", "r") as file:
        for line in file:
            site_category, site_id, path = None, None, None
            if not line:
                continue  # Skip empty lines

            site_category, site_id, path = parse_line(line)

            if invalid_output(site_category, site_id):
                logging.error(f"{timestamp()} Invalid line: {line}")
                print("Error - skipping")  # for debugging
                continue

            print(site_id, path, site_category, sep="\n")  # for debugging
            print("__________________")


if __name__ == "__main__":
    main()
