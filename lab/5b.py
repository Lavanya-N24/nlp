from collections import Counter

# Define the text corpus
corpus = ["this is my dog", "this is my cat", "i love my cat"]

# Tokenize corpus into individual lowercase words
words = " ".join(corpus).lower().split()

# Create bigrams and calculate frequency counts
bigrams = list(zip(words, words[1:]))
bc = Counter(bigrams)
uc = Counter(words)

# Target sentence to evaluate
sentence = "this is my cat".split()

# Calculate bigram language model probability
p = 1.0
for a, b in zip(sentence, sentence[1:]):
    if uc[a] > 0:
        p *= bc[(a, b)] / uc[a]
    else:
        p = 0

print("probability =", p)