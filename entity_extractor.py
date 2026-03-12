def extract_entities(text):

    entities = {}

    words = text.split()

    for word in words:

        if word.lower() in ["delhi", "mumbai"]:
            entities["location"] = word

        if word.lower() in ["pizza", "biryani"]:
            entities["food_item"] = word

    return entities