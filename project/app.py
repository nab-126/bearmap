from flask import Flask, Response, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')

@app.route('/getMyJson')
def getMyJson():
    # json = dataFrame.to_json(orient='records', date_format='iso')
    # response = Response(response=json, status=200, mimetype="application/json")
    data = {
    "nodes":[
          {"name":"node1","group":1},
          {"name":"node2","group":2},
          {"name":"node3","group":2},
          {"name":"node4","group":3}
      ],
      "links":[
          {"source":2,"target":1,"weight":1},
          {"source":0,"target":2,"weight":3}
      ]
    }
    return json.dumps(data)
    # return(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90)
    app.run()