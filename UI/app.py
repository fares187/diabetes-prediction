# app.py
from flask import Flask, render_template, request, redirect, url_for
import joblib  
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('best_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Create dictionary of raw form values for display
    age_mapping = {
        '1': '18–24', '2': '25–29', '3': '30–34', '4': '35–39',
        '5': '40–44', '6': '45–49', '7': '50–54', '8': '55–59',
        '9': '60–64', '10': '65–69', '11': '70–74', '12': '75–79',
        '13': '80 or older'
    }

    form_data = {
        'General Health': request.form['GenHlth'],
        'High Blood Pressure': request.form['HighBP'],
        'BMI': request.form['BMI'],
        'Age Group': age_mapping[request.form['Age']],
        'High Cholesterol': request.form['HighChol'],
        'Difficulty Walking': request.form['DiffWalk'],
        'Heart Disease/Attack History': request.form['HeartDiseaseorAttack'],
        'Physical Health Days': request.form['PhysHlth']
    }

    # Convert to model input format
    features = [
        int(form_data['General Health']),
        1 if form_data['High Blood Pressure'] == 'True' else 0,
        float(form_data['BMI']),
        int(request.form['Age']),  # Use original value for model
        1 if form_data['High Cholesterol'] == 'True' else 0,
        1 if form_data['Difficulty Walking'] == 'True' else 0,
        1 if form_data['Heart Disease/Attack History'] == 'True' else 0,
        int(form_data['Physical Health Days'])
    ]

    prediction = model.predict([features])[0]
    result = "High Risk of Diabetes" if prediction == 1 else "Low Risk of Diabetes"
    
    return render_template('result.html', 
                         form_data=form_data,
                         prediction=result)

if __name__ == '__main__':
    app.run(debug=True)