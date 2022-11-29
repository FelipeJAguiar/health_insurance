import os
import pickle
import requests
import pandas as pd
from flask import Flask, request, Response
from health_insurance.HIClass import HIClass

# loading model
model = pickle.load(open('C:/Users/PICHAU/repos/pa_hi/pa_hi/src/models/model_lgbm_final.pkl', 'rb'))

# initialize API
app = Flask( __name__ )
@app.route('/healthinsurance/predict', methods=['POST'])

def pahi_predict():
    test_json = request.get_json()
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys())
            
        # Instantiate HIClass class
        pipeline = HIClass()

        # feature engineering
        df1 = pipeline.feature_engineering(test_raw)

        # data preparation
        df2 = pipeline.data_preparation(df1)

        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df2)
        return df_response
    
    else:
        return Reponse('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = os.environ.get('PORT', 5000))