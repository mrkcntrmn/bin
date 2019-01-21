import boto3


client=boto3.client('rekognition')

response = client.detect_text(
    Image={
        'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 26lenox,
            'Name': test.jpg            
        }
    }
)  
