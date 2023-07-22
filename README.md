# Air Quality Prediction Web Application
This project is a Flask-based web application designed to predict the air quality category based on various air quality index (AQI) measurements. The application takes user input of four AQI measurements: sulfur dioxide (SO2), nitrogen dioxide (NO2), respirable suspended particulate matter (RSPM), and suspended particulate matter (SPM). These measurements are then used to predict the air quality category, which can be one of the following: Excellent, Acceptable, Caution, Poor, Very Poor, or Critical.

# Implementation
The model used for prediction is a pre-trained Random Forest model, which is loaded at the start of the application. The app is implemented using the Flask web framework.

The main application (app.py) consists of two routes:

'/' - The homepage, which renders a form for the user to input the AQI measurements.
'/predict' - A POST route that receives the form data, makes a prediction using the Random Forest model, and renders a result page.
The templates for the application are found in the templates directory and include:

- **index.html** - The homepage of the application, containing the form for the user to input the AQI measurements.
- **result.html** - The results page, which displays the predicted air quality category and a description of what that category means.
- The application's styling is in the static/style.css file.

# Visual Feedback
To provide better visual feedback, the results page changes the color of the text and the background color of the result container based on the predicted air quality category. The colors are set in the CSS file and are applied through a class that matches the name of the predicted category. The color scheme is as follows:

- ![Green](https://via.placeholder.com/15/008000/000000?text=+) `Excellent`
- ![Light Yellow](https://via.placeholder.com/15/ffff00/000000?text=+) `Acceptable`
- ![Light Orange](https://via.placeholder.com/15/ffa500/000000?text=+) `Caution`
- ![Light Red](https://via.placeholder.com/15/f03c15/000000?text=+) `Poor`
- ![Dark Red](https://via.placeholder.com/15/8b0000/000000?text=+) `Very Poor`
- ![Maroon](https://via.placeholder.com/15/800000/000000?text=+) `Critical`


# Usage
To use the application, start the Flask server by running app.py. Then, navigate to the server's address in your web browser (by default, this is localhost:5000). Enter the AQI measurements into the form and submit the form to see the predicted air quality category.

# Future Improvements
This application could be improved in several ways:

- **Improving user input validation:** The application currently only checks if the inputs are numbers. Additional validation could include checking that the numbers are within the expected range for AQI measurements.

- **Improving visual feedback:** The visual feedback could be further improved by adding animations or more sophisticated design elements. The color scheme could also be adjusted to be more visually appealing or to better represent the severity of each category.

