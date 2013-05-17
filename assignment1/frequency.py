import sys
import re
import urllib
import json

freqMap = {}

def computeFreqMap(fp):
    count = 0.0
    for line in fp.readlines(): 
        tweetObj = json.loads(line)
        if "text" in tweetObj:
            tweetText = tweetObj["text"]
            words = tweetText.split()
            for word in words:
                if word not in freqMap:
                    freqMap[word] = 0
                freqMap[word] += 1
                count += 1
                    
    for k,v in freqMap.items(): # weighted
        freqMap[k] = v / count

def printFreqMap():
   for k,v in freqMap.items():
       if k != "":
           print "{} {}".format(k.encode("UTF-8"), v)

def main():
    tweet_file = open(sys.argv[1])
    computeFreqMap(tweet_file)
    printFreqMap()

if __name__ == '__main__':
    main()
