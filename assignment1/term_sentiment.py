import sys
import re
import urllib
import json

dictMap = {}
excludedMap = {}
excludedCountMap = {}

def computeExcludedMap(fp):
    for line in fp.readlines(): 
        tweetObj = json.loads(line.encode("utf-8"))
        if "text" in tweetObj:
            tweetText = tweetObj["text"]
            words = tweetText.split()
            sentiment = 0.0
            for word in words:
                if word in dictMap:
                    sentiment += dictMap[word]
            for word in words:
                if word not in dictMap:
                    if word not in excludedMap:
                        excludedMap[word] = 0.0
                        excludedCountMap[word] = 0
                    excludedCountMap[word] += 1
                    excludedMap[word] += sentiment / (len(words) + 0.0)
                    
    for k,v in excludedCountMap.items(): # weighted
        excludedMap[k] = excludedMap[k] / v

def printExcludedMap():
   for k,v in excludedMap.items():
       if k != "":
           print "%s %.3f" % (k.encode("utf-8"), v)
    
def createDictionary(fp):
    lines = fp.readlines()
    
    for line in lines:
        chunks = line.split("\t")
        sentiment = re.sub(r"\n", "", chunks[1])
        subchunks = chunks[0].split(" ")
        for subchunk in subchunks:
            dictMap[subchunk] = int(sentiment)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    createDictionary(sent_file)
    computeExcludedMap(tweet_file)
    printExcludedMap()

if __name__ == '__main__':
    main()
