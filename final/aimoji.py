import re
import unidecode
from nltk import LancasterStemmer
from nltk.corpus import stopwords
from nltk.sentiment.util import *
from nltk.tokenize import TweetTokenizer

# Regex stuff
regex_url = re.compile('((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?')
regex_ht_mn = re.compile('(#|@)[\w]*')
regex_spaces = re.compile('[ ]+')
regex_nonword = re.compile('[\W]+')
regex_repeated_ch = re.compile(r'(\w*)(\w)\2(\w*)')
regex_ch = r'\1\2\3'

# NLTK stuff
stopwords = sorted(stopwords.words('spanish') + ['rt'])
stemmer = LancasterStemmer()
tweet_tokenizer = TweetTokenizer()

# Tweet cleaning
def remove_repeated_chars(word):
    repl_word =	regex_repeated_ch.sub(regex_ch, word)
    if repl_word !=	word:
        return remove_repeated_chars(repl_word)
    else:
        return repl_word

def clean_tweet(tweet):
    return regex_spaces.sub(' ', regex_ht_mn.sub('', regex_url.sub('', tweet)))

def standarize_tweet(tweet):
    return unidecode.unidecode(tweet).lower()

def tokenize_tweet(tweet):
    return tweet_tokenizer.tokenize(tweet)

def clean_tokens(tokens):
    return [remove_repeated_chars(t) for t in tokens if not t in stopwords and not regex_nonword.match(t)]

def stem_tokens(tokens):
    return [stemmer.stem(t) for t in tokens]

def get_emojis(tweet):
    emojis = []
    for c in tweet:
        if c in emoji_dict.keys():
            emojis.append(c)
    return emojis

# Classifier stuff
with open('words.txt', 'r') as f:
    word_features = list(map(lambda x: x.replace('\n', ''), f.readlines()))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def guess(tokens):
    return classifier.prob_classify(extract_features(tokens))

try:
    with open("aimoji.pickle", "rb") as f:
        classifier = pickle.load(f)
except FileNotFoundError:
    print('Classifier not found. Exiting...')
    exit()

# Emoji algorithm
with open('emoji_dict.csv', 'r') as f:
    lines = map(lambda x: x.replace('\n', '').replace('\r', ''), f.readlines()[1:])
    emoji_dict = {
        l[0]: {
            'code': l[1],
            'category': l[2],
            'description': l[3],
            'emotion': l[4],
            'emotion_value': int(l[5]),
            'tone': l[6],
            'tone_value': int(l[7])
        } for l in map(lambda x: x.split(','), lines)
    }

emotion_list = ['Alegria', 'Tristeza', 'Ira', 'Asco', 'Miedo']
tone_list = ['Positivo', 'Negativo', 'Neutral']
def calculate_emotion(emojis):
    if not emojis:
        return None
    emotions = dict(zip(emotion_list, [0] * len(emotion_list)))
    for e in emojis:
        emotion = emoji_dict[e]['emotion']
        value = emoji_dict[e]['emotion_value']
        emotions[emotion] += value
    tot = 0
    for v in emotions.values():
        tot += v
    return {k: v / tot for (k, v) in emotions.items()}

def calculate_tone(emojis):
    if not emojis:
        return None
    tones = dict(zip(tone_list, [0] * len(tone_list)))
    for e in emojis:
        tone = emoji_dict[e]['tone']
        value = emoji_dict[e]['tone_value']
        tones[tone] += value
    tot = 0
    for v in tones.values():
        tot += v
    return {k: v / tot for (k, v) in tones.items()}

# Detailed run
tweet = input('Inserte un twit a analizar: ')
emojis = get_emojis(tweet)
print('Emojis encontrados en el texto: {0}\n'.format(emojis))
clean_tweet = clean_tweet(tweet)
print('Twit limpio de URLs, hashtags y menciones: {0}\n'.format(clean_tweet))
standarized_tweet = standarize_tweet(clean_tweet)
print('Twit sin acentos y en minúsculas: {0}\n'.format(standarized_tweet))
tokenized_tweet = tokenize_tweet(standarized_tweet)
print('Twit tokenizado: {0}\n'.format(tokenized_tweet))
clean_tokens = clean_tokens(tokenized_tweet)
print('Tokens limpios: {0}\n'.format(clean_tokens))
stemmed_tokens = stem_tokens(clean_tokens)
print('Tokens raiz: {0}\n'.format(stemmed_tokens))
guess = guess(clean_tokens)
print('Resultado del algoritmo de texto:')
for s in guess.samples():
    print('{0}: {1}'.format(s, guess.prob(s)))
print()
emotion = calculate_emotion(emojis)
print('Resultado de emociones en emojis:')
if emotion:
    for (k, v) in emotion.items():
        print('{0}: {1}'.format(k, v))
else:
    print('N/A')
print()
tone = calculate_tone(emojis)
print('Resultado de tono en emojis:')
if tone:
    for (k, v) in tone.items():
        print('{0}: {1}'.format(k, v))
else:
    print('N/A')
