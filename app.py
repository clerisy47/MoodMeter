import joblib 
from flask import Flask, request, render_template
import numpy as np
import spacy

nlp = spacy.load("en_core_web_lg") 

flask_app = Flask(__name__)

class_names = ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy']
model = joblib.load('model1.pkl')

emotion_class = {'anger':0, 'sadness':1, 'fear':2, 'surprise':3, 'joy':4, 'love':5}

def preprocess(text):
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens) 

def key_from_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    text = request.form['input-text']
    preprocessed_text = preprocess(text)
    pred_value = model.predict([preprocessed_text])
    pred = key_from_value(emotion_class, pred_value)
    message = f"You are feeling {pred}"
    return render_template("index.html", message=message)



if __name__ == "__main__":
    flask_app.run(debug=True)
