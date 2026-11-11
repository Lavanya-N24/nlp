import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the required models for tokenization
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Be yourself, because an original is worth more than a copy. by xyz"

# Sentence tokenization
t = sent_tokenize(text)
print("\n sentence tokenization")
for i, te in enumerate(t, 1):
    print(i, ":", te)

# Word tokenization
w = word_tokenize(text)
print("\n word tokenization")
for i, wo in enumerate(w, 1):
    print(i, ":", wo)
