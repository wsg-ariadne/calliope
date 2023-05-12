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

# Train Naive Bayes classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[80:], featuresets[:80]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Test the classifier
print("Classifier accuracy rate: ",(nltk.classify.accuracy(classifier, test_set))*100)

# Show the most important features as interpreted by Naive Bayes
# classifier.show_most_informative_features(5)

# Pickling works
save_classifier = open('new_calliope.pickle', 'wb')
pickle.dump(classifier, save_classifier) 
save_classifier.close()

# This is how it's used
calliope = pickle.load(open('new_calliope.pickle', 'rb'))
test_banner = data[random.randint(0,20)][0]
print("'"+ test_banner + "' is " + calliope.classify(document_features(test_banner.split())))