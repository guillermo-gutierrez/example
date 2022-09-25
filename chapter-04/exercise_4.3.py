# Exercise 4.3
import boto3
import json
import datetime

# Just a quick helper function for date time conversions, in case you want to print the raw JSON

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o. str ()

# Variables
rds_identifier = 'my-rds-db'

# Create the client for Amazon RDS
rds_client = boto3.client('rds')
print("Fetching the RDS endpoint...")
response = rds_client.describe_db_instances(
    DBInstanceIdentifier=rds_identifier
)

rds_endpoint = json.dumps(response['DBInstances'][0]['Endpoint']['Address'])
rds_endpoint = rds_endpoint.replace('"','')
print('RDS Endpoint: ' + rds_endpoint)