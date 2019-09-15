#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response, jsonify
import random, json

app = Flask(__name__)

#The throw value that the server holds. Set on BLE input, sent and cleared on VR input.
@app.route('/', methods=['GET'])
def index():  # pragma: no cover
	return render_template('index.html',name='Joes')
    # content = get_file('./templates/index.html')
    # return Response(content, mimetype="text/html")


@app.route("/", methods = ['POST'])
def pass_login_data():
	# read json + reply
	data = request.get_json()
	accessToken = data.authResponse.accessToken
	userID = data.authResponse.accessToken
	result = ''

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

#Get data from the ble controller. Does not currently work.
@app.route("/ble", methods = ['POST'])
def load_ble_data():
    data = request.get_json()
    if data and data["val"]:
        setThrowVal(data["val"])
        return jsonify(data["val"]),200
    if not data:
        return jsonify("No JSON given"),400
    if not data["val"]:
        return jsonify("No 'val' property in JSON"),400

@app.route("/vr", methods = ["GET"])
def unload_ble_data():
    result = getThrowVal()
    setThrowVal(None)
    return jsonify(result), 200

throwVal = None
def getThrowVal():
    global throwVal
    return throwVal
def setThrowVal(val):
    global throwVal
    throwVal = val

if __name__ == "__main__":
	app.run()