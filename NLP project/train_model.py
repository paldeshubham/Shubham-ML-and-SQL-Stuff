import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Download NLTK stopwords
nltk.download("stopwords")

# Properly Balanced Dataset with more neutral examples
data = {
    "text": [
        "I love this product!", "This is the worst thing ever.",
        "Amazing experience!", "I hate this so much!",
        "Best service I've ever used.", "Not great, not terrible.",
        "Really bad quality.", "Absolutely fantastic!",
        "I feel great about this.", "This was an awful purchase.",
        "I am very satisfied.", "This was a terrible decision.",
        "Superb quality!", "Totally disappointing.",
        "Very happy with the result.", "Absolutely dreadful service.",
        "This is fantastic!", "I don't like this at all.",
        "I’m in love with this product!", "Worst experience ever!",
        "It's okay", "Not bad, not great", "Could be better", "Neither good nor bad",
        "I'm indifferent about this", "Average experience", "It’s fine", "Nothing special"
    ],
    "label": [
        "Positive", "Negative", "Positive", "Negative", "Positive", "Neutral",
        "Negative", "Positive", "Positive", "Negative", "Positive", "Negative",
        "Positive", "Negative", "Positive", "Negative", "Positive", "Negative",
        "Positive", "Negative", "Neutral", "Neutral", "Neutral", "Neutral",
        "Neutral", "Neutral", "Neutral", "Neutral"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Text Preprocessing Function
def preprocess_text(text):
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stopwords.words("english")]
    return " ".join(text)

df["text"] = df["text"].apply(preprocess_text)

# Splitting data into training and testing
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Logistic Regression Model
model = LogisticRegression(max_iter=500)
model.fit(X_train_tfidf, y_train)

# Save the model and vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved successfully!")

# Function to Predict Sentiment
def predict_sentiment(text):
    text = preprocess_text(text)
    text_tfidf = vectorizer.transform([text])

    # Get the model prediction
    return model.predict(text_tfidf)[0]

# Example Test Cases
test_sentences = [
    "I am unsatisfied", "I hate this!", "I love it!", "It's okay", "Not bad, not great."
]

for sentence in test_sentences:
    print(f"Text: {sentence} -> Sentiment: {predict_sentiment(sentence)}")
