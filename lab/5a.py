import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Download the required tokenizer resource
nltk.download('punkt')

# Input text
text = "Natural language processing"

# Tokenize text into words
words = word_tokenize(text)

# Generate and print 1-grams (Unigrams), 2-grams (Bigrams), and 3-grams (Trigrams)
for i in range(1, 4):
    print("\n", i, "-grams:")
    gram = ngrams(words, i)
    for g in gram:
        print(g)
