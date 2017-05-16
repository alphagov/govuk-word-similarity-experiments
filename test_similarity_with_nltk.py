# pip install nltk & download corpora
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

words = []

with open('output/terms.txt') as f:
    for line in f:
        raw_term = line.strip().lower()
        stemmed_word = wordnet_lemmatizer.lemmatize(raw_term)
        if raw_term != stemmed_word:
            print raw_term + ': ' + stemmed_word

        words.append(stemmed_word)

boating = wn.synset('boating.n.01')

for word in words:
    concept = wn.synset(word + '.n.01')
    print 'boating vs ' + word + ': ' + boating.lch_similarity(concept)
