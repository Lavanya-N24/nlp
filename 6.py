# 1. Install Stanza if not already installed
!pip install stanza

import stanza

# 2. Download and initialize Stanza pipeline for English
stanza.download("en")
nlp = stanza.Pipeline("en")

# 3. Input text
text = "narendra modi visited bengaluru"

# 4. Process text
doc = nlp(text)

# 5. Print tokens, lemmas, and POS tags (fixed 'lema' to 'lemma')
print("Tokens, Lemmas, and POS Tags:")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text} -> {word.lemma} -> {word.upos}")

# 6. Print Named Entities
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text} [{ent.type}]")