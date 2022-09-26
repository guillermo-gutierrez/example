from urllib import response
import boto3

# Create an S3 access object
s3 = boto3.client("s3")

response = s3.download_file(
    Bucket="devadmin-bucket",
    Key="new_file.csv",
    Filename="../chapter-03/downloaded_from_s3.csv"
)

print (response)