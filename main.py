import logging

import boto3
from botocore.exceptions import ClientError

from func import create_nested_structure, timestamp
from logging_config import setup_logging
from record import Record


def main():
    setup_logging()

    table_name = "DynamoDB_parser-dev"

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    with open("list1.txt", "r") as file:
        for line in file:

            if not line:
                continue  # Skip empty lines

            record = Record.from_line(line)

            if not record or record.is_invalid:
                logging.error(f"Error in line: {line}")
                print("Error - skipping")  # for debugging
                continue
            else:
                data = record.data

                try:
                    response = table.put_item(Item=data)
                    logging.info(f"Succesfully parsed line: {data}")
                except ClientError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")

            print(record, sep="\n")  # for debugging
            print("_" * 88)


if __name__ == "__main__":
    main()
