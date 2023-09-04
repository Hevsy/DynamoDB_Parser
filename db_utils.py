from botocore.config import Config
import boto3


def DynamoDBHandler(table_name, connect_timeout="5", read_timeout="10"):
    """
    Initialize and configure an AWS DynamoDB resource handler for interacting with a specific table.

    Args:
        table_name (str): The name of the DynamoDB table.
        connect_timeout (int, optional): The maximum time to wait for a connection to be established, in seconds. Defaults to 5.
        read_timeout (int, optional): The maximum time to wait for a read operation to complete, in seconds. Defaults to 10.

    Returns:
        boto3.resources.factory.dynamodb.Table: An AWS DynamoDB Table resource.

    Example:
        >>> dynamodb_table = DynamoDBHandler("MyTable", connect_timeout=5, read_timeout=10)
        >>> item = dynamodb_table.get_item(Key={"Key": "Value"})
    """
    config = Config(
        connect_timeout=connect_timeout,
        read_timeout=read_timeout,
        retries={"max_attempts": 5},
    )

    dynamodb = boto3.resource("dynamodb", config=config)
    table = dynamodb.Table(table_name)

    return table
