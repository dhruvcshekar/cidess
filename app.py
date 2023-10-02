from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

# Load the saved Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


country_encoding = {
        'Turkey': 1,'Georgia':2 ,'Thailand': 3,'Montenegro':4 ,'Northern Cyprus':5 ,
        'UAE': 6,'Lithuania':7 ,'Belarus':8 ,'Czech Republic': 9,'Uzbekistan':10
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        construction_year = float(request.form['construction_year'])
        total_floors = float(request.form['total_floors'])
        apartment_floor = float(request.form['apartment_floor'])
        rooms = float(request.form['rooms'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        total_area = float(request.form['total_area'])
        living_area = float(request.form['living_area'])

        # Encode the country
        country_encoded = country_encoding.get(country, 0)

        # Create a DataFrame with the user input
        input_data = pd.DataFrame({
            'country': [country_encoded],
            'building_construction_year': [construction_year],
            'building_total_floors': [total_floors],
            'apartment_floor': [apartment_floor],
            'apartment_rooms': [rooms],
            'apartment_bedrooms': [bedrooms],
            'apartment_bathrooms': [bathrooms],
            'apartment_total_area': [total_area],
            'apartment_living_area': [living_area]
        })

        # Make a prediction
        predicted_price = model.predict(input_data)[0]

        return render_template('index.html', predicted_price=predicted_price)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
