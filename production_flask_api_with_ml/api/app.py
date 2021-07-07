from typing_extensions import runtime
from numpy.lib.twodim_base import triu_indices
import requests

from flask import Flask, json, request
from flask import jsonify, render_template
import datetime as dt
import os
import pandas as pd
import sqlalchemy
from pickle import load
from pickle import dump

from sqlalchemy import sql
import numpy as np

from numpy.random import seed


import tensorflow
tensorflow.keras.__version__

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import OneHotEncoder



if not os.path.exists("data.db"):
    engine=sqlalchemy.create_engine('sqlite:///data.db')
    df=pd.read_csv("Resources/Merged_All_df.csv")
    df.to_sql("dataset",index=False,con=engine)

else:
    engine=sqlalchemy.create_engine('sqlite:///data.db')

movie_directors_df = pd.read_csv('Resources/movie_director_df(1).csv')


model = load_model('model.h5')
#X_scaler = load(open('scaler.pkl', 'rb'))
audience_score = [] 
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, Worldz!'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/directors')
def getDirectors():
    data_list = list(movie_directors_df.columns)
    data_list.pop(0)
    return jsonify(data_list)

# @app.route("/predict", methods=['POST'])
# def handlePredict():
# #    return request.form
#     
#     print(request.form)
#     return render_template("index.html", result = 67) 
    

@app.route("/predict",  methods=['POST'])
def predict():
    input_dictionary = request.form
    dim_df = pd.read_csv('Resources/dim_df.csv')
    data=list(input_dictionary.items())
    response_array=np.array(data)

   

    for i in range(0, len(response_array)):
        if response_array[i,1] == '<=90 minutes':
            response_array[i,1]= response_array[i,1].replace('<=90 minutes','1.0')
        elif response_array[i,1] == '90-120 minutes':
            response_array[i,1]= response_array[i,1].replace('90-120 minutes','2.0')
        elif response_array[i,1] == '>=120 minutes':    
            response_array[i,1]= response_array[i,1].replace('>=120 minutes','3.0')
    dummy_list = np.zeros(len(dim_df.columns))

    for i in range(0, len(response_array)):
        index = dim_df.columns.get_loc(response_array[i,1])
        dummy_list[index] = 1

    app.logger.info(f'data : {data}')

    # director_list = input_dictionary.keys()[4:]
    model_result = model.predict(dummy_list.reshape(1,-1))
    app.logger.info(model_result)
    # rebuilt_dict = {"rating" : input_dictionary[0], "genre" : input_dictionary[1], "prod_co": input_dictionary[2], "run_time" : input_dictionary[3], "director": director_list}
    result= {'input':input_dictionary,'score':model_result[0][0]}
    # result= {'input':input_dictionary[:4],'score':model_result[0][0], 'director': director_list}
    app.logger.info(result)
    #return jsonify(model.predict(new_data))
    return render_template("index.html", result = result)

# @app.route("/add/<Director>/<genre>/<runtime>/<production_ompany>/<content_rating>/<outcome>")
# def add_data(Director,genre,runtime,production_company,content_rating,outcome):
#     sql_str = f"INSERT INTO dataset VALUES ({Director},{genre},{runtime},{production_company},{content_rating},{outcome});"
#     engine.execute(sql_str)
#     return jsonify("success")

# @app.route("/train")
# def train():
#     sql_str="SELECT Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome FROM dataset"
#     df = pd.read_sql(sql_str,engine)
#     target = df["Outcome"]
#     data = df.drop("Outcome", axis=1)
#     X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)
#     # X_scaler = StandardScaler().fit(X_train)
#     # X_train_scaled = X_scaler.transform(X_train)
#     # X_test_scaled = X_scaler.transform(X_test)
#     rf = RandomForestClassifier(n_estimators=420)
#     model = rf.fit(X_train_scaled, y_train)
#     acc=model.score(X_test_scaled, y_test)
#     dump(X_scaler, open('scaler.pkl', 'wb'))
#     dump(model, open('model.pkl', 'wb'))

#    return jsonify({"acc":acc,})

if __name__ == '__main__':
    app.run(debug=True)
