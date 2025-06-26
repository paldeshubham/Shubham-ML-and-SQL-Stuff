from flask import Flask, request, render_template
import joblib

# Load trained ML model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]  # Get user input
        transformed_text = vectorizer.transform([text])  # Convert to numerical form
        sentiment = model.predict(transformed_text)[0]  # Predict sentiment

    return render_template("sentiment.html", sentiment=sentiment)


if __name__ == "__main__":
    app.run(debug=True)
