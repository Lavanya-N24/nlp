
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

text = "Lav went to Paris"

words = word_tokenize(text)
taggedwords = pos_tag(words)

tree = ne_chunk(taggedwords)

print("Named Entity Tree:")
tree.pretty_print()
