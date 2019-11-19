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
        """Root page, you shoud not land here.
        
        Returns:
            string -- Provides link to project home.
        """
        return render_template('home.html')


    @app.route("/request", methods=['GET', 'POST'])
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
        user_input = user_input or request.values["user_input"]
        results = get_preds(user_input)
        return jsonify(results)
    
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
        # return model.predict(user_info)
        return results
    

    return app