import logging, boto3
from time import sleep
from botocore.exceptions import ClientError, ReadTimeoutError, ConnectTimeoutError
from logging_config import setup_logging
from record import Record

from config import DYNAMODB_TABLE_NAME, WAIT_TIME, CONNECT_TIMEOUT, READ_TIMEOUT
from db_utils import DynamoDBHandler


def main():
    setup_logging()  # Set up logging configuration

    table = DynamoDBHandler(
        DYNAMODB_TABLE_NAME, CONNECT_TIMEOUT / 1000, READ_TIMEOUT / 1000
    )  # Set up DynamoDB connection

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
                    response = table.put_item(
                        Item=record.data, ReturnConsumedCapacity="TOTAL"
                    )
                    logging.info(f"Succesfully parsed line: {record.data}")
                except ClientError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")
                    print(f"Client error: {err}")
                    continue

                except ReadTimeoutError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")
                    print(f"Timeout error: {err}")
                    continue

                except ConnectTimeoutError as err:
                    logging.error(f"Error writing line {line} to the database: {err}")
                    print(f"Timeout error: {err}")
                    continue

            print(record, sep="\n")  # for debugging
            print("_" * 88)
            sleep(WAIT_TIME / 1000)


if __name__ == "__main__":
    main()
