import nltk
# Download the required tokenizer models
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "I am watching bigboss kannada 13"
words = word_tokenize(text)
ps = PorterStemmer()

print("original word -> Stemmed word")
for word in words:
    print(word, "->", ps.stem(word))