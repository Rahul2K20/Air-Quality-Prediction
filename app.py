from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('RF_model.pkl')

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
        SOi = float(request.form.get('so2'))
        Noi = float(request.form.get('no2'))
        Rpi = float(request.form.get('rspm'))
        SPmi = float(request.form.get('spm'))
        
        prediction = model.predict([[SOi, Noi, Rpi, SPmi]])
        output = prediction[0]

    except ValueError:
        return "Error: Please enter valid numbers for all fields", 400

    return render_template('result.html', prediction=output)
        

if __name__ == "__main__":
    app.run(debug=True)
