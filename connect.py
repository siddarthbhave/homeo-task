from flask import Flask, request
from flask_pymongo import PyMongo
from decouple import config
import json
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = config('MONGO_URI')
mongo = PyMongo()
mongo.init_app(app)


@app.route('/')
def index():
    beds = mongo.db.beds
    return '<h3>Database Connected</h3>'


@app.route('/find/<bedid>')
def find(bedid):
    bed = mongo.db.beds.find_one({'bedid': bedid})
    return f'<h3>Bed ID: { bed["bedid"] }, Name: { bed["name"] }, date: {bed["date"]}, Hospital: {bed["hospital"]}, Critical Level:{bed["criticalLevel"]}, Pin:{bed["pin"]} </h3>'


@app.route('/update/<bedid>', methods=['GET', 'POST'])
def update(bedid):
    con = request.json
    bed = mongo.db.beds.find_one({'bedid': bedid})
    if not bed: return '<h3>User doesn\'t exist. Try adding User</h3>'

    for i in mongo.db.beds.find():
        if i['date'] == con['date'] and i['hospital'] == con['hospital'] and i['bedid'] == con['bedid']:
            return '<h3>Date, Bed and Hospital Overlap. Choose different date or hospital or Bed</h3>'

    for i in con.keys():
        bed[i] = con[i]
    mongo.db.beds.save(bed)
    return '<h3>User updated<h3/></br>' + json.dumps(bed)


@app.route('/add', methods=['GET', 'POST'])
def add():
    content = request.json
    for i in mongo.db.beds.find():
        if i['date'] == content['date'] and i['hospital'] == content[
                'hospital'] and i['bedid'] == content['bedid']:
            return '<h3>Date, Bed and Hospital Overlap. Choose different date or hospital or Bed</h3>'

    mongo.db.beds.insert({
        'bedid': content['bedid'],
        'name': content['name'],
        'date': content['date'],
        'hospital': content['hospital'],
        'criticalLevel': content['criticalLevel'],
        'pin': content['pin']
    })
    return '<h3>User Added</h3></br>' + json.dumps(content)


@app.route('/delete/<bedid>', methods=['GET', 'DELETE'])
def delete(bedid):
    mongo.db.beds.find_one_and_delete({'bedid': bedid})
    return '<h3>User deleted</h3>'


@app.route('/get_all')
def get_all():
    return dumps(mongo.db.beds.find())


@app.route('/filter')
def filter():
    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    if arg1 in 'criticalLevelpin': arg2 = int(arg2)
    data = mongo.db.beds.find({arg1: arg2}, {'_id': 0})
    ret = {}
    for i in data:
        ret[i['bedid']] = i
    if not ret: return '<h3>Arguments passed in filter incorrect</h3>'
    return json.dumps(ret)