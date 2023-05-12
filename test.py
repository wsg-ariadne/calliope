import string
import random
import nltk
import pickle5 as pickle
import pandas as pd

df = pd.read_csv('data/combined_ms.csv')
data = df.to_numpy()

word_string = ''
documents = []

for point in data:
    curr_tuple = (point[0].translate(str.maketrans('', '', string.punctuation)).split(), point[1])
    documents.append(curr_tuple)
    word_string = word_string + point[0].translate(str.maketrans('', '', string.punctuation))

random.shuffle(documents)
# print(documents[0])

all_words = nltk.FreqDist(w.lower() for w in word_string.split())

word_features = list(all_words)[:5]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# Load pickled model:
calliope = pickle.load(open('calliope.pickle', 'rb'))

# Ask for text input to classify:
test_banner = input("Input browser banner text: ")

print("'"+ test_banner + "' is " + calliope.classify(document_features(test_banner.split())))