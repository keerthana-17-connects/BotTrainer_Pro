# 🤖 BotTrainer Pro
### Intelligent NLU Trainer & Chatbot Evaluation Platform

BotTrainer Pro is a Natural Language Understanding (NLU) training and evaluation system that detects user intent and extracts entities from text using Machine Learning. It includes a Streamlit dashboard for testing chatbot responses interactively.

--------------------------------------------------

📊 BotTrainer Dashboard

The project provides an interactive web dashboard built with Streamlit.

The dashboard allows users to:
• Enter a message
• Predict the intent
• Extract entities
• View confidence scores
• Test chatbot training data easily

Access the dashboard after running the application:

http://localhost:8501

--------------------------------------------------

🔁 System Pipeline

User Input
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Logistic Regression Model
   ↓
Intent Prediction
   ↓
Entity Extraction
   ↓
Streamlit Dashboard Output

This pipeline converts raw user messages into structured chatbot understanding.

--------------------------------------------------

📂 Project Architecture

BotTrainer_Pro

│
├── data  
│   └── intents.json  (training dataset)

│
├── models  
│   ├── intent_model.pkl  (trained ML model)  
│   └── vectorizer.pkl  (TF-IDF vectorizer)

│
├── src  
│   ├── train.py  (model training script)  
│   ├── predict.py  (intent prediction logic)  
│   ├── entity_extractor.py  (extracts entities like location or food item)  
│   ├── evaluate.py  (model evaluation metrics)  
│   └── app.py  (Streamlit web dashboard)

│
├── requirements.txt  (project dependencies)  
└── README.md  (project documentation)

--------------------------------------------------

⚡ Quick Start Guide

1️⃣ Install dependencies

pip install -r requirements.txt


2️⃣ Train the model

python src/train.py


3️⃣ Evaluate model performance

python src/evaluate.py


4️⃣ Launch the dashboard

streamlit run src/app.py


Then open:

http://localhost:8501

--------------------------------------------------

🌟 Key Features

• Intent classification  
• Entity extraction  
• Confidence scoring  
• Model evaluation metrics  
• Interactive chatbot testing dashboard  

--------------------------------------------------

🧪 Example Prediction

Input

I want to fly to Mumbai


Output

{
 "intent": "book_flight",
 "confidence": 0.51,
 "entities": {
   "location": "Mumbai"
 }
}

--------------------------------------------------

🛠 Technology Stack

Python  
Scikit-learn  
TF-IDF Vectorizer  
Logistic Regression  
Streamlit  

--------------------------------------------------

👩‍💻 Author

Keerthana
