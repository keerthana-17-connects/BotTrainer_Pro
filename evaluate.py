import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

model = pickle.load(open("models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

test_data = [
    "book flight to Delhi",
    "order pizza",
    "weather today"
]

actual = [
    "book_flight",
    "order_food",
    "check_weather"
]

X_test = vectorizer.transform(test_data)

predicted = model.predict(X_test)

print("Accuracy:", accuracy_score(actual, predicted))
print("Precision:", precision_score(actual, predicted, average="weighted"))
print("Recall:", recall_score(actual, predicted, average="weighted"))
print("F1 Score:", f1_score(actual, predicted, average="weighted"))

print("Confusion Matrix:")
print(confusion_matrix(actual, predicted))