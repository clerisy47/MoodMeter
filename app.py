import joblib 
import numpy as np
import spacy
import gradio as gr

nlp = spacy.load("en_core_web_lg") 

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


def predict(text):
    preprocessed_text = preprocess(text)
    pred_value = model.predict([preprocessed_text])
    pred = key_from_value(emotion_class, pred_value)
    message = f"You are feeling {pred}"
    return message

interface = gr.Interface(fn=predict, 
                     inputs="text", 
                     outputs="text", 
                     title="Sentiment Analysis",
                     description="Enter a text and get its sentiment polarity.")
interface.launch()
