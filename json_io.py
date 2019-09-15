#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

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

if __name__ == "__main__":
	app.run()