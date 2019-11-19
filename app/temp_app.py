from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pickle import load
from model import model

Predictor = model.Predictor()

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

    test_string = """The strain produces a citrus sweet, often described as red grapefruit,
    flavor that is tinged with just a bit of diesel. Such a rare taste delivers a powerful
    high that most often energizes users and activates their minds. """ 




    #Home page urls
    @app.route("/")
    def home():
        """Root page, you shoud not land here.
        
        Returns:
            string -- Provides link to project home.
        """
        return render_template('home.html')


    # @app.route("/request", methods=['GET', 'POST'])
    # def search(user_input=test_string):
    #     """Takes in user input and predicts top five recommended strains
        
        # Keyword Arguments:
        #     user_input {str} -- [effects, ailments, and flavors to pass to model ]
        #      (default: {None})
        
    #     Returns:
    #         [ARRAY] -- Returns a List of recommended strains, and a score of recommendation strength
    #         [EXAMPLE:] -- [{"strain_id": 1, "score": 80},
    #                       {"strain_id": 2, "score": 50},
    #                       {"strain_id": 3, "score": 40},
    #                       {"strain_id": 4, "score": 30},
    #                       {"strain_id": 5, "score": 30}]
    #     """
    #     user_input = user_input or request.values["user_input"]
    #     results = get_preds(user_input)
    #     return jsonify(results)
    
    @app.route('/request/', methods=['GET'])
    def recommend():
        # Set Defaults
        num_responses = 5

        if request.method == 'GET':
            if not 'search' in request.args:
                raise InvalidUsage(message="Search query not provided")
            if 'qty' in request.args:
                num_responses = int(request.args['qty'])

        # Get indices of strain from KDTree model
        pred_indices = Predictor.predict(user_input=request.args['search'], size=num_responses)
        pred_distances = Predictor.predict(user_input=request.args['search'], size=num_responses)

        return pred_indices, pred_distances
    
    class InvalidUsage(Exception):
        status_code = 400

        def __init__(self, message, status_code=None, payload=None):
            Exception.__init__(self)
            self.message = message
            if status_code is not None:
                self.status_code = status_code
            self.payload = payload

        def to_dict(self):
            rv = dict(self.payload or ())
            rv['message'] = self.message
            return rv

    # Register error handler
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


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
        return Predictor.predict(user_info)
        # return(user_info)
        

    return app
