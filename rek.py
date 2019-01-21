import boto3
import json

if __name__ == "__main__":

    bucket='15rek'
    photo='Scan.jpg'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    
    # parse x:
    parse = json.dumps(response, indent=4, sort_keys=True)
    
    print(parse)
    
    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    localfile = open('rek.txt', "w")  
    localfile.write(json.dumps(response))
    # Upload a new file
    data = open('rek.txt', 'rb')
    s3.Bucket('15rek').put_object(Key='rek.txt', Body=data)
