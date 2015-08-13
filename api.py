#!/usr/bin/env python

from flask import Flask, jsonify, request, Response
import json
import random
from flask.ext.cors import CORS, cross_origin

app =  Flask("API")
#cors = cross_origin(app, resources={r"/": {"origins": "*"}})
cors = CORS(app)

occupation_nouns = [
    "paint",
    "spoon",
    "car",
    "stage",
    "chair",
    "desk"
]

occupation_verbs = [
    "taster",
    "cooker",
    "frier",
    "dresser",
    "dancer"
]

first_names = [
    "bill",
    "candy",
    "jeff",
    "clay",
    "frank",
    "sally",
    "jane"
]

last_names = [
    "billiams",
    "nathans",
    "ivans",
    "timber",
    "clueless"
]

mlist = [
        {"name": ["bill", "morrison"],
         "occupations": ["burger tuner"]},
        {"name": ["candy", "carolsen"],
         "occupations": ["developer", "chief clock watcher"]},
        {"name": ["jeff", "jeffries"],
         "occupations": ["spoon licker", "brown noser"]},
        {"name": ["jeff", "jeffries"],
         "occupations": ["spoon licker", "brown noser"]}
]

@app.route("/hire", methods=['PUT'])
@cross_origin()
def hire():
    rando = {"name": [random.choice(first_names), random.choice(last_names)],
             "occupations": [" ".join((random.choice(occupation_nouns),
                                       random.choice(occupation_verbs)))]}
    mlist.append(rando)
    return Response(status=200)


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
    app.run(host='0.0.0.0', debug=True, threaded=True)
