#!/usr/bin/env python

from flask import Flask, jsonify, request, Response
import json
import random
from flask.ext.cors import CORS, cross_origin

app =  Flask("API")
#cors = cross_origin(app, resources={r"/": {"origins": "*"}})
cors = CORS(app)

mlist = [
        {"name": ["bill", "morrison"],
         "occupations": ["burger tuner"]},
        {"name": ["candy", "carolsen"],
         "occupations": ["developer", "chief clock watcher"]},
        {"name": ["jeff", "jeffries"],
         "occupations": ["spoon licker", "brown noser"]}
]

@app.route("/", methods=['GET', 'PUT'])
def index():
    # return json.dumps({["Bill", "Morrison"], ["Candy", "Carolsen"]})
    if request.method == "GET":
        return jsonify({"members": mlist})
    else:
        if mlist:
            del mlist[random.randint(0, len(mlist) -1)]
            return jsonify({"status": "done"})
        else:
            return Response(jsonify({"status": "can't do"}), status=406)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
