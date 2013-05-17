import sys
import re
import urllib
import json

dictMap = {}
stateSentMap = {}
stateCountMap = {}

def lines(fp):
    for line in fp.readlines(): 
        tweetObj = json.loads(line)
#        print tweetObj.keys()
        if "place" in tweetObj:
            tweetPlace = tweetObj["place"]
            if tweetPlace is not None:
                if tweetPlace["country_code"] == "US" or tweetPlace["country"] == "United States":
                    if tweetPlace["full_name"] is not None:
                        state = tweetPlace["full_name"].split(",")
                        # Get sentiment
                        if "text" in tweetObj:
                            tweetText = tweetObj["text"]
                            words = tweetText.split()
                            sentiment = 0.0
                            for word in words:
                                if word in dictMap:
                                    sentiment += dictMap[word]
                            if state[1].strip() not in stateSentMap:
                                stateSentMap[state[1].strip()] = 0.0
                                stateCountMap[state[1].strip()] = 0
                            stateSentMap[state[1].strip()] += sentiment
                            stateCountMap[state[1].strip()] += 1
    
    for k,v in stateCountMap.items(): # weighted
        stateSentMap[k] = stateSentMap[k] / v        
#        if "text" in tweetObj:
#            tweetText = tweetObj["text"]
#            words = tweetText.split(" ")
#            sentiment = 0.0
#            for word in words:
#                if word in dictMap:
#                    sentiment += dictMap[word]
#            print sentiment

def printHappiestState():
    happiest = 0.0
    state = ""
    for k,v in stateSentMap.items():
        if k != "":
            if v > happiest:
                happiest = v
                state = k
    print state
           
def createDictionary(fp):
    lines = fp.readlines()
    
    for line in lines:
        chunks = line.split("\t")
        sentiment = re.sub(r"\n", "", chunks[1])
        dictMap[chunks[0]] = int(sentiment)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    createDictionary(sent_file)
    lines(tweet_file)
    printHappiestState()

if __name__ == '__main__':
    main()
