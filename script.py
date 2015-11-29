# LeTest
import csv
import urllib2
import operator

url = 'https://doc-00-98-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/0lat5cg6vv3cno0dndk2u41tnhmfb3m5/1448820000000/05954773286171151700/*/0B_3YihA4SQKVZGd5cEFCRmItNGM?e=download'
response = urllib2.urlopen(url)

import numpy as np

from collections import defaultdict

def dataCount(ownerCount,tagCount,openStatusCount,dateClosed,data):
    tag1NotUsed = 0
    tag2NotUsed = 0
    tag3NotUsed = 0
    tag4NotUsed = 0
    tag5NotUsed = 0
    for i in data:
        ownerCount[i['OwnerUserId']]+=1
        openStatusCount[i['OpenStatus']]+=1
        if i['Tag1'] != '':
            tagCount[i['Tag1']]+=1
        else:
            tag1NotUsed+=1
            
        if i['Tag2'] != '':
            tagCount[i['Tag2']]+=1
        else:
            tag2NotUsed+=1
            
        if i['Tag3'] != '':
            tagCount[i['Tag3']]+=1
        else:
            tag3NotUsed+=1
            
        if i['Tag4'] != '':
            tagCount[i['Tag4']]+=1
        else:
            tag4NotUsed+=1
        if i['Tag5'] != '':
            tagCount[i['Tag5']]+=1
        else:
            tag5NotUsed+=1

        if i['PostClosedDate']!='':
            dateClosed+=1
        
    dateClosed = dateClosed
    return (tag1NotUsed,tag2NotUsed,tag3NotUsed,tag4NotUsed,tag5NotUsed)

def parseCSVData(csvfile):
    data = []
    rowIndex = 0
    spamreader = csv.reader(csvfile, delimiter=',')
    rowNum = 0
    for row in spamreader:
        print "At Row Num:", rowNum
        rowNum+=1
        if rowIndex !=0:
            element = {}
            fieldnames = ("PostId","PostCreationDate","OwnerUserId","OwnerCreationDate","ReputationAtPostCreation","OwnerUndeletedAnswerCountAtPostTime","Title","BodyMarkdown","Tag1","Tag2","Tag3","Tag4","Tag5","PostClosedDate","OpenStatus")
            index = 0
            for i in row:
                element[fieldnames[index]] = i
                if index == 0 or index == 5 or index == 4:   
                    element[fieldnames[index]] = int(i)
                index +=1


            data.append(element)
        else:
            rowIndex = 1
    return data

data = parseCSVData(response)

print len(data)

ownerCount = defaultdict(int)
tagCount = defaultdict(int)
openStatusCount = defaultdict(int)
dateClosed = 0


tagNotUsed = dataCount(ownerCount,tagCount,openStatusCount,dateClosed,data)


sorted_x = sorted(tagCount.items(), key=operator.itemgetter(1))

sorted_x.reverse()
print(len(sorted_x))