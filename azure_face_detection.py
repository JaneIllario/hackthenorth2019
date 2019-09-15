import os
import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os

# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline

# Replace <Subscription Key> with your valid subscription key.
FACE_SUBSCRIPTION_KEY = os.environ['COGNITIVE_SERVICE_KEY']

for it, profile_img in enumerate(os.listdir("data")):
	# Set image path from local file.
	image_path = os.path.join('data/profile-'+ str(it)+'.jpg')

	assert FACE_SUBSCRIPTION_KEY

	# You must use the same region in your REST call as you used to get your
	# subscription keys. For example, if you got your subscription keys from
	# westus, replace "westcentralus" in the URI below with "westus".
	#
	# Free trial subscription keys are generated in the westcentralus region.
	# If you use a free trial subscription key, you shouldn't need to change
	# this region.
	face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'

	image_data = open(image_path, "rb")
	im = Image.open(image_path)

	headers = {'Content-Type': 'application/octet-stream',
	           'Ocp-Apim-Subscription-Key': FACE_SUBSCRIPTION_KEY}
	params = {
	    'returnFaceId': 'true',
	    'returnFaceLandmarks': 'false',
	    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
	    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
	}

	response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
	response.raise_for_status()
	faces = response.json()

	for face in faces:
		fr = face["faceRectangle"]
		left = fr["left"]
		top = fr["top"]
		width = fr["width"]
		height = fr["height"]
		cropped_img = im.crop((left, top, (left+width), (top+height)))
		cropped_img.save("faces/face-" + str(it) + ".jpg", "JPEG")

print("done")