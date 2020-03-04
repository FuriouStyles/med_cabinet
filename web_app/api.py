from flask import Blueprint, jsonify, request, render_template, current_app
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


my_routes = Blueprint("my_routes", __name__)
filename = 'static/baseline_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


@my_routes.route('/')
def home():
    return 'Welcome Home, Homie!'

# Don't forget to re-add the GET method when deploying to Heroku
@my_routes.route('/get_recommendation')
def get_recommendation():
    # For now: this will return details on a random strain from a local db
    # if(request.method == 'GET'):
        ailment = request.args['ailment']
        relief = request.args['relief']
        booboo = ailment + relief
        temp_booboo = "I want to be able to stand up and not fall down at the same time, while also being able to speak and swallow liquids. I don't want to get too high."
        pred = loaded_model.predict(temp_booboo)


        return str(pred)

    # if(request.method == 'POST'):
    #     return 'OOPS! Sorry! This route is only used for GET requests.'
