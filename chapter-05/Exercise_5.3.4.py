import boto3

kms_client = boto3.client('kms', region_name='us-west-1')
response = kms_client.schedule_key_deletion(
    KeyId='fasdf1-2451b-151-bea2-easdfg8',
    PendingWindowInDays=7
)

print(response, indent=4, sort_keys=True)