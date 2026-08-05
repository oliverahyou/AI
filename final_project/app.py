import streamlit as st
import pandas as pd
import joblib

#loading models
model = joblib.load("./models/linear_svm_model.pkl")
vectorizer = joblib.load("./models/tfidf_vectorizer.pkl")

#loading dataset
df = pd.read_csv("./data/processed/lemmatized_reviews_sentiment.csv")

#app title
st.title("Coffee Customer Feedback Sentiment Analysis")
st.write(
    "This application predicts the sentiment of coffee customer feedback using TF-IDF and a Linear Support Vector Machine."
)

