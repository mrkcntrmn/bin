import boto3

if __name__ == "__main__":

    bucket='15rek'
    photo='Scan.png'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('BoundingBox: {}'.format(text['BoundingBox']))
          
            print
