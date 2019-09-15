#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

#The throw value that the server holds. Set on BLE input, sent and cleared on VR input.
throwVal = None

@app.route('/', methods=['GET'])
def index():  # pragma: no cover
	return render_template('index.html',name='Joes')
    # content = get_file('./templates/index.html')
    # return Response(content, mimetype="text/html")


@app.route("/", methods = ['POST'])
def pass_login_data():
	# read json + reply
	data = request.get_json()
	result = ''

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

#Get data from the ble controller. Does not currently work.
@app.route("/ble", methods = ['POST'])
def load_ble_data():
    data = request.get_json()
    throwVal = data.val

@app.route("/vr", methods = ["GET"])
def unload_ble_data():
    result = throwVal
    throwVal = 0
    return result

if __name__ == "__main__":
	app.run()