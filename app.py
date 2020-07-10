from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
# from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('Subs_model.pkl', 'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')
# standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        profiles=int(request.form['profiles'])
        cases=int(request.form['cases'])
        gender=request.form['gender']
        if(gender=='MALE'):
            gender=1
        else:
            gender=0
        # scaled = scaler.transform([[profiles,cases,gender,age]])
        prediction=model.predict([[profiles,cases,gender,age]]) 
        output=prediction[0]
        if output<1:
            return render_template('index.html',prediction_text="User will NOT buy subscription")
        else:
            return render_template('index.html',prediction_text="User will buy subscription")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

