# TuneVibe
This is a Gradio web application for Sentiment Analysis using Random Forest model that has been trained to recognize emotions of text input. The model was trained using Scikit-learn, Spacy, and TfidfVectorizer.

# Installation

Clone the repository and navigate to the root folder:
```terminal
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

Create a virtual environment: 
```terminal
python3 -m venv venv
```

Activate the virtual environment:  
On Windows:  
```terminal
venv\Scripts\activate
```

On Linux or macOS:
```terminal
source venv/bin/activate
```

Install the dependencies: 
```terminal
pip install -r requirements.txt
```

# Usage
To run the application, navigate to the root folder and execute the following command:  
```terminal
python app.py
```
Then, open a web browser and go to http://localhost:5000/.
Write text in the text field and the application will predict the sentiment of your text using the pre-trained machine learning model.

# Files
* app.py: This is the Gradio web application that serves as the main entry point of the program. It uses the machine learning model to predict the sentiment of the input field.

* main.py: This is the Python script that trains the machine learning model using Scikit-learn, Spacy, and TfidfVectorizer.

* model.pkl: This is the pre-trained machine learning model.

* dataset: This directory contain the data used for training the model.

* requirements.txt: This is the text files which contains all the necessary dependencies with their versions.

# License
This project is protected by the MIT License. See the LICENSE file for more details.

# Credits
* This project was created by Utsav Acharya.
* The face recognition model was trained using kaggle dataset jp797498e/twitter-entity-sentiment-analysis.
* The Spacy, and TfidfVectorizer were used for data preprocessing, cleaning and feature engineering of the text.
* The Scikit-learn was used for model training.
* The Gradio web framework was used to create the web application.

 



