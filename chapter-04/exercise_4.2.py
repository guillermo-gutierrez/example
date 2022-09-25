# Excercise 4.2
import boto3
import json
import datetime

# Just a quick helper function for date time conversions, in case you want to print the raw JSON
def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o. str ()

# Variables
sg_name = 'rds-sg-dev-demo'
rds_identifier = 'my-rds-db'
db_name = 'mytestdb'

user_name = 'masteruser'
user_password = 'mymasterpassw0rd1!'
admin_email = 'myemail@myemail.com'
sg_id_number = ''
rds_endpoint = ''

# We need to get the Security Group ID Number to use in the creation of the RDS Instance
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ]
)

sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')

# Create the client for Amazon RDS
rds_client = boto3.client('rds')

# This will create our MariaDB Database
# NOTE: Here we are hardcoding passwords for simplicity and testing purposes only! In production
# you should never hardcode passwords in configuration files/code!
# NOTE: This will create an MariaDB Database. Be sure to remove it when you are done.
response = rds_client.create_db_instance(
    DBInstanceIdentifier=rds_identifier,
    DBName=db_name,
    DBInstanceClass='db.t2.micro',
    Engine='mariadb',
    MasterUsername='masteruser',
    MasterUserPassword='mymasterpassw0rd1!',
    VpcSecurityGroupIds=[
        sg_id_number
    ],
    AllocatedStorage=20,
    Tags=[
        {
            'Key': 'POC-Email',
            'Value': admin_email
        },
        {
            'Key': 'Purpose',
            'Value': 'AWS Developer Study Guide Demo'
        }
    ]
)

# We need to wait until the DB Cluster is up!
print('Creating the RDS instance. This may take several minutes...')
waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_identifier)
print('Okay! The Amazon RDS Database is up!')