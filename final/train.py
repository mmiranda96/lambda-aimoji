import unidecode
from nltk import LancasterStemmer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity, stopwords
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.tokenize import TweetTokenizer

# NLTK stuff
tweet_tokenizer = TweetTokenizer()
stopwords = sorted(stopwords.words('spanish') + ['rt'])
stemmer = LancasterStemmer()

# Regex stuff
regex_url = re.compile('((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?')
regex_ht_mn = re.compile('(#|@)[\w]*')
regex_spaces = re.compile('[ ]+')
regex_nonword = re.compile('[\W]+')
regex_repeated_ch = re.compile(r'(\w*)(\w)\2(\w*)')
regex_ch = r'\1\2\3'

# Feature stuff
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def remove_repeated_chars(word):
    repl_word =	regex_repeated_ch.sub(regex_ch, word)
    if repl_word !=	word:
        return remove_repeated_chars(repl_word)
    else:
        return repl_word

# Tweet loading and cleaning
wrong = 0
with open('corpus.txt', 'r') as f:
    tweets = []
    for line in f.readlines():
        cols = line.replace('\n', '').replace('\ufeff', '').replace('\t', '').split('|')
        if len(cols) == 2:
            (cat, tweet) = (cols[0], cols[1])
            # Removal of URLs, hashtags and mentions
            tweet_regex = regex_spaces.sub(' ', regex_ht_mn.sub('', regex_url.sub('', tweet))).lower()
            # Removal of caps and accents
            tweet_raw = unidecode.unidecode(tweet_regex).lower()
            tokens = [
                remove_repeated_chars(stemmer.stem(t))
                for t in tweet_tokenizer.tokenize(tweet_regex) if not t in stopwords and not regex_nonword.match(t)
            ]
            tweets.append((tokens, cols[0]))
        else:
            wrong += 1
            print(line, end='')

print('Wrong: {0}'.format(wrong))
word_features = get_word_features(get_words_in_tweets(tweets))
tweets_cat = {
    'P': [t for t in tweets if t[1] == 'P'],
    'N': [t for t in tweets if t[1] == 'N'],
    'NEU': [t for t in tweets if t[1] == 'NEU']
}

# Splitting tweets by category between training and test sets
train_tweets, test_tweets = [], []
for (c, l) in tweets_cat.items():
    print('{0}: {1}'.format(c, len(l) / len(tweets)))
    y = int(len(l) / 3)
    x = len(l) - y
    train_tweets += l[:x]
    test_tweets += l[-y:]

print('Size of sets:')
print('Train: {0}'.format(len(train_tweets)))
print('Test: {0}'.format(len(test_tweets)))
print()

# Classifier training
trainer = NaiveBayesClassifier.train
sentim_analyzer = SentimentAnalyzer()

train_set = nltk.classify.apply_features(extract_features, train_tweets)
test_set = nltk.classify.apply_features(extract_features, test_tweets)
classifier = sentim_analyzer.train(trainer, train_set)

# Classifier validation
for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))

# Storing classifier and words
with open('aimoji.pickle', 'wb') as f:
    pickle.dump(classifier, f)

with open('words.txt', 'w') as f:
    for word in word_features:
        f.write(word + '\n')
