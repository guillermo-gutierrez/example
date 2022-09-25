# Exercise 4.8
import boto3
import json
import datetime

# In this example we are not using uuid; however, you could use this to autogenerate your user IDs.
# i.e. str(uuid.uuid4())
import uuid

# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('Users')

# Write a record to DynamoDB
response = table.put_item(
    Item={
        'user_id': '1234-5678',
        'user_email': 'someone@somewhere.com', 'user_fname': 'Sam',
        'user_lname': 'Samuels'
    }
)

# Just printing the raw JSON response, you should see a 200 status code
print(json.dumps(response, indent=2, sort_keys=True))