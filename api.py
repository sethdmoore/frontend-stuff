#!/usr/bin/env python

from flask import Flask, jsonify
import json
from flask.ext.cors import CORS, cross_origin

app =  Flask("API")
#cors = cross_origin(app, resources={r"/": {"origins": "*"}})
cors = CORS(app)

@app.route("/")
def index():
    mlist = [
            {"name": ["bill", "morrison"],
             "occupations": ["burger tuner"]},
            {"name": ["candy", "carolsen"],
             "occupations": ["developer", "chief clock watcher"]}
        ]
    # return json.dumps({["Bill", "Morrison"], ["Candy", "Carolsen"]})
    return jsonify({"members": mlist})

if __name__ == "__main__":
    app.run(debug=True)
