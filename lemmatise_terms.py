# lemmatises all the terms
#
# pip install nltk & download corpora
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

words = []

with open('output/terms.txt') as f:
    for line in f:
        stemmed_concept = []

        for term in line.strip().lower().split(' '):
            stemmed_word = wordnet_lemmatizer.lemmatize(term)
            stemmed_concept.append(stemmed_word)

        words.append(' '.join(stemmed_concept))

f = open("output/lemmatised.txt", "w")
f.write("\n".join(words))
f.close()
