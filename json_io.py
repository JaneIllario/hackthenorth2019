#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response, jsonify
import random, json
# import facebook
from azure_face_detection import face_detection

app = Flask(__name__)

#The throw value that the server holds. Set on BLE input, sent and cleared on VR input.
@app.route('/', methods=['GET'])
def index():  # pragma: no cover
	return render_template('index.html',name='Joes')
    # content = get_file('./templates/index.html')
    # return Response(content, mimetype="text/html")


# @app.route("/", methods = ['POST'])
# def pass_login_data():
# 	# read json + reply
# 	data = request.get_json()
# 	accessToken = data.authResponse.accessToken
# 	userID = data.authResponse.accessToken
#
#     # graph = facebook.GraphAPI(access_token=accessToken, version="2.12")
#     # # Get the active user's friends.
#     # friends = graph.get_connections(id='me', connection_name='friends')
#
#     	# URL used to access friend information from account
# #     FRIEND_URL = 'https://graph.facebook.com/me/friends?access_token=%s'
#
#     # URL to retrieve the profile picture from an account
# #     PHOTO_URL = 'http://graph.facebook.com/%s/picture?type=square'
#
#     # MD5 Hashes of blank images
#     BLANK_HASHES = []
#     # MD5 Hash of the blank male image
#     BLANK_HASHES.append('af10cdc4144e0a16b097a293b0d95422')
#     # MD5 hash of the blank female image
#     BLANK_HASHES.append('04aaffaf075732616c0c35ae3e28bce6')
#
#     # Initial URL (before paging)
#     url = FRIEND_URL % accessToken
#
#     # Complete friend list (from all pages)
#     friend_id_list = []
#
#     def get_json_data(url):
#         """
#         Retrieves the JSON response from Facebook and returns a parsed element.
#         """
#         urldata = urlopen(url)
#         fh = urldata.read()
#
#         return json.loads(fh)
#
#
#     def get_friends(json_data, friend_ids):
#         """
#         Takes the JSON data object and adds the friend IDs to a given list.
#         """
#         try:
#             for friend in json_data["data"]:
#                 friend_ids.append(friend["id"])
#         except KeyError:
#             print "Error: Data element not found in response."
#             if json_data["error"]:
#                 print "{0}: {1}".format(json_data["error"]["type"],
#                                         json_data["error"]["message"])
#             raise SystemExit(1)
#
#         return friend_ids
#
#
#     print "Retrieving first page of friend results ..."
#     json_data = get_json_data(url)
#     friend_id_list = get_friends(json_data, friend_id_list)
#
#     while json_data is not None:
#         try:
#             print "Retrieving next page of friend results ..."
#             url = json_data["paging"]["next"]
#             json_data = get_json_data(url)
#             friend_id_list = get_friends(json_data, friend_id_list)
#         except KeyError:
#             json_data = None
#
#     print "Friend retrieval complete, {0} friends found.".format(len(friend_id_list))
#
#     # Cache the images at the beginning so they don't have to download every use.
#     friend_images = []
#     print "Downloading profile pictures ..."
#     for x in friend_id_list:
#         img_url = PHOTO_URL % x
#         img_obj = cStringIO.StringIO(urlopen(img_url).read())
#         # Avoid adding the blank images
#         if md5(img_obj.getvalue()).hexdigest() not in BLANK_HASHES:
#             friend_images.append(Image.open(img_obj))
#
#     for it, img in friend_images:
#         img.save("data/profile-"+ str(it)+".jpg", "JPEG")
#
#     print("Done saving profiles")
#     azure_face_detection.face_detection()
#

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
    return render_template('bs.html',val=str(result))

throwVal = None
def getThrowVal():
    global throwVal
    return throwVal
def setThrowVal(val):
    global throwVal
    throwVal = val

if __name__ == "__main__":
	app.run()