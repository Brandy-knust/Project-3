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
from tensorflow.keras.models import Sequential
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

model = load(open('model.pkl', 'rb'))
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

@app.route("/predict", methods=['POST'])
def handlePredict():
    return request.form


@app.route("/predict/<Director>/<genre>/<runtime>/<production_company>/<content_rating>")
def predict(Director,genre,runtime,production_company,content_rating):
    new_data = np.array([[Director,genre,runtime,production_company,content_rating]])
    return jsonify(target_names[model.predict(X_scaler.transform(new_data))[0]])

@app.route("/add/<Director>/<genre>/<runtime>/<production_ompany>/<content_rating>/<outcome>")
def add_data(Director,genre,runtime,production_company,content_rating,outcome):
    sql_str = f"INSERT INTO dataset VALUES ({Director},{genre},{runtime},{production_company},{content_rating},{outcome});"
    engine.execute(sql_str)
    return jsonify("success")

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
    app.run()
