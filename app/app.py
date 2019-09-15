# Libraries
from flask import Flask, request, render_template, url_for, redirect, jsonify
from forms import sliderForm
from algorithm.dataset import Dataset
import random, json

# Variables
USER_XCOORDINATE = ""
USER_YCOORDINATE = ""
USER_SLIDER_1 = ""
USER_SLIDER_2 = ""
USER_SLIDER_3 = ""
USER_SLIDER_4 = ""
USER_SLIDER_5 = ""
INCOME = ""

API_KEY = "AIzaSyDySz37lxM4MpNo3tuUEVF7SOk26eDAr-8"

# SECTIONS: 

# Create Dataset instance from Brendon's code and call function. 
# dataset = Dataset(kevins_data)
# locations = dataset.get_recommendations(dictionary_of_sliders_and_lat_long)

# Instantiating app
app = Flask(__name__)
app.config['SECRET_KEY'] = "YnJRcS9HWjY+DZoFHtE"

# Establishing route for home connection
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = sliderForm()
    dataset = Dataset()

    # Getting slider values
    if form.validate_on_submit():
        INCOME = form.income.data
        USER_SLIDER_1 = form.slider_1.data
        USER_SLIDER_2 = form.slider_2.data
        USER_SLIDER_3 = form.slider_3.data
        USER_SLIDER_4 = form.slider_4.data
        USER_SLIDER_5 = form.slider_5.data
        USER_SLIDER_6 = form.slider_6.data
        
        recommendations = dataset.get_recommendations([USER_XCOORDINATE, USER_YCOORDINATE],
        'Food and Dining', [USER_SLIDER_1, USER_SLIDER_2, USER_SLIDER_3, USER_SLIDER_4, USER_SLIDER_5, USER_SLIDER_6], INCOME)

        return redirect(url_for('recommendations'))

    return render_template('index.html', api_key = API_KEY, form = form)

# Posts data using jQuery
@app.route('/reciever', methods = ['POST'])
def parser():
    # Getting coordinates
    data = request.get_json()
    USER_XCOORDINATE = data['lat']
    USER_YCOORDINATE = data['lng']

    print(USER_XCOORDINATE, ', ', USER_YCOORDINATE)
    return 'Collected marker longitudes and latitudes'

# File to display coordinates of recommendations
@app.route('/recommendations', methods = ['GET'])
def recommendations():
    recommendations = [
        [43.731548, -79.762421, "Mcdonalds"],
        [43.740732, -79.734769, "Tim Hortons"],
        [43.687131, -79.704570, "Res 1"],
        [43.719893, -79.771146, "Res 2"],
        [43.667763, -79.775264, "Res2"]
    ]

    return render_template('recommendations.html', recommendations = recommendations)

# Running app in debug mode
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)