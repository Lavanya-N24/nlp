import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Download the required NLTK stop words data
nltk.download('stopwords')

# Sample documents from the lab notebook
documents = [
    "This is a good book",
    "This is a good pen",
    "I like this book"
]

# Load English stop words
stop_words = stopwords.words('english')

# Initialize the TF-IDF Vectorizer with stop words
vectorizer = TfidfVectorizer(stop_words=stop_words)

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()

# Print results
print("Terms:", feature_names)
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())