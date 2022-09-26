from urllib import response
import boto3

# Create an S3 access object
s3 = boto3.client("s3")

response = s3.delete_object(
    Bucket="devadmin-bucket",
    Key="new_file.csv"
)

print (response)