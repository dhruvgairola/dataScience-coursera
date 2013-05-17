import sys
import re
import urllib
import json
import operator

hashtagMap = {}

def calcTopHashtags(fp):
    for line in fp.readlines(): 
        tweetObj = json.loads(line)
        if "entities" in tweetObj:
            entity = tweetObj["entities"]
            if "hashtags" in entity:
                hashtags = entity["hashtags"]
                for hashtag in hashtags:
                    htag = hashtag["text"]
                    if htag not in hashtagMap:
                        hashtagMap[htag] = 0
                    hashtagMap[htag] += 1

def main():
    tweet_file = open(sys.argv[1])
    calcTopHashtags(tweet_file)
    sorted_x = sorted(hashtagMap.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, 10):
        print "%s %i" % (sorted_x[i][0].encode("utf-8"), sorted_x[i][1])

if __name__ == '__main__':
    main()
