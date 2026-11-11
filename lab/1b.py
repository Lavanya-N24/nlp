import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Input text
text = "i am megha from cse"

# Tokenize text
words = word_tokenize(text)

# Create stopword set
stopword = set(stopwords.words('english'))

# Remove stopwords
filtered = []

for word in words:
    if word.lower() not in stopword:
        filtered.append(word)

print(filtered)