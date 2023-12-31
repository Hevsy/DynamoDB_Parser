from time import time
from urllib import response
from xml.etree.ElementTree import Comment
import boto3
from botocore.exceptions import ClientError
from func import timestamp, create_nested_structure

table_name = "DynamoDB_parser-dev"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

# print(list(dynamodb.tables.all()))
try:
    siteID = "google.coz"
    path = ["foo", "bar", "baz"]
    site_category = ["H6dsAI7l"]
    comment = "Imported " + timestamp()
    record = create_nested_structure("site", siteID, path, site_category, comment)

    response = table.put_item(Item=record)
    print(response, "_" * 88, sep="\n")
    print(comment, record, sep="\n")

except ClientError as err:
    print(err)

# print(list(dynamodb.tables.all()))
# try:
#     # client.put_item(Item={"id": "34", "company": "microsoft"})
#     siteID = "google.co"
#     response = table.get_item(Key={"siteId": siteID})
#     print(response, "______________", response["Item"], sep="\n")

# except ClientError as err:
#     print(err)

# try:
#     # client.put_item(Item={"id": "34", "company": "microsoft"})
#     response2 = client.put_item(
#         TableName="DynamoDB_parser-dev", Item={"siteId": {"S": "google.co"}}
#     )
#     print(response2)
# except ClientError as err:
#     print(err)
