from urllib import response
import boto3
from botocore.exceptions import ClientError

table_name = "DynamoDB_parser-dev"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

print(list(dynamodb.tables.all()))
try:
    # client.put_item(Item={"id": "34", "company": "microsoft"})
    siteID = "google.co"
    response = table.get_item(Key={"siteId": siteID})
    print(response, "______________", response["Item"], end="\n")

except ClientError as err:
    print(err)

# try:
#     # client.put_item(Item={"id": "34", "company": "microsoft"})
#     response2 = client.put_item(
#         TableName="DynamoDB_parser-dev", Item={"siteId": {"S": "google.co"}}
#     )
#     print(response2)
# except ClientError as err:
#     print(err)
