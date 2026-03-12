# BotTrainer Pro – Industry Level NLU Trainer

## Features
- Intent classification
- Entity extraction
- Model evaluation
- Confusion matrix
- Web interface

## Run Steps

1. Train the model
python src/train.py

2. Evaluate the model
python src/evaluate.py

3. Run the application
streamlit run src/app.py

## Example

Input:
book flight to Delhi

Output:
{
 "intent": "book_flight",
 "confidence": 0.97,
 "entities": {
   "location": "Delhi"
 }
}