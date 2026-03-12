import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
with open("data/intents.json") as f:
    data = json.load(f)

X = []
y = []

for intent in data["intents"]:
    for example in intent["examples"]:
        X.append(example)
        y.append(intent["name"])

# Vectorization
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vector, y)

# Save model
pickle.dump(model, open("models/intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("Model trained successfully")