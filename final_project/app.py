import streamlit as st
import pandas as pd
import joblib
from src.preprocessing import preprocess_text

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

#dataset review
st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Dataset Statistics")

#display basic statistics
st.write("Number of responses:", len(df))
st.write(df["Sentiment"].value_counts())
sentiment_counts = df["Sentiment"].value_counts()
st.bar_chart(sentiment_counts)

#model performance
st.subheader("Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "90%")
    st.metric("Macro Precision", "0.88")

with col2:
    st.metric("Macro Recall", "0.85")
    st.metric("Macro F1-score", "0.87")

#user input
user_input = st.text_area(
    "Enter your feedback:"
)

if st.button("Predict Sentiment"):

    if user_input.strip():
        with st.spinner("Analyzing sentiment..."):
            processed = preprocess_text(user_input)
            vector = vectorizer.transform([processed])
            prediction = model.predict(vector)

        st.success(f"Predicted Sentiment: {prediction[0]}")
    else:
        st.warning("Please enter some feedback.")
