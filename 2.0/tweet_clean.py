import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

# NLTK stuff
stopwords = sorted(stopwords.words('spanish') + ['rt'])
tweet_tokenizer = TweetTokenizer()

# Regex
regex_url = '((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?'
regex_ht_mn = '(#|@)[\w]*'
regex_sp = '[ ]+'
regex_nw = '[\W]+'

# Emojis
with open('emoji_dict.csv', 'r') as f:
    emoji_list = [l[0] for l in map(lambda x: x.split(','), f.readlines())]

# Tweet cleaning
def get_emojis(tweet):
    emojis = []
    for c in tweet:
        if c in emoji_list:
            emojis.append(c)
    return emojis

def clean_tweet(tweet):
    tweet_regex = re.sub(regex_sp, ' ', re.sub(regex_ht_mn, '', re.sub(regex_url, '', tweet)))
    words = tweet_tokenizer.tokenize(tweet_regex)
    clean_words = [w.lower() for w in words if w.lower() not in stopwords and not re.match(regex_nw, w)]
    return clean_words, get_emojis(tweet)

with open('tweets.txt', 'r') as f:
    tweets = map(lambda x: x.replace('\n', ''), f.readlines())

clean_tweets_file = open('clean.txt', 'w')
tweets_emojis_file = open('emojis.txt', 'w')

clean_tweets = map(clean_tweet, tweets)

for tweet, emojis in clean_tweets:
    if tweet:
        line = ''
        for word in tweet:
            line += word + ' '
        clean_tweets_file.write(line[:-1] + '\n')
    if emojis:
        line = ''
        for e in emojis:
            line += e + ' '
        tweets_emojis_file.write(line[:-1] + '\n')

clean_tweets_file.close()
tweets_emojis_file.close()
