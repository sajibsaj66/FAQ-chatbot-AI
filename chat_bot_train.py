import re
import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import joblib
from train_question_ans import trian_data


def word_tokenize_dash_remove_lemmatize(sentence):
    lemmatizer = WordNetLemmatizer()
    lst_words = []
    sentence = sentence.casefold()
    words = word_tokenize(sentence)
    # print(f"tokenize---------{words}")
    lst = []
    for word in words:
        t = re.split(r'[-]', word)
        for i in t:
            lst.append(i)
    # print(f"split----------{lst}")
    for i in lst:
        lst_words.append(lemmatizer.lemmatize(i))

    # print(f"lemmatize----------{lst_words}")
    return ''.join(i+" " for i in lst_words)


def chat_bot_train(predefined_data):
    # predefined_data = trian_data

    with open("predefined_data.json", "w") as json_data:
        json.dump(predefined_data, json_data)

    for i, record in enumerate(predefined_data):
        predefined_data[i]["question"] = word_tokenize_dash_remove_lemmatize(
            record["question"])
        # predefined_data[i]["answer"] = word_tokenize_dash_remove_lemmatize(
        #     record["answer"])

    # print(predefined_data)  # //////////////////////////////////////////////////

    tfidf_vectorizer = TfidfVectorizer()

    # Train the vectorizer on predefined questions
    predefined_questions = [item["question"] for item in predefined_data]
    tfidf_matrix = tfidf_vectorizer.fit_transform(predefined_questions)
    # print(f"tfidf vectorizer--------{tfidf_matrix}")
    joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")
    joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
    print("__________training finished__________")

    # Function to retrieve a predefined answer


# chat_bot_train("")  # ///////////////////////////////////////
