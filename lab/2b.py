import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Automatically download required NLTK packages
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Input text
text = "The cats are chasing mice"
words = word_tokenize(text)
wnl = WordNetLemmatizer()

# Print results
print("original word -> Lemmatized word")
for word in words:
    print(f"{word} -> {wnl.lemmatize(word)}")