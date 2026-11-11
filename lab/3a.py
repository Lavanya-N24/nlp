
import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The farmer grows healthy crops"
tagged = pos_tag(word_tokenize(text))
print("POS Tags:", tagged)

grammar = """
NP: {<DT>?<JJ>*<NN.*>}
VP: {<VB.*><NP>*}
"""
parser = RegexpParser(grammar)
tree = parser.parse(tagged)

print("\nChunk Tree:")
tree.pretty_print()
