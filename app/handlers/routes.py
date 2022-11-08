import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"

    # request returns a json object with the admisison prediction and student information
    @app.route('/predict')
    def predict():
        G1 = request.args.get('G1')
        G2 = request.args.get('G2')
        failures = request.args.get('failures')
        studytime = request.args.get('studytime')
        absences = request.args.get('absences')
        data = [[G1], [G2], [failures], [studytime], [absences]]
        query_df = pd.DataFrame({
            'G1': pd.Series(G1),
            'G2': pd.Series(G2),
            'failures': pd.Series(failures),
            'studytime': pd.Series(studytime),
            'absences': pd.Series(absences)
        })
       
        prediction = clf.predict(query_df)
        print(np.ndarray.item(prediction))
        return jsonify({"AdmissionStatus": np.ndarray.item(prediction), 
                        "G1": int(G1), 
                        "G2": int(G2), 
                        "failures": int(failures), 
                        "studytime": int(studytime), 
                        "absences": int(absences)})
