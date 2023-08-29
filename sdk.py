from urllib import response
import boto3

client = boto3.client("dynamodb")

response = client.list_tables()
print(response)
try:
    response = client.put_item (
        TableName = "DynamoDB_parser-dev", 
        Item = {'siteId' = 'google.co', 'site'= ['google', 'com'], 'categories' = 'H6dsAI7l'})
    print (response)
except ClientError as err:
    print (err)