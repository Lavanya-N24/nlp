import nltk

# 1. Download the required packages
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

# 2. Use a grammatically correct sentence for accurate tagging
text = "The farmer grows healthy crops."

# 3. Process the text
words = word_tokenize(text)
taggedwords = pos_tag(words)

print("tagged output", taggedwords)