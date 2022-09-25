# Exercise 4.6
import boto3
import json
import datetime

# Variables
rds_identifier = 'my-rds-db'
sg_name = 'rds-sg-dev-demo'
sg_id_number = ''

# Create the client for Amazon RDS
rds_client = boto3.client('rds')

# Delete the RDS Instance
response = rds_client.delete_db_instance(
    DBInstanceIdentifier=rds_identifier,
    SkipFinalSnapshot=True
)
print('RDS Instance is being terminated...This may take several minutes.')

waiter = rds_client.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=rds_identifier)

# We must wait to remove the security groups until the RDS database has been deleted, this is a dependency.
print('The Amazon RDS database has been deleted. Removing Security Groups')

# Create the client for Amazon EC2 SG
ec2_client = boto3.client('ec2')

# Get the Security Group ID Number
response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ]
)
sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')

# Delete the Security Group!
response = ec2_client.delete_security_group(
    GroupId=sg_id_number
)

print('Cleanup is complete!')