import boto3

# Create an S3 access object
s3 = boto3.client("s3")

response = s3.upload_file(
    Filename="../chapter-12/input.payroll.data.csv",
    Bucket="devadmin-bucket",
    Key="new_file.csv",
)

print (response)