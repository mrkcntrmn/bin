import boto3
import json

if __name__ == "__main__":

    bucket='15rek'
    photo='Scan.png'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    
    # parse x:
    parse = json.dumps(response, indent=4, sort_keys=True)
    
    print(parse)
    
'''    
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Geometry: {}'.format(text['Geometry']))
          
            print
'''
