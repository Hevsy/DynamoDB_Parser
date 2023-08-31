import logging

import boto3
from botocore.exceptions import ClientError

from func import create_nested_structure, invalid_output, parse_line, timestamp
from logging_config import setup_logging


def main():
    setup_logging()

    table_name = "DynamoDB_parser-dev"

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    with open("list1.txt", "r") as file:
        for line in file:
            # Initialising data for each loop (otherwise lines with an empty field getting values form the prvious line)
            site_category, site_id, path = None, None, None
            if not line:
                continue  # Skip empty lines

            site_category, site_id, path = parse_line(line)

            if invalid_output(site_category, site_id):
                logging.error(f"Error in line: {line}")
                print("Error - skipping")  # for debugging
                continue
            else:
                comment = "Imported " + timestamp()
                record = create_nested_structure(
                    "site", site_id, path, site_category, comment
                )

                try:
                    response = table.put_item(Item=record)
                    logging.info(f"Succesfully parsed line: {record}")
                except ClientError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")

            print(site_id, path, site_category, sep="\n")  # for debugging
            print("_" * 88)


if __name__ == "__main__":
    main()
