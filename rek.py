import boto3

# Let's use Amazon S3
rek = boto3.client('rekognition')

bucket = "26lenox"
photo = "test.jpg"    

  
response=rek.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
textDetections=response['TextDetections']
print ('Detected text')
for text in textDetections:
    print ('Detected text:' + text['DetectedText'])
    print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
    print ('Id: {}'.format(text['Id']))
    if 'ParentId' in text:
        print ('Parent Id: {}'.format(text['ParentId']))
    print ('Type:' + text['Type'])
    print    

