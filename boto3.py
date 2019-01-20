'''
Created on Jan 19, 2019
@author: MARK
'''

#This is a comment using Python!


print "Python2 running..."


print "Boto3 importing..."

import boto3



# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
