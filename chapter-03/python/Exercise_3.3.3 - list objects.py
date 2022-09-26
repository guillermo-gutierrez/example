import boto3

# Retrieve the list of existing buckets
s3 = boto3.client("s3")
response = s3.list_objects_v2(
    Bucket='devadmin-bucket'
)

# Output the object names
print("Existing objects:")
for content in response.get('Contents', []):
    print(content['Key'])