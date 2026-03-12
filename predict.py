import pickle
import json
from entity_extractor import extract_entities

model = pickle.load(open("models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict(text):

    vector = vectorizer.transform([text])

    intent = model.predict(vector)[0]

    confidence = max(model.predict_proba(vector)[0])

    entities = extract_entities(text)

    result = {
        "intent": intent,
        "confidence": float(confidence),
        "entities": entities
    }

    return result

if __name__ == "__main__":

    text = input("Enter message: ")

    result = predict(text)

    print(json.dumps(result, indent=2))