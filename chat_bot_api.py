
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import joblib
from flask import Flask, request, jsonify
from chat_bot_train import chat_bot_train
from flask_cors import CORS
from chat_bot import chat_with_chatbot
from mongodb_connection import get_data, app


@app.route("/chat_bot_train", methods=["GET"])
def train():
    question_ans_json = get_data()
    # question_ans_json = predefined_data  # /////////////
    if "train_data" in question_ans_json:  # nedd better check
        chat_bot_train(question_ans_json["train_data"])
        print("_____________chatbot train_______________")
        return jsonify({"response": "chat bot trained"}), 200


@app.route("/chat_bot", methods=["POST"])
def chat():
    user_query = request.json

    if "text" not in user_query or not isinstance(user_query, dict):
        return jsonify({"error": "Invalid inpu format"}), 400
    else:
        predefined_answer = chat_with_chatbot(user_query["text"])
        print("_______________chatbot response_______________")
        return jsonify({"response": predefined_answer}), 200


if __name__ == "__main__":
    app.run(debug=True)
