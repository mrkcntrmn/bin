import boto3


client=boto3.client('rekognition')

response=client.detect_text(Image={'https://s3.us-east-2.amazonaws.com/26lenox/cert.jpg'})
