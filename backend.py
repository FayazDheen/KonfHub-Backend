import requests
import json
from pprint import pprint

result = requests.get(
    'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')

# print(result.status_code)

data = result.json()
# pprint(data)

# print (data)

merged = data['paid'] + data['free']
# print (merged)
# for pad in data['free']:
#     for each in pad:
#         print(each)
#     print()
# a = 0
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

# print(type(merged))
# print(a)
# l = merged

# l = [{'emailId': '', 'city': '', 'twitter_handle': '', 'keywordSupport': ' Artificial Intelligence ,Machine Learning,Cloud', 'country': '', 'imageURL': 'https://storage.googleapis.com/konfhub-bd9c9.appspot.com/54497.jpg?Expires=4733103270&GoogleAccessId=firebase-adminsdk-r3qh4%40konfhub-bd9c9.iam.gserviceaccount.com&Signature=GSihzq4Vf8koeEGcawKXeQmwT%2FQLZhooWUS%2BqJeNtPXtJqnNfky%2F5RgeOTEWKYCEjqAGFLSEx02cCdZ8CBTO7T2HlMjAZl6yTmDRMTH5mNawUHOrxqjsiNzSwCj4KLqHo8KlEqQrgE%2FTbxmWpT28zKfoOS20C88HrDXFMELmj5aHi4f0V%2BTF30rIlQJkNlFy6fkko2ipkLLxtYOMh0i%2B0tV1vZ0gI21mlpyNzfn6hC%2BGtN1BIz4BciB4IpMkkw7FUydFbXwJOVNm2FJs9AafozJdwdy0gOCtFDrMB2wY8JiPL2oSa%2BkBFlhIgjnIg3LaCPlfj%2Bqn9FTT%2FP5TrOioSg%3D%3D', 'venue': 'Online', 'searchTerms': ' AWS Innovate Online Conference, Artificial Intelligence ,Machine Learning,Cloud, Online, February, Free, 1579503272, India', 'confName': 'AWS Innovate Online Conference', 'state': '', 'long': '', 'confEndDate': '19 Feb, 2020', 'conference_id': 1579503272, 'lat': '', 'user_id': '1578287153', 'confUrl': 'https://aws.amazon.com/events/aws-innovate/machine-learning/', 'confStartDate': '19 Feb, 2020', 'entryType': 'Free', 'confRegUrl': 'https://aws.amazon.com/events/aws-innovate/machine-learning/'},
#      {'emailId': '', 'city': '', 'twitter_handle': '', 'keywordSupport': ' Artificial Intelligence ,Machine Learning,Cloud', 'country': '', 'imageURL': 'https://storage.googleapis.com/konfhub-bd9c9.appspot.com/54497.jpg?Expires=4733103270&GoogleAccessId=firebase-adminsdk-r3qh4%40konfhub-bd9c9.iam.gserviceaccount.com&Signature=GSihzq4Vf8koeEGcawKXeQmwT%2FQLZhooWUS%2BqJeNtPXtJqnNfky%2F5RgeOTEWKYCEjqAGFLSEx02cCdZ8CBTO7T2HlMjAZl6yTmDRMTH5mNawUHOrxqjsiNzSwCj4KLqHo8KlEqQrgE%2FTbxmWpT28zKfoOS20C88HrDXFMELmj5aHi4f0V%2BTF30rIlQJkNlFy6fkko2ipkLLxtYOMh0i%2B0tV1vZ0gI21mlpyNzfn6hC%2BGtN1BIz4BciB4IpMkkw7FUydFbXwJOVNm2FJs9AafozJdwdy0gOCtFDrMB2wY8JiPL2oSa%2BkBFlhIgjnIg3LaCPlfj%2Bqn9FTT%2FP5TrOioSg%3D%3D', 'venue': 'Online', 'searchTerms': ' AWS Innovate Online Conference, Artificial Intelligence ,Machine Learning,Cloud, Online, February, Free, 1579503272, India', 'confName': 'AWS Innovate Online Conference', 'state': '', 'long': '', 'confEndDate': '19 Feb, 2020', 'conference_id': 1579503272, 'lat': '', 'user_id': '1578287153', 'confUrl': 'https://aws.amazon.com/events/aws-innovate/machine-learning/', 'confStartDate': '19 Feb, 2020', 'entryType': 'Free', 'confRegUrl': 'https://aws.amazon.com/events/aws-innovate/machine-learning/'}]
# seen = set()
# nonDupList = []

# for d in l:
#     t = tuple(d.items())
#     if t not in seen:
#         a += 1
#         seen.add(t)
#         nonDupList.append(d)

# dat = data['free']  
# def remove_dupe_dicts(l):
#   list_of_strings = [
#     json.dumps(d, sort_keys=True)
#     for d in l
#   ]
#   list_of_strings = set(list_of_strings)
#   return [
#     json.loads(s)
#     for s in list_of_strings
#   ]   

# print(remove_dupe_dicts(dat))\