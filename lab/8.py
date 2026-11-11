!pip install nltk scikit-learn
import nltk
from nltk.corpus import movie_reviews
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('movie_reviews')

X = [movie_reviews.raw(f) for f in movie_reviews.fileids()]
y = [movie_reviews.categories(f)[0] for f in movie_reviews.fileids()]

model = make_pipeline(TfidfVectorizer(stop_words='english'),
                      MultinomialNB())
model.fit(X, y)

for text in ["This movie is excellent", "This movie is terrible"]:
    print(text, ":", model.predict([text])[0].upper())