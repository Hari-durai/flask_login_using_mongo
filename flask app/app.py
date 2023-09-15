from flask import Flask, render_template, request , jsonify
import numpy as np
import certifi
import pymongo
from pymongo import MongoClient
from mango import uri
app = Flask(__name__)

ca = certifi.where()

client = MongoClient(uri,tlsCAFile=certifi.where())

db=client['test']
col=db['test']
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST','GET'])
def predict():
    # name='hari'
    # user='hariharan1234@gmail.com'
    # uid='hariharan1234'
    # pas='q1w2e3r4'
    # if request.method == 'GET':
    # # name=str(request.form['name'])
    # # user = str(request.form['username'])
    # # uid = str(request.form['uid'])
    # # pas= str(request.form['password'])
    #     pos={"_id":uid,"name":name,"user":user,"password":pas}
    #     #col.insert_one(pos)
    # #    print(pos)
    # #    jsonify(pos)
    #     return jsonify(pos)
    if request.method == 'POST':
        name=str(request.form['name'])
        user = str(request.form['username'])
        uid = str(request.form['uid'])
        pas= str(request.form['password'])
        pos={"_id":uid,"name":name,"user":user,"password":pas}
        col.insert_one(pos)
        

        
        return render_template('result.html', use=user,ui=uid,pasw=pas,nam=name)

@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        name=str(request.form['name'])
        user = str(request.form['username'])
        uid = str(request.form['uids'])
        pas= str(request.form['password'])
        ud=int(request.form['upd'])
        #pos={"_id":uid,"user":user,"password":pas}
        #col.update_one({'_id':uid},{"$set":{'user':user}})
        #print("111111111111111111111111111111111111111111111111111111111111111111")
        print(user,pas,uid,ud,name)
        if ud==0:
            col.update_one({'_id':uid},{"$set":{'name':name,'user':user,'password':pas}})
            return render_template('result.html', use=user,ui=uid,pasw=pas,nam=name)
        else:
            col.delete_one({'_id':uid})
            return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

