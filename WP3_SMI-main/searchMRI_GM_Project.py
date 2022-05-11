# USAGE
# python search.py --model output/autoencoder.h5 --index output/index.pickle 

# import the necessary packages
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from helper.load_custome_data import load_images_from_folder
from helper.load_custome_data import load_images_from_folderNII
from helper.hyperparameters import height, width
import imutils
#from imutils import  build_montage

from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from operator import itemgetter
from tkinter_UI import show_images
#from CBIR_GUI import show_images
import numpy as np
import argparse
import pickle
import cv2
import os

#--model /home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/output/autoencoderMRI.json --index /home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/output/indexMRINew.pickle
def euclidean(a, b):
	# compute and return the euclidean distance between two vectors
	return np.linalg.norm(a - b)

def perform_search(queryFeatures, index, maxResults=64):
	# initialize our list of results
	results = []

	# loop over our index
	for i in range(0, len(index["features"])):
		# compute the euclidean distance between our query features
		# and the features for the current image in our index, then
		# update our results list with a 2-tuple consisting of the
		# computed distance and the index of the image
		d = euclidean(queryFeatures, index["features"][i])
		results.append((d, index["indexes"][i])) #i))

	# sort the results and grab the top ones
	results = sorted(results) #[:maxResults]
	print(np.array(results).shape)

	# return the list of results
	return results

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained autoencoder")
ap.add_argument("-i", "--index", type=str, required=True,
	help="path to features index file")
ap.add_argument("-s", "--sample", type=int, default=5,
	help="# of testing queries to perform")
args = vars(ap.parse_args())

args = vars(ap.parse_args())

# load the dataset
print("[INFO] loading dataset...")
#path = '/home/azureuser/PycharmProjects/WP3/'
path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/'
#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)
subfolders = [ f.path for f in os.scandir(path+'MRISeq/') if f.is_dir() ]
image_data = []
filenames = []
labels_names =[]
labels=[]
for folder in subfolders :

	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width=width, height=height)
	if 'DTI' in folder:
		image_data1 = image_data1[:600]
		filenames1 = filenames1[:600]
	image_data.append(image_data1)  # [*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)
	labels_names.append([folder[len(path + 'MRISeq/IXI-'):]] * len(image_data1))
	labels.append(folder[len(path + 'MRISeq/'):])

labels_names = [item for sublist in labels_names for item in sublist]

y_dense =labels_names

	#labels_names.append([folder[len(path + 'MRISeq/IXI-'):]] * len(image_data1))
	#labels.append(folder[len(path + 'MRISeq/'):])

image_data = [item for sublist in image_data for item in sublist]
filenames = [item for sublist in filenames for item in sublist]
image_data = np.array(image_data)

#x_train,x_test = train_test_split(image_data,test_size=0.3, shuffle = True)
#y_train,y_test = train_test_split(filenames,test_size=0.3, shuffle = True)


#trainX =  x_train
x_train, x_test, y_train, y_test = train_test_split(image_data, y_dense, test_size=0.10)
testX = x_test#x_test#[100:]

# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
# trainX = np.expand_dims(trainX, axis=-1)
# testX = np.expand_dims(testX, axis=-1)
#trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# load the autoencoder model and index from disk
print("[INFO] loading autoencoder and index...")
json_file = open(args["model"], 'r')
loaded_model_json = json_file.read()
json_file.close()
autoencoder = model_from_json(loaded_model_json)

#autoencoder = load_model(args["model"])
index = pickle.loads(open(args["index"], "rb").read())

# create the encoder model which consists of *just* the encoder
# portion of the autoencoder
encoder = Model(inputs=autoencoder.input,
	outputs=autoencoder.get_layer("encoded").output)

# quantify the contents of our input testing images using the encoder
print("[INFO] encoding testing images...")
features = encoder.predict(testX)

# randomly sample a set of testing query image indexes
queryIdxs = list(range(0, testX.shape[0]))
#queryIdxs = np.random.choice(queryIdxs, size=args["sample"],replace=False)
# loop over the testing indexes
for i in queryIdxs[0:2]:
	# take the features for the current image, find all similar
	# images in our dataset, and then initialize our list of result
	# images
	queryFeatures = features[i]
	filename = filenames[i]
	print(filename)
	results = perform_search(queryFeatures, index) #, maxResults=40)
	images = []
	images_names = []
	resmax = max(results, key=itemgetter(1))[0]
	resmin = min(results, key=itemgetter(1))[0]
	threshold = (resmax + resmin) / 2
	# loop over the results
	my_list = []
	with open(path + 'results' + str(i) + '.txt', 'w') as f:
		for (d, j) in results:
			# grab the result image, convert it back to the range
			# [0, 255], and then update the images list

			if d >=  0: #== resmax: #<= threshold:
				names = index["filenames"]
				#names = [item for sublist in names for item in sublist]
				#names = np.array(names)
				name = names[j]
				img = cv2.imread(name)
				images_names.append(name)


				f.write('query: ' + str(name) + ' score ' + str(d) + '\n')

				image = cv2.resize(img, (width, height))
				#image = (trainX[j] * 255).astype("uint8")
				image = np.dstack([image])
				images.append(image)

	# display the query image
	query = (testX[i] * 255).astype("uint8")
	#cv2.imshow("Query", query)

	show_images(images_names, filenames[i]) #query)

	#cv2.imshow("Query", query)

	cv2.imshow("Query", query)
	print(np.array(images).shape)
	# build a montage from the results and display it
	montage = imutils.build_montages(images, (60, 40), (20, 20))[0]
	cv2.waitKey(0)
	cv2.imshow("Results", montage)

