# Libraries
from flask import Flask, request, render_template, url_for, redirect, jsonify
from forms import sliderForm
import random, json

# Variables
USER_XCOORDINATE = ""
USER_YCOORDINATE = ""
USER_SLIDER_1 = ""
USER_SLIDER_2 = ""
USER_SLIDER_3 = ""
USER_SLIDER_4 = ""
USER_SLIDER_5 = ""

API_KEY = "AIzaSyDySz37lxM4MpNo3tuUEVF7SOk26eDAr-8"

# Create Dataset instance from Brendon's code and call function. 
# dataset = Dataset(kevins_data)
# locations = dataset.get_recommendations(dictionary_of_sliders_and_lat_long)

# Instantiating app
app = Flask(__name__)
app.config['SECRET_KEY'] = "YnJRcS9HWjY+DZoFHtE"

# Establishing route for home connection
@app.route('/')
@app.route('/index')
def index():
    form = sliderForm()

    # Getting slider values
    if form.validate_on_submit():
        USER_SLIDER_1 = form.slider_1.data
        USER_SLIDER_2 = form.slider_2.data
        USER_SLIDER_3 = form.slider_3.data
        USER_SLIDER_4 = form.slider_4.data
        USER_SLIDER_5 = form.slider_5.data

    return render_template('index.html', api_key = API_KEY, form = form)

# Posts data using jQuery
@app.route('/reciever', methods = ['POST'])
def parser():
    # Getting coordinates
    data = request.get_json()
    USER_XCOORDINATE = data['lat']
    USER_YCOORDINATE = data['lng']


# Running app in debug mode
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)