import sys
import re
import urllib
import json

dictMap = {}

def lines(fp):
    for line in fp.readlines(): 
        tweetObj = json.loads(line)
        if "text" in tweetObj:
            tweetText = tweetObj["text"]
            words = tweetText.split()
            sentiment = 0.0
            for word in words:
                if word in dictMap:
                    sentiment += dictMap[word]
            print sentiment

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

if __name__ == '__main__':
    main()
