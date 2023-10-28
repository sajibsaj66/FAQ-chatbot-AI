import re
import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chat_bot_train import word_tokenize_dash_remove_lemmatize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import joblib
from flask import Flask, request, jsonify
from chat_bot_train import chat_bot_train
from flask_cors import CORS


def retrieve_predefined_answer(user_query):
    with open("predefined_data.json", "r") as json_data:
        predefined_data = json.load(json_data)
    tfidf_matrix = joblib.load("tfidf_matrix.pkl")
    tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
    user_query_vector = tfidf_vectorizer.transform([user_query])
    similarity_scores = cosine_similarity(user_query_vector, tfidf_matrix)
    best_match_index = similarity_scores.argmax()
    # return best_match_index
    return predefined_data[best_match_index]["answer"]


def chat_with_chatbot(user_query):
    user_query = word_tokenize_dash_remove_lemmatize(user_query)
    predefined_answer = retrieve_predefined_answer(user_query)

    # Check if the predefined answer is sufficient

    if predefined_answer:
        print(predefined_answer)  # ///////////////////////
        return predefined_answer
    else:
        # gpt3_response = generate_gpt3_response(user_query)
        return "I don't have the answer"


# chat_with_chatbot(input("text:"))
