# -*- coding: utf-8 -*-

from flask import Flask,jsonify,render_template,request
from category_encoders import *
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
clf=pickle.load(open('model_dt.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/impact',methods=['POST'])
def impact():
    if request.method == 'POST':
        features=[val for val in request.form.values()]
        ID_status = request.form.get("ID_status")
        count_updated = request.form.get("count_updated")
        opened_by = request.form.get("opened_by")
        category_ID = request.form.get("category_ID")
        Support_group = request.form.get("Support_group")


    list1 = np.array([ ID_status,  count_updated,  opened_by,  category_ID,  Support_group])
    list2 = []


    features = np.array(features)

    pkl_file = open('ID_status_encoder.pkl', 'rb')
    le_test = pickle.load(pkl_file)
    pkl_file.close()
    list2.append(le_test.transform(list1[0:1]))


    pkl_file = open('opened_by_encoder.pkl', 'rb')
    le_test = pickle.load(pkl_file)
    pkl_file.close()
    list2.append(le_test.transform(list1[2:3]))


    pkl_file = open('category_ID_encoder.pkl', 'rb')
    le_test = pickle.load(pkl_file)
    pkl_file.close()
    list2.append(le_test.transform(list1[3:4]))


    pkl_file = open('Support_group_encoder.pkl', 'rb')
    le_test = pickle.load(pkl_file)
    pkl_file.close()
    list2.append(le_test.transform(list1[4:5]))

    dict ={'ID_status': [list2[0]], 'count_updated' : [list1[1]], 'opened_by' : [list2[1]], 'category_ID' : [list2[2]], 'Support_group' : [list2[3]]}

    prediction = clf.predict(pd.DataFrame(dict))

    if prediction == 0:
        prediction = 'High'
    elif prediction == 2:
        prediction = "Low"
    else:
        prediction = "Medium"


    return render_template('index.html', prediction_text='Impact will be {}!'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
