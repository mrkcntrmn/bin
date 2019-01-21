import boto3

bucket='26lenox'
photo='test.jpg'

client=boto3.client('rekognition')

response = client.detect_text(
    Image={
        'Bytes': b'bytes',
        'S3Object': {
            'Bucket': bucket,
            'Name': photo            
        }
    }
)  
