from flask import Flask, Response, render_template, jsonify, request
# from flask_pymongo import PyMongo
import json
import pymongo


app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'restdb'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

app.config['MONGO_URI'] = "mongodb+srv://admin:jlwkrcotQDYlbW3F@berkeley.bljdr.mongodb.net/<dbname>?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = "Berkeley"

# mongo = PyMongo(app)
connection = pymongo.MongoClient('mongodb+srv://admin:jlwkrcotQDYlbW3F@berkeley.bljdr.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = connection['Berkeley']

@app.route('/data', methods=['GET'])
def get_data():
  classes = db['Classes']
#   classes = db.Classes
  output = []
  for c in classes.find():
    output.append(c['code'])
  return jsonify({'result' : output})

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')

@app.route('/getMyJson')
def getMyJson():
    # json = dataFrame.to_json(orient='records', date_format='iso')
    # response = Response(response=json, status=200, mimetype="application/json")
    # data = {
    # "nodes":[
    #       {"name":"node1","group":1},
    #       {"name":"node2","group":2},
    #       {"name":"node3","group":2},
    #       {"name":"node4","group":3}
    #   ],
    #   "links":[
    #       {"source":2,"target":1,"weight":1},
    #       {"source":0,"target":2,"weight":3}
    #   ]
    # }
    data = [{'title': "Data 8", 'id': 0, 'x':100, 'y':100},
    {'title': "Math 1A", 'id': 1, 'x':100, 'y':100},
    {'title': "Math 1B", 'id': 2, 'x':100, 'y':100},
    {'title': "Math 54", 'id': 3, 'x':100, 'y':100},
    {'title': "CS 61A", 'id': 4, 'x':100, 'y':100},
    {'title': "CS 61B", 'id': 5, 'x':200, 'y':200},
    {'title': "Data 100", 'id': 6, 'x':100, 'y':150}]
    return json.dumps(data)
    # return data

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=90)
    app.run(debug=True, TEMPLATES_AUTO_RELOAD=True)
