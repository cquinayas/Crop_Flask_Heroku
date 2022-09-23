#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def model_prediction(x_in):
    model = pickle.load(open("checkpoints/pickle_model.pkl","rb"))
    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        predictS = model_prediction(to_predict_list)
    return render_template("result.html", prediction=predictS[0].upper())
    

if __name__=="__main__":

    app.run(port=5001)