import streamlit as st
from predict import predict

st.set_page_config(page_title="BotTrainer Pro", layout="wide")

st.title("BotTrainer Pro – NLU Trainer & Evaluator")

user_input = st.text_input("Enter user message")

if user_input:

    result = predict(user_input)

    st.json(result)

    st.success("Intent: " + result["intent"])
    st.info("Confidence: " + str(result["confidence"]))