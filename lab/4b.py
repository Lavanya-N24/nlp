import nltk

# Define the Context-Free Grammar (CFG)
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'mat'
Adj -> 'big' | 'small'
V -> 'chased' | 'saw'
""")

# Input sentence
sentence = "the cat chased the dog"
words = sentence.split()

# Initialize the chart parser
parser = nltk.ChartParser(grammar)

# Parse and print the structure
for tree in parser.parse(words):
    print(tree)
    # Inside the loop to print the visual diagram for every valid parse tree
    tree.pretty_print() 