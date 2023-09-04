import logging,boto3
from time import sleep
from botocore.exceptions import ClientError
from logging_config import setup_logging
from record import Record

from config import DYNAMODB_TABLE_NAME, TIMEOUT, WAIT_TIME


def main():
    setup_logging() # Set up logging configuration

    table_name = DYNAMODB_TABLE_NAME

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
                try:
                    response = table.put_item(Item=record.data)
                    logging.info(f"Succesfully parsed line: {record.data}")
                except ClientError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")

            print(record, sep="\n")  # for debugging
            print("_" * 88)
            sleep(TIMEOUT/1000)



if __name__ == "__main__":
    main()
