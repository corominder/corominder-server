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
    return '''<h1>Corominder api</h1>
<p>/get_crowded_places/[lat]/[lng]/[threshold] </p> may take up to 10 seconds'''


# A route to return all of the available entries in our catalog.
@app.route('/api/get_crowded_places/<float:lat>/<float:lng>/<int:threshold>', methods=['POST'])
def task(lat, lng, threshold):
    return jsonify(dataSource.get((request.form['lat'], request.form['lng']), request.form['threshold'], search_radius))

app.run(host='0.0.0.0', port=80)
