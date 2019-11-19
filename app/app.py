from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pickle import load


#Ethan was here ;)
# Configuration   
load_dotenv() # To access .env
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #Initialise Database
    db = SQLAlchemy(app)

    #temp data
    results = [{"strain_id": 1, "score": 80},
                {"strain_id": 2, "score": 50},
                {"strain_id": 3, "score": 40},
                {"strain_id": 4, "score": 30},
                {"strain_id": 5, "score": 30}]

    #temp "model"
    model = "pickled_model"

    #Home page urls
    @app.route("/")
    def home():
        return render_template('home.html')


    @app.route("/request", methods=['GET', 'POST'])
    def request():
        # user_info = request.args  # Is this correct?
        user_info = "test_data"  # Temporary
        results = get_preds(user_info)
        return jsonify(results)

    def get_preds(user_info):
        # return model.predict(user_info)
        return results
    
    return app