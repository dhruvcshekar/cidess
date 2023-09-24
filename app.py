from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def encode_country(country):
    country_mapping = {
        'Turkey': 1,'Georgia':2 ,'Thailand': 3,'Montenegro':4 ,'Northern Cyprus':5 ,
        'UAE': 6,'Lithuania':7 ,'Belarus':8 ,'Czech Republic': 9,'Uzbekistan':10 

    }
    return country_mapping.get(country, 0) 


















# Render the home page
@app.route('/')
def home():
    return render_template('index.html', prediction=None)

# Predict the house price
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        country = request.form['country']
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        construction_year = int(request.form['construction_year'])
        












        # Add code to get values for other features (apartment_floor, apartment_rooms, etc.)

        # Preprocess the input data (e.g., encoding country)
        encoded_country = encode_country(country)
        # Replace with actual preprocessing for other features

        # Create a feature vector from the input data
        input_data = np.array([construction_year, encoded_country, ...])  # Include other features

        # Make a prediction using the model
        prediction = model.predict(input_data.reshape(1, -1))[0]

        return render_template('index.html', prediction=round(prediction, 2))

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', prediction=None, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
