import logging

import boto3
from botocore.exceptions import ClientError

from func import Record, timestamp
from logging_config import setup_logging


def main():
    setup_logging()

    # table_name = "DynamoDB_parser-dev"

    # dynamodb = boto3.resource("dynamodb")
    # table = dynamodb.Table(table_name)

    with open("list1.txt", "r") as file:
        for line in file:
            if not line:
                continue  # Skip empty lines

            record = Record.from_line(line)

            # if record.is_invalid
            #     logging.error(f"Error in line: {line}")
            #     print("Error - skipping")  # for debugging
            #     continue
            # else:
            #     comment = "Imported " + timestamp()
            #     record = create_nested_structure(
            #         "site", site_id, path, site_category, comment
            #     )

            #     try:
            #         response = table.put_item(Item=record)
            #         logging.info(f"Succesfully parsed line: {record}")
            #     except ClientError as err:
            #         logging.error(f"Error writing line {line} to the database: {err}")

            # print(site_id, path, site_category, sep="\n")  # for debugging
            if record:
                print(type(record))
                print(record.data)
                print("_" * 88)
            else:
                print("Invalid line - skipping")
                print("_" * 88)


if __name__ == "__main__":
    main()
