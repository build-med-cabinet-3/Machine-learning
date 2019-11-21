from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pickle import load
from model.model import *
from .get_info import strain_info

#Ethan was here ;)
#load app
# Configuration   
load_dotenv() # To access .env
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    #Initialise Database
    db = SQLAlchemy(app)


    #temp data
    test_results = [{1: [{'strain': 'afternoon-delight'},
     {'effect': 'Creative Euphoric Focused Happy Relaxed Talkative Tingly Uplifted'},
      {'medical_effect_plain': 'Pain relief Anorectic Inhibits bacteria Antiemetic Antiepileptic Reduces inflammation Aids sleep Inhibits cancer growth Suppresses muscle spasms Increases appetite Stimulates bone growth Reduces acid reflux'}, {'flavor': 'Apple Berry Citrus Diesel Earthy Fruity Nutty Pine Pungent Skunk Tropical'}, {'Type': 'hybrid'}, {'THC_Percent': '0.19'}, {'CBD': '0.09333333333333334'}, {'Description1': 'Afternoon Delight is a sativa dominant hybrid strain created through a cross of the insanely delicious'},
      {'Score': 2.29822077}]}]

    test_string = """The strain produces a citrus sweet, often described as red grapefruit,
    flavor that is tinged with just a bit of diesel. Such a rare taste delivers a powerful
    high that most often energizes users and activates their minds. """ 



    #temp "model"
    model = "pickled_model"


    #Home page urls
    @app.route("/")
    def home():
        """Root page, you shoud not land here.
        
        Returns:
            string -- Provides link to project home.
        """
        return render_template('home.html')


    @app.route("/request/", methods=['GET', 'POST'])
    def search(user_input=None):
        """Takes in user input and predicts top five recommended strains
        
        Keyword Arguments:
            user_input {str} -- [effects, ailments, and flavors to pass to model ]
             (default: {None})
        
        Returns:
            [ARRAY] -- Returns a List of recommended strains, and a score of recommendation strength
            [EXAMPLE:] -- [{"strain_id": 1, "score": 80},
                          {"strain_id": 2, "score": 50},
                          {"strain_id": 3, "score": 40},
                          {"strain_id": 4, "score": 30},
                          {"strain_id": 5, "score": 30}]
        """
<<<<<<< HEAD
        user_input = str(request.args['search'])
        decoded = decode(user_input)
        results = get_preds(decoded)
        indices = results[0]
        distances = results[1]
        strain_list = strain_info(distances, indices)
        return jsonify(strain_list)
=======

        user_input = request.args['search']
        results = get_preds(user_input)
        info = strain_info(results[0], results[1])
        
        
        print(user_input)
        # return str(results)
        return jsonify(info)
>>>>>>> 0fbbba65856f85e0fc804bae078b6f2b371ec524

    @app.route("/test/", methods=['GET', 'POST'])
    def test_search(user_input=test_string):
        """Takes in user input and predicts top five recommended strains
        
        Keyword Arguments:
            user_input {str} -- [effects, ailments, and flavors to pass to model ]
             (default: {None})
        
        Returns:
            [ARRAY] -- Returns a List of recommended strains, and a score of recommendation strength
            [EXAMPLE:] -- [{"strain_id": 1, "score": 80},
                          {"strain_id": 2, "score": 50},
                          {"strain_id": 3, "score": 40},
                          {"strain_id": 4, "score": 30},
                          {"strain_id": 5, "score": 30}]
        """

        user_input = request.args['search']
        print(user_input)
        results1 = [1237, 1131, 780, 1418, 127]
        results2 = [2.29822077, 2.3112716 , 2.31566792, 2.31842484, 2.3206283]
        info = strain_info(results1, results2)
        return jsonify(info)
        # return jsonify(test_results, user_input, info) 
    
    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist', 404

    def get_preds(user_info):
        """Retrives prediction
        
        Arguments:
            user_info {str} -- Returns a List of recommended strains, and a score of recommendation strength
        
        Returns:
            list -- Predictions
        """
        nlpmodel = Predictor()
        pred_distances, pred_indices = nlpmodel.predict(user_input=user_info)

        return [pred_indices, pred_distances]

    def decode(input_str):
        return input_str.replace("%22", " ").replace("%20", " ").replace("%7B", " ").replace("%7D", " ")
    
    return app
