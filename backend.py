import requests
import json
from pprint import pprint

result = requests.get(
    'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

# print(result.status_code)
data = result.json()
merged = data['paid'] + data['free']

for jobjectArr in merged:
    a+=1
    if jobjectArr['confName'] != "":
        print ("Conference Name : ",jobjectArr['confName'])
    if jobjectArr['confStartDate'] != "":
        print ("Conference Start Date : ",jobjectArr['confStartDate'])
    if jobjectArr['confEndDate'] != "":
        print ("Conference End Date : ",jobjectArr['confEndDate'])
    if jobjectArr['venue'] != "":
        print ("Venue : ",jobjectArr['venue'])
    if jobjectArr['city'] != "":
        print ("City : ",jobjectArr['city'])
    if jobjectArr['state'] != "":
        print ("State : ",jobjectArr['state'])
    if jobjectArr['country'] != "":
        print ("Country : ",jobjectArr['country'])
    if jobjectArr['entryType'] != "":
        print ("Entry Type : ",jobjectArr['entryType'])
    if jobjectArr['emailId'] != "":
        print ("Email ID : ",jobjectArr['emailId'])
    if jobjectArr['twitter_handle'] != "":
        print ("Twitter : ",jobjectArr['twitter_handle'])
    if jobjectArr['confUrl'] != "":
        print ("Conference URL : ",jobjectArr['confUrl'])
    if jobjectArr['confRegUrl'] != "":
        print ("Conference Registration URL : ",jobjectArr['confRegUrl'])
    print ()