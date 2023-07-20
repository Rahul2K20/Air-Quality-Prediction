from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('RF_model.pkl')


def calculate_index(val, breakpoints):
    for bp in breakpoints:
        if val <= bp[0]:
            return bp[1] * val / bp[0]
        elif val <= bp[2]:
            return bp[1] + (val - bp[0]) * (bp[3] - bp[1]) / (bp[2] - bp[0])

def calculate_aqi(si, ni, rspmi, spmi):
    return max(si, ni, rspmi, spmi)

# Define breakpoints
breakpoints_so2 = [(40, 50, 80, 100), (80, 100, 380, 200), (380, 200, 800, 300), (800, 300, 1600, 400), (1600, 400, float('inf'), 500)]
breakpoints_no2 = [(40, 50, 80, 100), (80, 100, 180, 200), (180, 200, 280, 300), (280, 300, 400, 400), (400, 400, float('inf'), 500)]
breakpoints_rspm = [(30, 50, 60, 100), (60, 100, 90, 200), (90, 200, 120, 300), (120, 300, 250, 400), (250, 400, float('inf'), 500)]
breakpoints_spm = [(50, 50, 100, 100), (100, 100, 250, 200), (250, 200, 350, 300), (350, 300, 430, 400), (430, 400, float('inf'), 500)]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        # Get the data from the POST request
        so2 = float(request.form.get('so2'))
        no2 = float(request.form.get('no2'))
        rspm = float(request.form.get('rspm'))
        spm = float(request.form.get('spm'))

        # Convert raw pollutant measures to AQI values
        SOi = calculate_index(so2, breakpoints_so2)
        Noi = calculate_index(no2, breakpoints_no2)
        Rpi = calculate_index(rspm, breakpoints_rspm)
        SPmi = calculate_index(spm, breakpoints_spm)

        # Make prediction using the model loaded from disk as per the data
        prediction = model.predict([[SOi, Noi, Rpi, SPmi]])

        output = prediction[0]

    except ValueError:
        return jsonify("Error: Please enter valid numbers for all fields"), 400

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
