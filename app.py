from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('RF_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:  
        SOi = float(request.form.get('so2'))
        Noi = float(request.form.get('no2'))
        Rpi = float(request.form.get('rspm'))
        SPMi = float(request.form.get('spm'))

        prediction = model.predict([[SOi, Noi, Rpi, SPMi]])
        output = prediction[0]
    except ValueError:
        return "Error: Please enter valid numbers for all fields", 400


    return render_template('result.html', prediction=output)


if __name__ == "__main__":
    app.run(debug=True)
