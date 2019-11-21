
"""
This library interfaces with the pickled model.
"""

import os
import pickle
import pandas as pd
import numpy as np
import spacy
from spacy.tokens import Doc


###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self, model=None, vectorizer=None):
        self.model = load_file('model')
        self.vectorizer = Vectorizer()
        
    def transform(self, raw_input, verbose=False):
        self.raw_input = raw_input
        vinput = self.vectorizer.transform(raw_input).reshape(1, -1)
        if verbose:
            print(vinput)

        return vinput

    def predict(self, user_input=None, size=5):
        if self.data_available(user_input):
            if user_input:
                distances, indices = self.model.query(
                    self.transform(user_input),
                    k=size)
                return indices[0], distances[0]
            else:
                distances, indices = self.model.query(
                    self.vectorized_input,
                    k=size)
                return indices[0], distances[0]
        else:
            raise Error

    def data_available(self, user_input):
        if user_input is None and self.vectorized_input is None:
            raise NoDataProvided
        else:
            if type(user_input) == str:
                self.transform(user_input, verbose=False)
            elif user_input:
                self.vectorized_input = user_input
            return True

class Vectorizer():
    def __init__(self):
        pass

    def transform(self, input_string):
        vectorized_input = get_vector_from_doc(
            tokenize_text(input_string)
        )
        return vectorized_input.reshape(1,-1)

####################
###Error Handling###
####################

class Error(Exception):
    """Base class for Custom Errors"""
    pass

class NoDataProvided(Error):
    """No Data Provided"""
    pass

######################
###Helper Functions###
######################

def get_abs_path(filename, **kwargs):
    if os.path.isfile(os.path.abspath(filename)):
        return os.path.abspath(filename)
    else:
        return os.path.join(
            os.getcwd(), 'djapi/recommender/'+filename,
        )

def load_file(file_key):
    with open(get_abs_path(params[file_key]), 'rb') as f:
        opened = pickle.load(f)
    return opened

##################
##SET PARAMETERS##
##################

params = {
    'model': 'kdtree_model_1.2.pkl'
}

# Load spacy model

# Use if deploying to heroku.  manually add folder to base repo
# path_to_model = os.path.join(os.getcwd(), "en_core_web_md-2.2.0/")

# Use if local/pushing to github.  Requires installation of model via
#    python -m spacy download en_core_web_md
path_to_model = "en_core_web_sm"

nlp = spacy.load(path_to_model)

############################
###Spacy filter/tokenizer###
############################

def tokenize_text(text):
    return nlp(text)

def get_vector_from_doc(x):
    return x.vector