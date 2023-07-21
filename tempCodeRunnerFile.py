from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('RF_model.pkl')

breakpoints_so2 = [(40, 50, 80, 100), (80, 100, 380, 150), (380, 150, 800, 200), (800, 200, 1600, 300), (1600, 300, 2100, 400), (2100, 400, 2620, 500)]
breakpoints_no2 = [(40, 50, 80, 100), (80, 100, 180, 150), (180, 150, 280, 200), (280, 200, 400, 300), (400, 300, 800, 400), (800, 400, 1000, 500)]
breakpoints_rspm = [(50, 50, 100, 100), (100, 100, 250, 150), (250, 150, 350, 200), (350, 200, 420, 300), (420, 300, 520, 400), (520, 400, 620, 500)]
breakpoints_spm = [(50, 50, 100, 100), (100, 100, 250, 150), (250, 150, 350, 200), (350, 200, 430, 300), (430, 300, 530, 400), (530, 400, 630, 500)]


def calculate_index(val, breakpoints):
    for bp in breakpoints:
        if val <= bp[0]:
            return bp[1] * val / bp[0]
        elif val <= bp[2]:
            return bp[1] + (val - bp[0]) * (bp[3] - bp[1]) / (bp[2] - bp[0])
    return bp[3] + (val - bp[2]) * (500 - bp[3]) / (bp[4] - bp[2])

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

        # Make prediction 
        prediction = model.predict([[SOi, Noi, Rpi, SPmi]])

      
        output = prediction[0]

    except ValueError:
        return "Error: Please enter valid numbers for all fields", 400

   
    if output <= 50:
        category = 'Good (Air quality is satisfactory and poses little or no risk)'
    elif output <= 100:
        category = 'Moderate (Air quality is acceptable, but there may be a risk for some people, particularly those who are unusually sensitive to air pollution)'
    elif output <= 150:
        category = 'Unhealthy for Sensitive Groups (Members of sensitive groups may experience health effects, but the general public is unlikely to be affected)'
    elif output <= 200:
        category = 'Unhealthy (Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects)'
    elif output <= 300:
        category = 'Very Unhealthy (Health warnings of emergency conditions; the entire population is more likely to be affected)'
    else:
        category = 'Hazardous (Health alert: everyone may experience more serious health effects)'

    return render_template('result.html', aqi=output, category=category)

if __name__ == "__main__":
    app.run(debug=True)
