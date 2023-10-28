from flask import jsonify, Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://ipsita:Ipsita%402023@uk-bd0.u3pngqk.mongodb.net/airbnb"
try:
    mongo = PyMongo(app)
    print("____________________connection successfull____________________________")

except Exception as e:
    print(f"error________________{e}")


def get_data():
    question_ans = []
    print("11111111111111111111111111111111111111111111111111111111111111111")
    collection = mongo.db.chatbot_question_ans
    print("22222222222222222222222222222222222222222222222222222222222222")
    data = list(collection.find({}))
    print(data)
    print("3333333333333333333333333333333333333333333333333333333333333333333333333")
    for item in data:
        question_ans.append(
            {"question": item["question"], "answer": item["answer"]})

    print(question_ans)
    return {"train_data": question_ans}


# get_data()

# if __name__ == "__main__":
#     app.run(debug=True)
