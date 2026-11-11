from collections import Counter
import nltk
from nltk.corpus import reuters, stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download(['stopwords', 'reuters', 'punkt', 'punkt_tab'], quiet=True)

stop_words = set(stopwords.words('english'))
docs = [reuters.raw(fid) for fid in reuters.fileids()[:100]]

def stopword_frequency(documents):
    tokens = [w for doc in documents for w in nltk.word_tokenize(doc.lower()) if w in stop_words]
    return Counter(tokens)

def compute_tf_idf(documents):
    vec = TfidfVectorizer(stop_words='english')
    scores = vec.fit_transform(documents)[0].toarray()[0]
    return sorted(zip(vec.get_feature_names_out(), scores), key=lambda x: x[1], reverse=True)

print("Most Frequent Stopwords:", stopword_frequency(docs).most_common(10))
print("\nTop 10 TF-IDF Words in First Document:", compute_tf_idf(docs)[:10])