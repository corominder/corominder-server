from data import MapData
import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

api_key = "AIzaSyD42KMDWyXKW2-MVPMD0UR-4aceApBpdYQ"
search_radius = 0.009213
dataSource = MapData(api_key)

@app.route('/api', methods=['GET'])
def home():
    return '''<h1>Corominders api</h1>
<p>/amisafe?'''


# A route to return all of the available entries in our catalog.
@app.route('/api/amisafe/<float:lat>/<float:lng>/<int:threshold>', methods=['GET'])
def task(lat, lng, threshold):
    return jsonify(dataSource.get((lat, lng), threshold, search_radius))

app.run()
