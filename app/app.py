# Libraries
from flask import Flask, request, render_template, url_for, redirect

# Variables
USER_XCOORDINATE = ""
USER_YCOORDINATE = ""
USER_ID = ""

# Gets recommendation from algorithm 
def get_recommendations(transaction_information):
    return transaction_information

# Instantiating app
app = Flask(__name__)
app.config['SECRET_KEY'] = "YnJRcS9HWjY+DZoFHtE"

# Establishing route for home connection
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Running app in debug mode
if __name__ == '__main__':
    app.run(debug = True)