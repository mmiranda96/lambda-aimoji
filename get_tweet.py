import json
import codecs
import re

file = open("anasoclash_short.json","r")
# file1 = open("tweetsPablo.txt","w")
file1 = codecs.open("anasoclashtweets.txt", "w", "utf-8")
file1.write(u'\ufeff')
j = json.load(file)
for tweet in j:
	# file1.write(tweet['text'])
	file1.write(re.sub('\n','',tweet['text'])) 
	file1.write('\n')
# file.close()