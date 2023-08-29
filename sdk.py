from urllib import response
import boto3
from botocore.exceptions import ClientError

client = boto3.client("dynamodb")

response = client.list_tables()
print(response)
try:
    # client.put_item(Item={"id": "34", "company": "microsoft"})
    response2 = client.put_item(
        TableName="DynamoDB_parser-dev", Item={"siteId": {"S": "google.co"}}
    )
    print(response2)
except ClientError as err:
    print(err)
